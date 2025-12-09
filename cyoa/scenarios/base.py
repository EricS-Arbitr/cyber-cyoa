"""Base classes for scenarios and questions."""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Callable
from enum import Enum


class QuestionType(Enum):
    """Types of questions available."""
    MULTIPLE_CHOICE = "multiple_choice"
    RANKING = "ranking"
    FREE_TEXT = "free_text"
    CHECKLIST = "checklist"
    TABLE = "table"


@dataclass
class Question:
    """Base class for all question types."""

    id: str
    text: str
    feedback_correct: str
    feedback_incorrect: str
    model_answer: str
    correct_answer: Any = None
    hint: Optional[str] = None
    points: int = 1
    question_type: QuestionType = field(default=QuestionType.FREE_TEXT)

    def check_answer(self, answer: Any) -> tuple:
        """
        Check if answer is correct.

        Returns:
            Tuple of (is_correct: bool, score: float, feedback: str)
        """
        raise NotImplementedError("Subclasses must implement check_answer")


@dataclass
class MultipleChoiceQuestion(Question):
    """Multiple choice question with single correct answer."""

    options: List[tuple] = field(default_factory=list)  # [(key, text), ...]

    def __post_init__(self):
        self.question_type = QuestionType.MULTIPLE_CHOICE

    def check_answer(self, answer: str) -> tuple:
        """Check multiple choice answer."""
        is_correct = answer.upper() == self.correct_answer.upper()
        score = self.points if is_correct else 0
        feedback = self.feedback_correct if is_correct else self.feedback_incorrect
        return (is_correct, score, feedback)


@dataclass
class RankingQuestion(Question):
    """Question where user ranks items in order."""

    items: List[str] = field(default_factory=list)
    num_ranks: int = 3

    def __post_init__(self):
        self.question_type = QuestionType.RANKING

    def check_answer(self, answer: List[int]) -> tuple:
        """
        Check ranking answer.

        Partial credit for close rankings.
        """
        if answer == self.correct_answer:
            return (True, self.points, self.feedback_correct)

        # Calculate partial score based on position matches
        correct_positions = sum(
            1 for i, val in enumerate(answer)
            if i < len(self.correct_answer) and val == self.correct_answer[i]
        )

        if correct_positions > 0:
            partial_score = (correct_positions / len(self.correct_answer)) * self.points
            feedback = f"Partially correct. {self.feedback_incorrect}"
            return (False, partial_score, feedback)

        return (False, 0, self.feedback_incorrect)


@dataclass
class FreeTextQuestion(Question):
    """Open-ended text response question."""

    required_keywords: List[str] = field(default_factory=list)
    bonus_keywords: List[str] = field(default_factory=list)
    min_keywords: int = 2

    def __post_init__(self):
        self.question_type = QuestionType.FREE_TEXT

    def check_answer(self, answer: str) -> tuple:
        """
        Check free text answer using keyword matching.

        Returns partial credit based on keywords found.
        """
        answer_lower = answer.lower()

        # Count required keywords found
        required_found = sum(
            1 for kw in self.required_keywords
            if kw.lower() in answer_lower
        )

        # Count bonus keywords found
        bonus_found = sum(
            1 for kw in self.bonus_keywords
            if kw.lower() in answer_lower
        )

        total_required = len(self.required_keywords)

        if total_required == 0:
            # No keywords defined - accept any substantial answer
            return (True, self.points, self.feedback_correct)

        if required_found >= total_required:
            # All required keywords found
            bonus_score = min(bonus_found * 0.1, 0.3)  # Up to 30% bonus
            score = min(self.points * (1 + bonus_score), self.points)
            feedback = "Excellent response! " + self.feedback_correct
            return (True, score, feedback)

        elif required_found >= self.min_keywords:
            # Partial credit
            ratio = required_found / total_required
            score = self.points * ratio
            missing = [kw for kw in self.required_keywords if kw.lower() not in answer_lower]
            feedback = f"Good response, but consider also discussing: {', '.join(missing[:3])}"
            return (False, score, feedback)

        else:
            # Not enough keywords
            feedback = self.feedback_incorrect
            return (False, 0, feedback)


@dataclass
class ChecklistQuestion(Question):
    """Question where user selects multiple correct options."""

    options: List[tuple] = field(default_factory=list)  # [(key, text), ...]
    correct_answers: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.question_type = QuestionType.CHECKLIST

    def check_answer(self, answers: List[str]) -> tuple:
        """Check checklist answer."""
        answers_upper = set(a.upper() for a in answers)
        correct_upper = set(a.upper() for a in self.correct_answers)

        if answers_upper == correct_upper:
            return (True, self.points, self.feedback_correct)

        # Partial credit
        correct_selected = len(answers_upper & correct_upper)
        incorrect_selected = len(answers_upper - correct_upper)
        total_correct = len(correct_upper)

        if correct_selected > 0 and incorrect_selected == 0:
            # Some correct, none wrong
            score = (correct_selected / total_correct) * self.points
            feedback = f"Partially correct. You identified {correct_selected} of {total_correct} correct options."
            return (False, score, feedback)

        elif correct_selected > incorrect_selected:
            # More right than wrong
            score = max(0, (correct_selected - incorrect_selected) / total_correct) * self.points
            feedback = self.feedback_incorrect
            return (False, score, feedback)

        return (False, 0, self.feedback_incorrect)


@dataclass
class Scenario:
    """A scenario containing multiple questions."""

    id: str
    title: str
    description: str
    questions: List[Question] = field(default_factory=list)

    def get_total_points(self) -> int:
        """Get total possible points for this scenario."""
        return sum(q.points for q in self.questions)


@dataclass
class Exercise:
    """An exercise containing multiple scenarios."""

    id: str
    number: int
    title: str
    description: str
    estimated_time: str
    objectives: List[str] = field(default_factory=list)
    scenarios: List[Scenario] = field(default_factory=list)

    def get_total_points(self) -> int:
        """Get total possible points for this exercise."""
        return sum(s.get_total_points() for s in self.scenarios)

    def get_total_questions(self) -> int:
        """Get total number of questions in this exercise."""
        return sum(len(s.questions) for s in self.scenarios)
