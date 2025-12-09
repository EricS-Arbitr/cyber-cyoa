#!/usr/bin/env python3
"""
Cybersecurity Foundations - Interactive Training Lab

A choose-your-own-adventure style training application for the
Cyber Defense Infrastructure Support Specialist Course, Module 1.

Run with: python main.py
"""

import os
import sys

# Ensure we can import from the cyoa package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cyoa.engine import GameEngine
from cyoa.scenarios import (
    get_exercise1,
    get_exercise2,
    get_exercise3,
    get_exercise4,
    get_exercise5,
)


def main():
    """Main entry point for the application."""
    # Determine data directory (same directory as script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")

    # Create the game engine
    engine = GameEngine(data_dir=data_dir)

    # Register all exercises
    engine.register_exercise(get_exercise1())
    engine.register_exercise(get_exercise2())
    engine.register_exercise(get_exercise3())
    engine.register_exercise(get_exercise4())
    engine.register_exercise(get_exercise5())

    # Run the game
    try:
        engine.run()
    except KeyboardInterrupt:
        print("\n\nExiting... Your progress has been saved.")
        sys.exit(0)


if __name__ == "__main__":
    main()
