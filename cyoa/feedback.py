"""Feedback and answer evaluation utilities."""

import re
from typing import List, Tuple, Optional
from difflib import SequenceMatcher

from .scenarios.base import (
    Question,
    MultipleChoiceQuestion,
    RankingQuestion,
    FreeTextQuestion,
    ChecklistQuestion,
    QuestionType,
)
from . import ui


def evaluate_answer(question: Question, answer) -> Tuple[bool, float, str]:
    """
    Evaluate an answer to a question.

    Args:
        question: The question being answered
        answer: The user's answer

    Returns:
        Tuple of (is_correct, score, feedback)
    """
    return question.check_answer(answer)


def display_feedback(
    is_correct: bool,
    score: float,
    feedback: str,
    model_answer: Optional[str] = None,
    show_model: bool = True
):
    """
    Display feedback to the user.

    Args:
        is_correct: Whether the answer was fully correct
        score: Score earned (0 to max points)
        feedback: Feedback text to display
        model_answer: Optional model answer to show
        show_model: Whether to show the model answer
    """
    if is_correct:
        ui.print_success_box(feedback)
    elif score > 0:
        ui.print_partial_box(feedback)
    else:
        ui.print_incorrect_box(feedback)

    if show_model and model_answer:
        ui.print_model_answer(model_answer)


def keyword_match_score(text: str, keywords: List[str]) -> Tuple[int, List[str], List[str]]:
    """
    Check how many keywords are present in text.

    Args:
        text: The text to search
        keywords: List of keywords to find

    Returns:
        Tuple of (count_found, keywords_found, keywords_missing)
    """
    text_lower = text.lower()
    found = []
    missing = []

    for keyword in keywords:
        # Handle multi-word keywords and variations
        kw_lower = keyword.lower()

        # Try exact match first
        if kw_lower in text_lower:
            found.append(keyword)
        # Try word boundary match
        elif re.search(r'\b' + re.escape(kw_lower) + r'\b', text_lower):
            found.append(keyword)
        else:
            missing.append(keyword)

    return (len(found), found, missing)


def fuzzy_match(text1: str, text2: str) -> float:
    """
    Calculate fuzzy match ratio between two strings.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Similarity ratio (0 to 1)
    """
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()


def evaluate_free_text_detailed(
    response: str,
    required_concepts: List[str],
    optional_concepts: List[str] = None,
    min_required: int = 2
) -> dict:
    """
    Detailed evaluation of free text response.

    Args:
        response: User's response
        required_concepts: Concepts that should be mentioned
        optional_concepts: Bonus concepts
        min_required: Minimum required concepts for partial credit

    Returns:
        Dictionary with evaluation details
    """
    optional_concepts = optional_concepts or []

    required_found, req_matched, req_missing = keyword_match_score(response, required_concepts)
    optional_found, opt_matched, opt_missing = keyword_match_score(response, optional_concepts)

    total_required = len(required_concepts)

    if required_found >= total_required:
        rating = "excellent"
        score_pct = 100 + (optional_found * 5)  # Bonus for optional
    elif required_found >= min_required:
        rating = "good"
        score_pct = int((required_found / total_required) * 100)
    elif required_found > 0:
        rating = "partial"
        score_pct = int((required_found / total_required) * 50)
    else:
        rating = "needs_improvement"
        score_pct = 0

    return {
        "rating": rating,
        "score_pct": min(score_pct, 100),
        "required_found": required_found,
        "required_total": total_required,
        "required_matched": req_matched,
        "required_missing": req_missing,
        "optional_found": optional_found,
        "optional_matched": opt_matched,
    }


def generate_text_feedback(evaluation: dict) -> str:
    """
    Generate feedback text from evaluation results.

    Args:
        evaluation: Dictionary from evaluate_free_text_detailed

    Returns:
        Formatted feedback string
    """
    rating = evaluation["rating"]

    if rating == "excellent":
        feedback = "Excellent response! You've demonstrated a thorough understanding of the key concepts."
        if evaluation["optional_found"] > 0:
            feedback += f"\n\nBonus: You also covered additional relevant concepts: {', '.join(evaluation['optional_matched'])}"

    elif rating == "good":
        feedback = f"Good response! You covered {evaluation['required_found']} of {evaluation['required_total']} key concepts."
        if evaluation["required_missing"]:
            feedback += f"\n\nConsider also discussing: {', '.join(evaluation['required_missing'][:3])}"

    elif rating == "partial":
        feedback = "You're on the right track but missed some important concepts."
        feedback += f"\n\nKey concepts to include: {', '.join(evaluation['required_missing'][:4])}"

    else:
        feedback = "Your response needs more detail on the key concepts."
        feedback += f"\n\nImportant concepts to address: {', '.join(evaluation['required_missing'][:4])}"

    return feedback


def compare_rankings(user_ranking: List[int], correct_ranking: List[int]) -> dict:
    """
    Compare user's ranking to correct ranking.

    Args:
        user_ranking: User's ranking (list of item indices)
        correct_ranking: Correct ranking

    Returns:
        Dictionary with comparison details
    """
    exact_matches = sum(
        1 for i, val in enumerate(user_ranking)
        if i < len(correct_ranking) and val == correct_ranking[i]
    )

    # Check if items are at least in the list (order agnostic)
    items_included = sum(
        1 for val in user_ranking
        if val in correct_ranking
    )

    # Calculate order correlation (simplified)
    total = len(correct_ranking)
    position_errors = 0
    for i, val in enumerate(user_ranking):
        if val in correct_ranking:
            correct_pos = correct_ranking.index(val)
            position_errors += abs(i - correct_pos)

    max_errors = total * (total - 1)  # Maximum possible position errors
    order_score = 1 - (position_errors / max_errors) if max_errors > 0 else 1

    return {
        "exact_matches": exact_matches,
        "total_positions": total,
        "items_included": items_included,
        "order_score": order_score,
        "is_perfect": exact_matches == total,
    }
