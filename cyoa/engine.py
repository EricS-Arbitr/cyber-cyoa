"""Core game engine for the CYOA application."""

from typing import List, Optional, Callable
from datetime import datetime

from . import ui
from .progress import ProgressManager
from .feedback import evaluate_answer, display_feedback
from .scenarios.base import (
    Exercise,
    Scenario,
    Question,
    MultipleChoiceQuestion,
    RankingQuestion,
    FreeTextQuestion,
    ChecklistQuestion,
    QuestionType,
)


class GameEngine:
    """Main game engine handling navigation and flow."""

    def __init__(self, data_dir: str = "data"):
        """Initialize the game engine."""
        self.progress = ProgressManager(data_dir)
        self.exercises: List[Exercise] = []
        self.current_exercise: Optional[Exercise] = None
        self.current_scenario: Optional[Scenario] = None
        self.running = True

    def register_exercise(self, exercise: Exercise):
        """Register an exercise with the engine."""
        self.exercises.append(exercise)
        # Sort by exercise number
        self.exercises.sort(key=lambda e: e.number)

    def run(self):
        """Main game loop."""
        self.running = True

        while self.running:
            self.show_main_menu()

    def show_main_menu(self):
        """Display the main menu."""
        ui.clear_screen()
        ui.print_header(
            "CYBERSECURITY FOUNDATIONS",
            "Interactive Training Lab"
        )

        # Check for existing progress
        existing = self.progress.load_session()

        options = []
        if existing:
            completion = self.progress.session.get_overall_completion()
            options.append(("1", f"Continue Session ({completion:.0f}% complete)"))
            options.append(("2", "Start New Session"))
            options.append(("3", "View Progress"))
            options.append(("Q", "Exit"))
        else:
            options.append(("1", "Start New Session"))
            options.append(("Q", "Exit"))

        ui.print_menu(options)

        if existing:
            choice = ui.get_input("> ", ["1", "2", "3", "Q"])
            if choice == "1":
                self.show_exercise_menu()
            elif choice == "2":
                self.confirm_new_session()
            elif choice == "3":
                self.show_progress()
            elif choice == "Q":
                self.exit_game()
        else:
            choice = ui.get_input("> ", ["1", "Q"])
            if choice == "1":
                self.progress.new_session()
                self.progress.save_session()
                self.show_exercise_menu()
            elif choice == "Q":
                self.exit_game()

    def confirm_new_session(self):
        """Confirm starting a new session (losing existing progress)."""
        ui.clear_screen()
        ui.print_header("START NEW SESSION")

        print(f"{ui.Colors.YELLOW}Warning: This will erase your existing progress.{ui.Colors.RESET}")
        print()

        options = [("Y", "Yes, start fresh"), ("N", "No, go back")]
        ui.print_menu(options)

        choice = ui.get_input("> ", ["Y", "N"])
        if choice == "Y":
            self.progress.reset_progress()
            self.progress.new_session()
            self.progress.save_session()
            self.show_exercise_menu()

    def show_exercise_menu(self):
        """Display the exercise selection menu."""
        while self.running:
            ui.clear_screen()
            ui.print_header("SELECT EXERCISE")

            options = []
            for i, exercise in enumerate(self.exercises, 1):
                # Get status for this exercise
                ex_progress = self.progress.get_exercise_progress(exercise.id)

                if ex_progress.completed:
                    status = f"{ui.Colors.GREEN}[Completed]{ui.Colors.RESET}"
                elif ex_progress.started:
                    pct = ex_progress.get_completion_pct()
                    status = f"{ui.Colors.YELLOW}[{pct:.0f}% Complete]{ui.Colors.RESET}"
                else:
                    status = f"{ui.Colors.DIM}[Not Started]{ui.Colors.RESET}"

                options.append((str(i), f"{exercise.title}  {status}"))

            options.append(("P", "View Progress"))
            options.append(("B", "Back to Main Menu"))

            ui.print_menu(options)

            valid = [str(i) for i in range(1, len(self.exercises) + 1)] + ["P", "B"]
            choice = ui.get_input("> ", valid)

            if choice == "B":
                return
            elif choice == "P":
                self.show_progress()
            elif choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.exercises):
                    self.run_exercise(self.exercises[idx])

    def show_progress(self):
        """Display progress summary."""
        ui.clear_screen()
        ui.print_header("YOUR PROGRESS")

        summary = self.progress.get_summary()

        if not summary.get("has_progress"):
            print("No progress recorded yet. Start an exercise to begin!")
        else:
            # Overall progress
            ui.print_progress_bar(
                int(summary["completion_pct"]),
                100,
                label="Overall Progress"
            )
            print()

            # Per-exercise progress
            for exercise in self.exercises:
                ex_data = summary["exercises"].get(exercise.id, {})

                if ex_data.get("completed"):
                    status = f"{ui.Colors.GREEN}Complete{ui.Colors.RESET}"
                elif ex_data.get("started"):
                    status = f"{ui.Colors.YELLOW}In Progress{ui.Colors.RESET}"
                else:
                    status = f"{ui.Colors.DIM}Not Started{ui.Colors.RESET}"

                pct = ex_data.get("completion_pct", 0)
                score = ex_data.get("score", 0)

                print(f"\n{ui.Colors.BOLD}Exercise {exercise.number}: {exercise.title}{ui.Colors.RESET}")
                print(f"  Status: {status}")
                if ex_data.get("started"):
                    ui.print_progress_bar(int(pct), 100, width=25, label="  Progress")
                    print(f"  Score: {score:.1f} points")

            print()
            print(f"{ui.Colors.DIM}Session started: {summary.get('created', 'Unknown')}{ui.Colors.RESET}")
            print(f"{ui.Colors.DIM}Last updated: {summary.get('last_updated', 'Unknown')}{ui.Colors.RESET}")

        ui.wait_for_enter()

    def run_exercise(self, exercise: Exercise):
        """Run through an exercise."""
        self.current_exercise = exercise

        # Show exercise intro
        ui.clear_screen()
        ui.print_header(
            f"EXERCISE {exercise.number}: {exercise.title.upper()}",
            f"Estimated Time: {exercise.estimated_time}"
        )

        print(ui.wrap_text(exercise.description))
        print()

        if exercise.objectives:
            print(f"{ui.Colors.BOLD}Objectives:{ui.Colors.RESET}")
            for obj in exercise.objectives:
                print(f"  • {obj}")
            print()

        ui.wait_for_enter("Press Enter to begin...")

        # Run each scenario
        for scenario in exercise.scenarios:
            if not self.running:
                break
            self.run_scenario(exercise, scenario)

        # Mark exercise complete if all scenarios done
        ex_progress = self.progress.get_exercise_progress(exercise.id)
        all_complete = all(
            self.progress.get_scenario_progress(exercise.id, s.id).completed
            for s in exercise.scenarios
        )
        if all_complete:
            ex_progress.completed = True
            self.progress.save_session()

            ui.clear_screen()
            ui.print_header("EXERCISE COMPLETE!")

            score = ex_progress.get_score()
            total = exercise.get_total_points()

            print(f"{ui.Colors.GREEN}Congratulations!{ui.Colors.RESET}")
            print(f"\nYou've completed Exercise {exercise.number}: {exercise.title}")
            print(f"\nYour score: {score:.1f} / {total} points ({score/total*100:.0f}%)")

            ui.wait_for_enter()

        self.current_exercise = None

    def run_scenario(self, exercise: Exercise, scenario: Scenario):
        """Run through a scenario."""
        self.current_scenario = scenario

        # Check if already completed
        sc_progress = self.progress.get_scenario_progress(exercise.id, scenario.id)
        if sc_progress.completed:
            # Ask if user wants to redo
            ui.clear_screen()
            ui.print_scenario_title(scenario.title)
            print(f"{ui.Colors.GREEN}You've already completed this scenario.{ui.Colors.RESET}")
            print()

            options = [("R", "Redo scenario"), ("S", "Skip to next"), ("B", "Back to menu")]
            ui.print_menu(options)

            choice = ui.get_input("> ", ["R", "S", "B"])
            if choice == "S":
                return
            elif choice == "B":
                self.current_scenario = None
                return

        # Show scenario description
        ui.clear_screen()
        ui.print_header(f"EXERCISE {exercise.number}: {exercise.title.upper()}")
        ui.print_scenario_title(scenario.title)

        print(ui.wrap_text(scenario.description))
        print()
        ui.print_divider()

        # Run each question
        for i, question in enumerate(scenario.questions, 1):
            if not self.running:
                break
            self.run_question(exercise, scenario, question, i)

        # Mark scenario complete
        self.progress.mark_scenario_complete(exercise.id, scenario.id)

        self.current_scenario = None

    def run_question(
        self,
        exercise: Exercise,
        scenario: Scenario,
        question: Question,
        number: int
    ):
        """Run a single question."""
        ui.print_question(number, question.text)

        # Get answer based on question type
        if isinstance(question, MultipleChoiceQuestion):
            answer = self.get_multiple_choice_answer(question)
        elif isinstance(question, RankingQuestion):
            answer = self.get_ranking_answer(question)
        elif isinstance(question, FreeTextQuestion):
            answer = self.get_free_text_answer(question)
        elif isinstance(question, ChecklistQuestion):
            answer = self.get_checklist_answer(question)
        else:
            # Default to text input
            answer = ui.get_text_input("Your answer:", min_length=5)

        # Evaluate answer
        is_correct, score, feedback = evaluate_answer(question, answer)

        # Display feedback
        display_feedback(is_correct, score, feedback, question.model_answer)

        # Record progress
        self.progress.record_answer(
            exercise.id,
            scenario.id,
            question.id,
            answer,
            is_correct,
            score
        )

        ui.wait_for_enter()

    def get_multiple_choice_answer(self, question: MultipleChoiceQuestion) -> str:
        """Get answer for multiple choice question."""
        ui.print_options(question.options)

        valid_keys = [opt[0].upper() for opt in question.options]
        return ui.get_input("Your answer: ", valid_keys)

    def get_ranking_answer(self, question: RankingQuestion) -> List[int]:
        """Get answer for ranking question."""
        return ui.get_ranking_input(question.items, question.num_ranks)

    def get_free_text_answer(self, question: FreeTextQuestion) -> str:
        """Get answer for free text question."""
        if question.hint:
            print(f"{ui.Colors.DIM}Hint: {question.hint}{ui.Colors.RESET}")
            print()

        return ui.get_text_input("Your answer:", min_length=20)

    def get_checklist_answer(self, question: ChecklistQuestion) -> List[str]:
        """Get answer for checklist question."""
        print(f"{ui.Colors.DIM}(Enter letters separated by commas, e.g., A,B,D){ui.Colors.RESET}")
        print()

        for key, text in question.options:
            print(f"  {ui.Colors.CYAN}[{key}]{ui.Colors.RESET} {text}")
        print()

        while True:
            response = ui.get_input("Your selections: ")
            # Parse comma-separated values
            selections = [s.strip().upper() for s in response.split(",") if s.strip()]

            valid_keys = [opt[0].upper() for opt in question.options]
            if all(s in valid_keys for s in selections):
                return selections

            print(f"{ui.Colors.YELLOW}Please enter valid options separated by commas.{ui.Colors.RESET}")

    def exit_game(self):
        """Exit the game."""
        ui.clear_screen()
        print()
        print(f"{ui.Colors.CYAN}Thank you for using the Cybersecurity Foundations Training Lab!{ui.Colors.RESET}")
        print()

        if self.progress.session:
            summary = self.progress.get_summary()
            print(f"Your progress ({summary.get('completion_pct', 0):.0f}% complete) has been saved.")
            print("You can continue where you left off next time.")
            print()

        self.running = False
