"""Exercise 3: Mission Impact Analysis scenarios."""

from .base import (
    Exercise,
    Scenario,
    MultipleChoiceQuestion,
    RankingQuestion,
    ChecklistQuestion,
)


def get_exercise() -> Exercise:
    """Create and return Exercise 3."""

    # Operation IRON SHIELD Background
    scenario_systems = Scenario(
        id="3a",
        title="Part A: Critical System Identification",
        description="""Operation IRON SHIELD

You are the Cyber Defense Infrastructure Support Specialist supporting a Joint Task Force (JTF)
headquarters conducting a multinational peacekeeping operation.

Operation Details:
- Forces: 5,000 personnel from three nations
- Duration: 12-month deployment
- Location: Forward operating base in a partner nation
- Mission: Protect civilian population, support local government, deter hostile actors
- Threat Environment: Regional adversary with cyber capabilities, local criminals, insider threats

Your first task is to identify and prioritize the critical information systems supporting this mission.""",
        questions=[
            ChecklistQuestion(
                id="3a_q1",
                text="Select ALL systems that should be classified as CRITICAL for this mission:",
                options=[
                    ("A", "Mission command applications and battle tracking"),
                    ("B", "SATCOM and tactical radio networks"),
                    ("C", "Recreational internet/MWR systems"),
                    ("D", "Intelligence databases and ISR feeds"),
                    ("E", "Base gym reservation system"),
                    ("F", "Supply tracking and logistics systems"),
                    ("G", "Weapons platform control systems"),
                ],
                correct_answers=["A", "B", "D", "F", "G"],
                feedback_correct="""Correct! Critical systems for combat operations:
- Mission command (A) - Core C2 capability
- Communications (B) - Cannot command without comms
- Intelligence (D) - Situational awareness essential
- Logistics (F) - Troops need supplies
- Weapons systems (G) - Combat capability

Recreational (C) and gym (E) systems are NOT mission critical.""",
                feedback_incorrect="""Critical systems support the MISSION:
- A - Mission command: Core C2 capability
- B - SATCOM/tactical radios: Essential communications
- D - Intelligence: Situational awareness
- F - Logistics: Supply chain visibility
- G - Weapons systems: Combat capability

MWR/recreational and gym systems are nice-to-have, not mission critical.""",
                model_answer="A, B, D, F, G - Systems directly supporting combat operations.",
                points=3
            ),
            RankingQuestion(
                id="3a_q2",
                text="Rank these system categories by criticality (1 = most critical):",
                items=[
                    "Command & Control Systems",
                    "Communications Networks",
                    "Logistics Systems",
                ],
                correct_answer=[1, 2, 3],
                num_ranks=3,
                feedback_correct="""Correct ranking!
1. C2 - The brain of the operation; without it, 5,000 operate without direction
2. Communications - The nervous system; enables C2 but has backup options
3. Logistics - The lifeblood; critical but can sustain short-term loss on stockpiles""",
                feedback_incorrect="""Criticality ranking:
1. COMMAND & CONTROL - The decision-making center; without it, chaos
2. COMMUNICATIONS - Enables C2; multiple backup options exist (radio, satellite, courier)
3. LOGISTICS - Essential for sustained ops but forces have stockpiles for short-term""",
                model_answer="1-C2, 2-Communications, 3-Logistics",
                points=2
            ),
        ]
    )

    # Part B: Dependency Mapping
    scenario_dependencies = Scenario(
        id="3b",
        title="Part B: Dependency Mapping",
        description="""Understanding system dependencies is crucial for predicting cascading failures.
Consider the Command & Control (C2) system for Operation IRON SHIELD.""",
        questions=[
            ChecklistQuestion(
                id="3b_q1",
                text="What does the C2 system DEPEND ON to function? (Select ALL that apply)",
                options=[
                    ("A", "Network connectivity"),
                    ("B", "Reliable power supply"),
                    ("C", "Communications links (SATCOM, tactical)"),
                    ("D", "Trained operators"),
                    ("E", "Intelligence feeds"),
                    ("F", "Gym reservation system"),
                    ("G", "Authentication servers"),
                ],
                correct_answers=["A", "B", "C", "D", "E", "G"],
                feedback_correct="""Correct! C2 system dependencies:
- Network connectivity (A) - Data transport
- Power (B) - Nothing works without power
- Communications (C) - Links to subordinate units
- Trained operators (D) - Someone to run it
- Intelligence feeds (E) - Data to display
- Authentication (G) - Secure access control

Gym reservations (F) have no relationship to C2.""",
                feedback_incorrect="""C2 depends on:
- A - Network: Data transport
- B - Power: Foundation for everything
- C - Communications: Links to field units
- D - Operators: Human operation required
- E - Intelligence: Information to process
- G - Authentication: Access control

The gym system is completely unrelated to C2.""",
                model_answer="A, B, C, D, E, G - Infrastructure, communications, personnel, data, security.",
                points=2
            ),
            ChecklistQuestion(
                id="3b_q2",
                text="What systems/functions DEPEND ON the C2 system? (Select ALL that apply)",
                options=[
                    ("A", "Fire support coordination"),
                    ("B", "Medical evacuation requests"),
                    ("C", "Subordinate unit coordination"),
                    ("D", "Logistics resupply requests"),
                    ("E", "Gym class scheduling"),
                    ("F", "Intelligence dissemination"),
                    ("G", "Personnel accountability"),
                ],
                correct_answers=["A", "B", "C", "D", "F", "G"],
                feedback_correct="""Correct! Functions dependent on C2:
- Fire support (A) - Coordinate artillery, air support
- Medevac (B) - Request and coordinate evacuations
- Unit coordination (C) - Prevent fratricide, sync operations
- Logistics (D) - Request and track supplies
- Intelligence (F) - Disseminate threat info
- Personnel (G) - Track force locations

Gym scheduling (E) does not depend on C2.""",
                feedback_incorrect="""C2 enables these critical functions:
- A - Fire support: Life-saving capability
- B - Medevac: Getting wounded to care
- C - Unit coordination: Preventing fratricide
- D - Logistics: Supply requests
- F - Intelligence: Sharing threat information
- G - Personnel: Tracking the force

Gym scheduling is administrative, not C2-dependent.""",
                model_answer="A, B, C, D, F, G - Combat support, coordination, logistics, intelligence, personnel.",
                points=2
            ),
        ]
    )

    # Part C: Impact Analysis
    scenario_impact = Scenario(
        id="3c",
        title="Part C: Mission Impact Analysis",
        description="""Analyze the impact of compromising different CIA properties for the
Command & Control system during Operation IRON SHIELD.""",
        questions=[
            MultipleChoiceQuestion(
                id="3c_q1",
                text="If CONFIDENTIALITY is compromised (enemy sees your plans), what is the PRIMARY impact?",
                options=[
                    ("A", "System performance degrades"),
                    ("B", "Enemy can predict and counter your operations"),
                    ("C", "Data becomes corrupted"),
                    ("D", "System becomes unavailable"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Confidentiality compromise means the enemy can see your plans:
- They know your operational plans
- They can predict unit movements
- They can prepare ambushes
- You lose the element of surprise
- They can avoid your strength, hit your weakness""",
                feedback_incorrect="""CONFIDENTIALITY = who can READ the data.

If compromised:
- Enemy knows your plans
- Enemy can predict your movements
- Enemy can prepare defenses/ambushes
- You lose tactical surprise

Performance, corruption, and availability are different CIA properties.""",
                model_answer="B - Enemy knows your plans and can counter them.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="3c_q2",
                text="If INTEGRITY is compromised (data can be modified), what is the MOST DANGEROUS impact?",
                options=[
                    ("A", "Reports arrive 30 minutes late"),
                    ("B", "Enemy learns your positions"),
                    ("C", "False orders or positions could cause fratricide"),
                    ("D", "Users need to re-enter passwords"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Integrity compromise = wrong information, which can be deadly:
- False orders could be injected
- Unit positions displayed incorrectly
- Fire support directed at friendlies
- Commanders making decisions on bad data

Wrong information acted upon is worse than no information.""",
                feedback_incorrect="""INTEGRITY = data accuracy and trustworthiness.

If compromised:
- False orders could be injected
- Wrong positions shown = fratricide risk
- Decisions based on corrupted intelligence
- Commanders lose trust in the system

Delays and password issues are different problems.""",
                model_answer="C - False information could cause friendly fire casualties.",
                points=3
            ),
            MultipleChoiceQuestion(
                id="3c_q3",
                text="If AVAILABILITY is compromised (system is down), what is the PRIMARY impact?",
                options=[
                    ("A", "Historical records are lost"),
                    ("B", "Enemy learns classified information"),
                    ("C", "Cannot coordinate forces, request support, or maintain situational awareness"),
                    ("D", "Data integrity is compromised"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Availability loss = system is DOWN:
- Headquarters loses situational awareness
- Cannot issue new orders
- Cannot coordinate between units
- Cannot request fire support or medevac
- Units operate independently = fratricide risk

"A commander who cannot communicate cannot command." """,
                feedback_incorrect="""AVAILABILITY = system is working and accessible.

If unavailable:
- Can't issue orders
- Can't coordinate units
- Can't request fire support
- Can't request medevac
- Units operate blind

Historical records and confidentiality are separate concerns.""",
                model_answer="C - Cannot command or coordinate forces.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="3c_q4",
                text="Which CIA property loss is MOST immediately dangerous for C2?",
                options=[
                    ("A", "Confidentiality - Enemy knows our plans"),
                    ("B", "Integrity - Data may be wrong"),
                    ("C", "Availability - System is down"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Integrity loss is often most immediately dangerous because:
- Wrong information is WORSE than no information
- You might not KNOW the data is wrong
- Could cause fratricide before anyone realizes
- Erodes trust even after discovered

Availability loss is obvious (system down). Confidentiality loss is bad but survivable.
Integrity loss is insidious—you act on false data without knowing.""",
                feedback_incorrect="""Integrity loss is most dangerous because:
- You may NOT KNOW the data is wrong
- Actions based on false data = casualties
- Harder to detect than availability loss
- Could cause fratricide before discovery

Availability loss is OBVIOUS (system down).
Integrity loss is HIDDEN (looks normal but wrong).""",
                model_answer="B - Wrong information acted upon is worse than no information.",
                points=2
            ),
        ]
    )

    # Part D: Cascading Effects
    scenario_cascading = Scenario(
        id="3d",
        title="Part D: Cascading Effects Analysis",
        description="""The logistics tracking system experiences a complete availability loss due to a
ransomware attack. Analyze how this failure cascades through the operation over time.""",
        questions=[
            MultipleChoiceQuestion(
                id="3d_q1",
                text="At 0-4 hours after logistics system failure, what is the PRIMARY impact?",
                options=[
                    ("A", "Mass casualties from supply shortages"),
                    ("B", "Loss of visibility on supply status; fall back to manual processes"),
                    ("C", "Complete mission failure"),
                    ("D", "All vehicles run out of fuel"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! In the first 0-4 hours:
- Loss of real-time supply visibility
- Cannot process automated requests
- Fall back to manual tracking (phone, radio, paper)
- Operations continue on existing stockpiles
- Confusion about what's in stock where

Not yet critical—units have supplies, just lost visibility.""",
                feedback_incorrect="""At 0-4 hours:
- Immediate: Loss of visibility and automation
- Response: Fall back to manual processes
- Impact: Inconvenient but not critical yet
- Units: Operating on existing stockpiles

Mass casualties and mission failure come much later, if at all.""",
                model_answer="B - Loss of visibility; manual workarounds begin.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="3d_q2",
                text="At 12-24 hours after logistics system failure, what becomes the PRIMARY concern?",
                options=[
                    ("A", "Users forget their passwords"),
                    ("B", "Manual processes overwhelmed; potential shortages at some locations"),
                    ("C", "Recreational activities cancelled"),
                    ("D", "Email backlog"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! At 12-24 hours:
- Manual tracking can't keep up with demand
- Some units running low on consumables
- Potential shortages at some locations
- Priority decisions required
- Some operations may need to pause
- Increased risk to personnel safety""",
                feedback_incorrect="""At 12-24 hours, real problems emerge:
- Manual processes overwhelmed
- Units running low on consumables
- Misdirected supplies (no visibility)
- Emergency resupply coordination failing
- Potential for casualties if critical supplies run out

Password and email issues are trivial by comparison.""",
                model_answer="B - Manual processes can't keep up; shortages developing.",
                points=2
            ),
            ChecklistQuestion(
                id="3d_q3",
                text="What actions would help PREVENT or MITIGATE cascading failure? (Select ALL that apply)",
                options=[
                    ("A", "Network segmentation to isolate from attack vectors"),
                    ("B", "Regular offline backups"),
                    ("C", "Hope attackers don't notice"),
                    ("D", "Documented manual procedures (tested regularly)"),
                    ("E", "Emergency supply stockpiles at each location"),
                    ("F", "Cross-train personnel on manual processes"),
                ],
                correct_answers=["A", "B", "D", "E", "F"],
                feedback_correct="""Correct! Prevention and mitigation measures:
- Segmentation (A) - Limits attack spread
- Offline backups (B) - Enable recovery
- Manual procedures (D) - Tested workarounds
- Stockpiles (E) - Buffer against shortages
- Cross-training (F) - Personnel can adapt

"Hope" (C) is not a strategy.""",
                feedback_incorrect="""Effective prevention and mitigation:
- A - Segmentation: Isolate from attack vectors
- B - Backups: Enable rapid recovery
- D - Manual procedures: Tested alternatives
- E - Stockpiles: Buy time during outages
- F - Cross-training: Flexible workforce

Hope is never a security strategy.""",
                model_answer="A, B, D, E, F - Segmentation, backups, procedures, stockpiles, training.",
                points=3
            ),
        ]
    )

    # Part E: Prioritization
    scenario_priority = Scenario(
        id="3e",
        title="Part E: Protection Prioritization",
        description="""Based on your analysis, you must recommend protection priorities to the commander.
Resources are limited, and you can only fully protect a subset of systems.""",
        questions=[
            RankingQuestion(
                id="3e_q1",
                text="Rank these systems for protection priority (1 = highest priority):",
                items=[
                    "Command & Control Systems",
                    "Communications Networks",
                    "Logistics Tracking Systems",
                ],
                correct_answer=[1, 2, 3],
                num_ranks=3,
                feedback_correct="""Correct! Prioritization logic:
1. C2 - The brain; without it, can't coordinate 5,000 personnel
2. Communications - Enables C2; multiple backup options exist
3. Logistics - Can sustain short-term with stockpiles""",
                feedback_incorrect="""Protection priority:
1. COMMAND & CONTROL - Cannot coordinate without it
2. COMMUNICATIONS - Enables C2, but has backups (radio, satellite)
3. LOGISTICS - Can operate short-term on existing supplies

You can survive without logistics visibility for hours;
you cannot command effectively without C2.""",
                model_answer="1-C2, 2-Communications, 3-Logistics",
                points=2
            ),
            MultipleChoiceQuestion(
                id="3e_q2",
                text="If you could only fully protect ONE system, which should you choose?",
                options=[
                    ("A", "Command & Control"),
                    ("B", "Communications"),
                    ("C", "Logistics"),
                    ("D", "Recreational/MWR"),
                ],
                correct_answer="A",
                feedback_correct="""Correct! C2 is the priority because:
- It's the "brain" of the operation
- Enables coordination of 5,000 personnel
- All other systems SUPPORT the C2 function
- Communications exist TO ENABLE C2
- Logistics exists to support the force C2 directs

Without C2, you have 5,000 people acting independently.""",
                feedback_incorrect="""Command & Control is the priority because:
- It's the decision-making center
- All other systems support C2
- Without C2 = chaos with 5,000 personnel
- Communications enables C2 but has backups
- Logistics supports the force C2 directs

"Protect the brain first—everything else supports it." """,
                model_answer="A - C2 is the brain; everything else supports it.",
                points=2
            ),
        ]
    )

    # Create the exercise
    exercise = Exercise(
        id="exercise3",
        number=3,
        title="Mission Impact Analysis",
        description="""This exercise develops your ability to analyze how cyber incidents impact military
operations. You will identify critical systems, map dependencies, and assess the operational
consequences of CIA property compromises in a realistic deployed scenario.""",
        estimated_time="45-60 minutes",
        objectives=[
            "Identify critical information systems for military operations",
            "Map system dependencies and single points of failure",
            "Analyze cascading failure scenarios",
            "Prioritize protection efforts based on mission criticality",
        ],
        scenarios=[
            scenario_systems,
            scenario_dependencies,
            scenario_impact,
            scenario_cascading,
            scenario_priority
        ]
    )

    return exercise
