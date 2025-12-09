# Cyber CYOA

A choose-your-own-adventure style CLI training application for the Cyber Defense Infrastructure Support Specialist Course, Module 1: Cybersecurity Foundations.

## Overview

This interactive terminal application guides learners through cybersecurity scenarios, providing immediate feedback on their decisions. It covers core concepts including the CIA Triad, threat actor analysis, mission impact assessment, and ethical decision-making.

## Features

- **Interactive CLI** - Terminal-based interface with colored output and formatted text
- **5 Training Exercises** - Progressive scenarios covering foundational cybersecurity concepts
- **Immediate Feedback** - Educational explanations for each answer
- **Progress Tracking** - Automatically saves completion status
- **Zero Dependencies** - Uses only Python standard library
- **Offline Operation** - No internet connection required

## Requirements

- Python 3.6+

## Usage

```bash
python main.py
```

## Exercises

1. **CIA Triad Analysis** - Evaluate confidentiality, integrity, and availability priorities for military systems
2. **Threat Actor Analysis** - Profile adversaries and analyze their tactics, techniques, and procedures
3. **Mission Impact Analysis** - Assess how cyber incidents affect operational missions
4. **Ethical Scenarios** - Navigate complex ethical situations in cybersecurity
5. **Comprehensive Assessment** - Apply all concepts in integrated scenarios

## Project Structure

```
cyber-cyoa/
├── main.py              # Entry point
├── cyoa/
│   ├── engine.py        # Core game engine
│   ├── ui.py            # Terminal UI formatting
│   ├── feedback.py      # Answer evaluation
│   ├── progress.py      # Progress persistence
│   └── scenarios/       # Exercise modules
│       ├── base.py      # Base classes
│       └── exercise*.py # Individual exercises
└── data/
    └── progress.json    # Saved progress (auto-generated)
```

## License

See [LICENSE](LICENSE) for details.
