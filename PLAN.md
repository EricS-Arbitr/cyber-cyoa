# Cyber CYOA Application - Implementation Plan

## Overview

Create a choose-your-own-adventure style CLI Python application that guides learners through the Module 1 Cybersecurity Foundations lab scenarios, providing interactive feedback based on their answers.

## Key Requirements

- **Offline Operation**: No internet access required in final environment
- **Interactive CLI**: Terminal-based interface for scenario navigation
- **Feedback System**: Provide educational feedback on learner answers
- **Progress Tracking**: Track which exercises are completed
- **Self-contained**: All content embedded in the application
- **Zero Dependencies**: Standard library only for maximum portability

## Why CLI Adventure?

1. **True CYOA Feel**: Immersive, game-like experience
2. **Zero Dependencies**: Runs anywhere with Python 3.6+
3. **Simple Deployment**: Single directory, no installation needed
4. **Works Offline**: No network required
5. **Engaging**: More interactive than static documents

## Architecture

### File Structure

```
cyber_cyoa/
├── main.py                     # Entry point
├── cyoa/
│   ├── __init__.py
│   ├── engine.py               # Core game engine (navigation, state)
│   ├── ui.py                   # Terminal UI (colors, formatting, input)
│   ├── feedback.py             # Answer evaluation and feedback
│   ├── progress.py             # Progress tracking (JSON persistence)
│   └── scenarios/
│       ├── __init__.py
│       ├── base.py             # Base classes for scenarios/questions
│       ├── exercise1.py        # CIA Triad Analysis
│       ├── exercise2.py        # Threat Actor Analysis
│       ├── exercise3.py        # Mission Impact Analysis
│       ├── exercise4.py        # Ethical Scenarios
│       └── exercise5.py        # Comprehensive Assessment
├── data/
│   └── progress.json           # Saved progress (created at runtime)
└── Module_1_Lab_Cybersecurity_Foundations.md  # Original reference
```

### Core Components

#### 1. UI Module (`ui.py`)
- ANSI color codes (with fallback for Windows)
- Screen clearing
- Text wrapping for readability
- Box drawing for visual separation
- Input prompts with validation
- Progress indicators

#### 2. Engine (`engine.py`)
- Main game loop
- Menu navigation
- State management
- Exercise/scenario flow control

#### 3. Question Types (`scenarios/base.py`)
- `MultipleChoice`: Select one option (A/B/C)
- `Ranking`: Order items 1-3 or 1-5
- `FreeText`: Open response with keyword evaluation
- `Checklist`: Select all that apply

#### 4. Feedback System (`feedback.py`)
- Immediate feedback after each question
- Keyword matching for free text
- Tiered responses (Excellent/Good/Needs Review)
- Model answers revealed after submission

### User Flow

```
┌─────────────────────────────────────┐
│     CYBERSECURITY FOUNDATIONS       │
│        Interactive Training         │
└─────────────────────────────────────┘

[1] Start New Session
[2] Continue Previous Session
[3] View Progress
[4] Exit

> 1

┌─────────────────────────────────────┐
│         SELECT EXERCISE             │
└─────────────────────────────────────┘

[1] CIA Triad Analysis          [Not Started]
[2] Threat Actor Analysis       [Not Started]
[3] Mission Impact Analysis     [Not Started]
[4] Ethical Scenarios           [Not Started]
[5] Comprehensive Assessment    [Not Started]
[B] Back to Main Menu

> 1
```

### Sample Interaction

```
════════════════════════════════════════════════════════════════
              EXERCISE 1: CIA TRIAD ANALYSIS
════════════════════════════════════════════════════════════════

SCENARIO 1A: Intelligence Database
────────────────────────────────────────────────────────────────

An intelligence database contains information about enemy force
positions, capabilities, and intentions. The database is accessed
by analysts at multiple locations worldwide via classified networks.
Analysts use this information to brief commanders and develop
operational recommendations.

────────────────────────────────────────────────────────────────

QUESTION 1: Which CIA property is MOST critical for this system?

  [C] Confidentiality
  [I] Integrity
  [A] Availability

Your answer: C

┌────────────────────────────────────────────────────────────┐
│  ✓ CORRECT!                                                │
│                                                            │
│  Confidentiality is indeed most critical for an            │
│  intelligence database. If this information were           │
│  disclosed to adversaries, it could:                       │
│                                                            │
│  • Compromise ongoing operations                           │
│  • Endanger personnel whose positions are known            │
│  • Provide strategic advantage to enemies                  │
│                                                            │
│  While integrity and availability are important, the       │
│  classified nature of intelligence data makes              │
│  confidentiality paramount.                                │
└────────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Implementation Phases

### Phase 1: Core Framework
- [ ] Create project structure
- [ ] Implement ui.py (colors, formatting, input)
- [ ] Implement base.py (question classes)
- [ ] Implement engine.py (navigation, menus)
- [ ] Implement progress.py (save/load)
- [ ] Implement feedback.py (evaluation)

### Phase 2: Exercise 1 - CIA Triad
- [ ] Scenario 1A: Intelligence Database (4 questions)
- [ ] Scenario 1B: Logistics System (3 questions)
- [ ] Scenario 1C: C2 Network (3 questions)

### Phase 3: Exercise 2 - Threat Actor Analysis
- [ ] Part A: Threat Actor Profiling
- [ ] Part B: Target Analysis
- [ ] Part C: Defense Recommendations

### Phase 4: Exercises 3-4
- [ ] Exercise 3: Mission Impact Analysis
- [ ] Exercise 4: Ethical Scenarios (4 scenarios)

### Phase 5: Exercise 5 & Polish
- [ ] Comprehensive Assessment
- [ ] Final testing
- [ ] Progress summary screen

## Dependencies

**None** - Standard library only:
- `json` - Progress persistence
- `os` - Screen clearing, paths
- `textwrap` - Text formatting
- `re` - Keyword matching
- `difflib` - Fuzzy matching (optional)
