"""Progress tracking and persistence."""

import json
import os
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from datetime import datetime


@dataclass
class QuestionProgress:
    """Progress for a single question."""

    question_id: str
    answered: bool = False
    correct: bool = False
    score: float = 0.0
    attempts: int = 0
    user_answer: Any = None
    timestamp: Optional[str] = None


@dataclass
class ScenarioProgress:
    """Progress for a scenario."""

    scenario_id: str
    started: bool = False
    completed: bool = False
    questions: Dict[str, QuestionProgress] = field(default_factory=dict)

    def get_score(self) -> float:
        """Get total score for this scenario."""
        return sum(q.score for q in self.questions.values())

    def get_completion_pct(self) -> float:
        """Get completion percentage."""
        if not self.questions:
            return 0.0
        answered = sum(1 for q in self.questions.values() if q.answered)
        return (answered / len(self.questions)) * 100


@dataclass
class ExerciseProgress:
    """Progress for an exercise."""

    exercise_id: str
    started: bool = False
    completed: bool = False
    scenarios: Dict[str, ScenarioProgress] = field(default_factory=dict)

    def get_score(self) -> float:
        """Get total score for this exercise."""
        return sum(s.get_score() for s in self.scenarios.values())

    def get_completion_pct(self) -> float:
        """Get completion percentage."""
        if not self.scenarios:
            return 0.0
        total_questions = sum(len(s.questions) for s in self.scenarios.values())
        if total_questions == 0:
            return 0.0
        answered = sum(
            sum(1 for q in s.questions.values() if q.answered)
            for s in self.scenarios.values()
        )
        return (answered / total_questions) * 100


@dataclass
class SessionProgress:
    """Overall session progress."""

    session_id: str
    created: str
    last_updated: str
    exercises: Dict[str, ExerciseProgress] = field(default_factory=dict)

    def get_total_score(self) -> float:
        """Get total score across all exercises."""
        return sum(e.get_score() for e in self.exercises.values())

    def get_overall_completion(self) -> float:
        """Get overall completion percentage."""
        if not self.exercises:
            return 0.0

        total = 0
        completed = 0
        for ex in self.exercises.values():
            for sc in ex.scenarios.values():
                total += len(sc.questions)
                completed += sum(1 for q in sc.questions.values() if q.answered)

        return (completed / total * 100) if total > 0 else 0.0


class ProgressManager:
    """Manages saving and loading progress."""

    def __init__(self, data_dir: str = "data"):
        """Initialize progress manager."""
        self.data_dir = data_dir
        self.progress_file = os.path.join(data_dir, "progress.json")
        self.session: Optional[SessionProgress] = None

    def ensure_data_dir(self):
        """Ensure data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)

    def new_session(self) -> SessionProgress:
        """Create a new session."""
        now = datetime.now().isoformat()
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.session = SessionProgress(
            session_id=session_id,
            created=now,
            last_updated=now,
            exercises={}
        )
        return self.session

    def load_session(self) -> Optional[SessionProgress]:
        """Load existing session from file."""
        if not os.path.exists(self.progress_file):
            return None

        try:
            with open(self.progress_file, 'r') as f:
                data = json.load(f)

            # Reconstruct dataclass objects
            self.session = SessionProgress(
                session_id=data.get("session_id", "unknown"),
                created=data.get("created", ""),
                last_updated=data.get("last_updated", ""),
                exercises={}
            )

            for ex_id, ex_data in data.get("exercises", {}).items():
                ex_progress = ExerciseProgress(
                    exercise_id=ex_id,
                    started=ex_data.get("started", False),
                    completed=ex_data.get("completed", False),
                    scenarios={}
                )

                for sc_id, sc_data in ex_data.get("scenarios", {}).items():
                    sc_progress = ScenarioProgress(
                        scenario_id=sc_id,
                        started=sc_data.get("started", False),
                        completed=sc_data.get("completed", False),
                        questions={}
                    )

                    for q_id, q_data in sc_data.get("questions", {}).items():
                        sc_progress.questions[q_id] = QuestionProgress(
                            question_id=q_id,
                            answered=q_data.get("answered", False),
                            correct=q_data.get("correct", False),
                            score=q_data.get("score", 0.0),
                            attempts=q_data.get("attempts", 0),
                            user_answer=q_data.get("user_answer"),
                            timestamp=q_data.get("timestamp")
                        )

                    ex_progress.scenarios[sc_id] = sc_progress

                self.session.exercises[ex_id] = ex_progress

            return self.session

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Warning: Could not load progress file: {e}")
            return None

    def save_session(self):
        """Save current session to file."""
        if not self.session:
            return

        self.ensure_data_dir()
        self.session.last_updated = datetime.now().isoformat()

        # Convert to dict for JSON serialization
        data = {
            "session_id": self.session.session_id,
            "created": self.session.created,
            "last_updated": self.session.last_updated,
            "exercises": {}
        }

        for ex_id, ex in self.session.exercises.items():
            data["exercises"][ex_id] = {
                "exercise_id": ex.exercise_id,
                "started": ex.started,
                "completed": ex.completed,
                "scenarios": {}
            }

            for sc_id, sc in ex.scenarios.items():
                data["exercises"][ex_id]["scenarios"][sc_id] = {
                    "scenario_id": sc.scenario_id,
                    "started": sc.started,
                    "completed": sc.completed,
                    "questions": {}
                }

                for q_id, q in sc.questions.items():
                    data["exercises"][ex_id]["scenarios"][sc_id]["questions"][q_id] = {
                        "question_id": q.question_id,
                        "answered": q.answered,
                        "correct": q.correct,
                        "score": q.score,
                        "attempts": q.attempts,
                        "user_answer": q.user_answer,
                        "timestamp": q.timestamp
                    }

        with open(self.progress_file, 'w') as f:
            json.dump(data, f, indent=2)

    def get_exercise_progress(self, exercise_id: str) -> ExerciseProgress:
        """Get or create progress for an exercise."""
        if not self.session:
            self.new_session()

        if exercise_id not in self.session.exercises:
            self.session.exercises[exercise_id] = ExerciseProgress(
                exercise_id=exercise_id
            )

        return self.session.exercises[exercise_id]

    def get_scenario_progress(
        self,
        exercise_id: str,
        scenario_id: str
    ) -> ScenarioProgress:
        """Get or create progress for a scenario."""
        ex_progress = self.get_exercise_progress(exercise_id)

        if scenario_id not in ex_progress.scenarios:
            ex_progress.scenarios[scenario_id] = ScenarioProgress(
                scenario_id=scenario_id
            )

        return ex_progress.scenarios[scenario_id]

    def record_answer(
        self,
        exercise_id: str,
        scenario_id: str,
        question_id: str,
        answer: Any,
        correct: bool,
        score: float
    ):
        """Record an answer to a question."""
        sc_progress = self.get_scenario_progress(exercise_id, scenario_id)

        # Mark exercise and scenario as started
        self.session.exercises[exercise_id].started = True
        sc_progress.started = True

        if question_id not in sc_progress.questions:
            sc_progress.questions[question_id] = QuestionProgress(
                question_id=question_id
            )

        q_progress = sc_progress.questions[question_id]
        q_progress.answered = True
        q_progress.correct = correct
        q_progress.score = score
        q_progress.attempts += 1
        q_progress.user_answer = answer
        q_progress.timestamp = datetime.now().isoformat()

        # Auto-save after each answer
        self.save_session()

    def mark_scenario_complete(self, exercise_id: str, scenario_id: str):
        """Mark a scenario as completed."""
        sc_progress = self.get_scenario_progress(exercise_id, scenario_id)
        sc_progress.completed = True

        # Check if all scenarios in exercise are complete
        ex_progress = self.get_exercise_progress(exercise_id)
        all_complete = all(s.completed for s in ex_progress.scenarios.values())
        if all_complete and ex_progress.scenarios:
            ex_progress.completed = True

        self.save_session()

    def get_summary(self) -> dict:
        """Get a summary of progress."""
        if not self.session:
            return {"has_progress": False}

        return {
            "has_progress": True,
            "session_id": self.session.session_id,
            "created": self.session.created,
            "last_updated": self.session.last_updated,
            "total_score": self.session.get_total_score(),
            "completion_pct": self.session.get_overall_completion(),
            "exercises": {
                ex_id: {
                    "started": ex.started,
                    "completed": ex.completed,
                    "score": ex.get_score(),
                    "completion_pct": ex.get_completion_pct()
                }
                for ex_id, ex in self.session.exercises.items()
            }
        }

    def reset_progress(self):
        """Reset all progress."""
        if os.path.exists(self.progress_file):
            os.remove(self.progress_file)
        self.session = None
