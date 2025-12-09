"""Terminal UI utilities for the CYOA application."""

import os
import sys
import textwrap
from typing import List, Optional, Tuple


# ANSI Color Codes
class Colors:
    """ANSI color codes for terminal output."""

    # Check if colors are supported
    ENABLED = sys.stdout.isatty() and os.name != 'nt' or os.environ.get('TERM')

    if ENABLED:
        RESET = "\033[0m"
        BOLD = "\033[1m"
        DIM = "\033[2m"
        ITALIC = "\033[3m"
        UNDERLINE = "\033[4m"

        # Colors
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE = "\033[37m"

        # Bright colors
        BRIGHT_RED = "\033[91m"
        BRIGHT_GREEN = "\033[92m"
        BRIGHT_YELLOW = "\033[93m"
        BRIGHT_BLUE = "\033[94m"
        BRIGHT_MAGENTA = "\033[95m"
        BRIGHT_CYAN = "\033[96m"
        BRIGHT_WHITE = "\033[97m"

        # Background colors
        BG_RED = "\033[41m"
        BG_GREEN = "\033[42m"
        BG_YELLOW = "\033[43m"
        BG_BLUE = "\033[44m"
    else:
        # No colors - empty strings
        RESET = BOLD = DIM = ITALIC = UNDERLINE = ""
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = ""
        BRIGHT_RED = BRIGHT_GREEN = BRIGHT_YELLOW = BRIGHT_BLUE = ""
        BRIGHT_MAGENTA = BRIGHT_CYAN = BRIGHT_WHITE = ""
        BG_RED = BG_GREEN = BG_YELLOW = BG_BLUE = ""


# Box drawing characters
class Box:
    """Unicode box drawing characters."""

    # Single line
    HORIZONTAL = "─"
    VERTICAL = "│"
    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOTTOM_LEFT = "└"
    BOTTOM_RIGHT = "┘"

    # Double line
    DOUBLE_HORIZONTAL = "═"
    DOUBLE_VERTICAL = "║"
    DOUBLE_TOP_LEFT = "╔"
    DOUBLE_TOP_RIGHT = "╗"
    DOUBLE_BOTTOM_LEFT = "╚"
    DOUBLE_BOTTOM_RIGHT = "╝"


# Terminal width
def get_terminal_width() -> int:
    """Get the current terminal width."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80  # Default fallback


def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_header(title: str, subtitle: Optional[str] = None):
    """Print a styled header."""
    width = min(get_terminal_width(), 70)

    print()
    print(f"{Colors.BRIGHT_CYAN}{Box.DOUBLE_HORIZONTAL * width}{Colors.RESET}")

    # Center the title
    padding = (width - len(title)) // 2
    print(f"{Colors.BOLD}{Colors.BRIGHT_WHITE}{' ' * padding}{title}{Colors.RESET}")

    if subtitle:
        padding = (width - len(subtitle)) // 2
        print(f"{Colors.DIM}{' ' * padding}{subtitle}{Colors.RESET}")

    print(f"{Colors.BRIGHT_CYAN}{Box.DOUBLE_HORIZONTAL * width}{Colors.RESET}")
    print()


def print_subheader(title: str):
    """Print a smaller section header."""
    width = min(get_terminal_width(), 70)

    print()
    print(f"{Colors.CYAN}{title}{Colors.RESET}")
    print(f"{Colors.DIM}{Box.HORIZONTAL * len(title)}{Colors.RESET}")
    print()


def print_scenario_title(title: str):
    """Print a scenario title with decorative line."""
    width = min(get_terminal_width(), 70)

    print()
    print(f"{Colors.BOLD}{Colors.YELLOW}{title}{Colors.RESET}")
    print(f"{Colors.DIM}{Box.HORIZONTAL * width}{Colors.RESET}")
    print()


def wrap_text(text: str, width: Optional[int] = None, indent: int = 0) -> str:
    """Wrap text to fit terminal width."""
    if width is None:
        width = min(get_terminal_width() - 4, 70)

    # Split on double newlines (paragraphs) first
    paragraphs = text.split('\n\n')
    wrapped_paragraphs = []

    for paragraph in paragraphs:
        if paragraph.strip():
            # Join single newlines within a paragraph (they're just from source formatting)
            joined = ' '.join(line.strip() for line in paragraph.split('\n') if line.strip())
            wrapped = textwrap.fill(
                joined,
                width=width - indent,
                initial_indent=' ' * indent,
                subsequent_indent=' ' * indent
            )
            wrapped_paragraphs.append(wrapped)
        else:
            wrapped_paragraphs.append('')

    return '\n\n'.join(wrapped_paragraphs)


def print_wrapped(text: str, indent: int = 0):
    """Print text wrapped to terminal width."""
    print(wrap_text(text, indent=indent))


def print_box(content: str, color: str = Colors.WHITE, width: Optional[int] = None):
    """Print content inside a box."""
    if width is None:
        width = min(get_terminal_width() - 4, 66)

    lines = []
    # Split on double newlines for paragraphs
    paragraphs = content.split('\n\n')

    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip():
            # Join single newlines within paragraph
            joined = ' '.join(line.strip() for line in paragraph.split('\n') if line.strip())
            wrapped = textwrap.fill(joined, width=width - 4)
            lines.extend(wrapped.split('\n'))
            # Add blank line between paragraphs (but not after the last one)
            if i < len(paragraphs) - 1:
                lines.append('')
        else:
            lines.append('')

    # Draw box
    print(f"{color}{Box.TOP_LEFT}{Box.HORIZONTAL * (width - 2)}{Box.TOP_RIGHT}{Colors.RESET}")

    for line in lines:
        padding = width - 4 - len(line)
        print(f"{color}{Box.VERTICAL}{Colors.RESET}  {line}{' ' * padding}  {color}{Box.VERTICAL}{Colors.RESET}")

    print(f"{color}{Box.BOTTOM_LEFT}{Box.HORIZONTAL * (width - 2)}{Box.BOTTOM_RIGHT}{Colors.RESET}")


def print_success_box(content: str):
    """Print a green success box."""
    print()
    print(f"{Colors.BRIGHT_GREEN}  ✓ CORRECT!{Colors.RESET}")
    print()
    print_box(content, color=Colors.GREEN)
    print()


def print_partial_box(content: str):
    """Print a yellow partial credit box."""
    print()
    print(f"{Colors.BRIGHT_YELLOW}  ~ PARTIALLY CORRECT{Colors.RESET}")
    print()
    print_box(content, color=Colors.YELLOW)
    print()


def print_incorrect_box(content: str):
    """Print a red incorrect box."""
    print()
    print(f"{Colors.BRIGHT_RED}  ✗ NOT QUITE{Colors.RESET}")
    print()
    print_box(content, color=Colors.RED)
    print()


def print_info_box(content: str):
    """Print a blue info box."""
    print()
    print_box(content, color=Colors.CYAN)
    print()


def print_model_answer(content: str):
    """Print a model answer section."""
    print()
    print(f"{Colors.DIM}{'─' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}MODEL ANSWER:{Colors.RESET}")
    print()
    print_wrapped(content, indent=2)
    print(f"{Colors.DIM}{'─' * 40}{Colors.RESET}")
    print()


def print_menu(options: List[Tuple[str, str]], title: Optional[str] = None):
    """
    Print a menu with options.

    Args:
        options: List of (key, description) tuples
        title: Optional menu title
    """
    if title:
        print(f"\n{Colors.BOLD}{title}{Colors.RESET}\n")

    for key, description in options:
        print(f"  {Colors.BRIGHT_CYAN}[{key}]{Colors.RESET} {description}")

    print()


def print_question(number: int, text: str):
    """Print a question with number."""
    print()
    print(f"{Colors.BOLD}{Colors.WHITE}QUESTION {number}:{Colors.RESET} {text}")
    print()


def print_options(options: List[Tuple[str, str]]):
    """Print multiple choice options."""
    for key, text in options:
        print(f"  {Colors.BRIGHT_CYAN}[{key}]{Colors.RESET} {text}")
    print()


def get_input(prompt: str = "> ", valid_options: Optional[List[str]] = None) -> str:
    """
    Get user input with optional validation.

    Args:
        prompt: The prompt to display
        valid_options: List of valid options (case-insensitive)

    Returns:
        The user's input (stripped and lowercased if validating)
    """
    while True:
        try:
            response = input(f"{Colors.BRIGHT_WHITE}{prompt}{Colors.RESET}").strip()

            if valid_options is None:
                return response

            if response.upper() in [opt.upper() for opt in valid_options]:
                return response.upper()

            print(f"{Colors.YELLOW}Please enter one of: {', '.join(valid_options)}{Colors.RESET}")

        except EOFError:
            return "Q"
        except KeyboardInterrupt:
            print()
            return "Q"


def get_text_input(prompt: str, min_length: int = 10):
    """
    Get multi-line text input from user.

    Args:
        prompt: The prompt to display
        min_length: Minimum character length required

    Returns:
        The user's response, or "Q" if user quit
    """
    print(f"{Colors.DIM}(Enter your response. Type 'DONE' on a new line when finished){Colors.RESET}")
    print(f"{Colors.DIM}(Minimum {min_length} characters required){Colors.RESET}")
    print()

    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "DONE":
                break
            if line.strip().upper() == "Q" and not lines:
                # Only allow Q to quit if it's the first input
                return "Q"
            lines.append(line)
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            return "Q"

    response = '\n'.join(lines).strip()

    if len(response) < min_length:
        print(f"{Colors.YELLOW}Response too short. Please provide more detail.{Colors.RESET}")
        return get_text_input(prompt, min_length)

    return response


def get_ranking_input(items: List[str], ranks: int = 3):
    """
    Get ranking input from user.

    Args:
        items: List of items to rank
        ranks: Number of ranks (e.g., 3 for 1st, 2nd, 3rd)

    Returns:
        List of indices representing the ranking, or "Q" if user quit
    """
    print(f"{Colors.DIM}(Enter the number of your choice for each rank){Colors.RESET}")
    print()

    # Display items with numbers
    for i, item in enumerate(items, 1):
        print(f"  {Colors.CYAN}[{i}]{Colors.RESET} {item}")
    print()

    ranking = []
    for rank in range(1, ranks + 1):
        while True:
            try:
                ordinal = {1: "1st", 2: "2nd", 3: "3rd"}.get(rank, f"{rank}th")
                choice = input(f"{Colors.BRIGHT_WHITE}{ordinal} place: {Colors.RESET}").strip()

                # Check for quit
                if choice.upper() == "Q":
                    return "Q"

                if choice.isdigit():
                    idx = int(choice)
                    if 1 <= idx <= len(items) and idx not in ranking:
                        ranking.append(idx)
                        break
                    elif idx in ranking:
                        print(f"{Colors.YELLOW}Already selected. Choose another.{Colors.RESET}")
                    else:
                        print(f"{Colors.YELLOW}Enter a number between 1 and {len(items)}{Colors.RESET}")
                else:
                    print(f"{Colors.YELLOW}Please enter a number.{Colors.RESET}")
            except (EOFError, KeyboardInterrupt):
                print()
                return "Q"  # Treat interrupt as quit

    return ranking


def wait_for_enter(message: str = "Press Enter to continue..."):
    """Wait for user to press Enter."""
    try:
        input(f"\n{Colors.DIM}{message}{Colors.RESET}")
    except (EOFError, KeyboardInterrupt):
        pass


def print_progress_bar(current: int, total: int, width: int = 30, label: str = ""):
    """Print a progress bar."""
    filled = int(width * current / total) if total > 0 else 0
    bar = "█" * filled + "░" * (width - filled)
    percent = (current / total * 100) if total > 0 else 0

    if label:
        print(f"{label}: {Colors.CYAN}[{bar}]{Colors.RESET} {percent:.0f}% ({current}/{total})")
    else:
        print(f"{Colors.CYAN}[{bar}]{Colors.RESET} {percent:.0f}% ({current}/{total})")


def print_divider(char: str = "─", width: Optional[int] = None):
    """Print a horizontal divider."""
    if width is None:
        width = min(get_terminal_width() - 4, 70)
    print(f"{Colors.DIM}{char * width}{Colors.RESET}")
