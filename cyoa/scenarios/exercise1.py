"""Exercise 1: CIA Triad Analysis scenarios."""

from .base import (
    Exercise,
    Scenario,
    MultipleChoiceQuestion,
    RankingQuestion,
    ChecklistQuestion,
)


def get_exercise() -> Exercise:
    """Create and return Exercise 1."""

    # Scenario 1A: Intelligence Database
    scenario_1a = Scenario(
        id="1a",
        title="Scenario 1A: Intelligence Database",
        description="""An intelligence database contains information about enemy force positions,
capabilities, and intentions. The database is accessed by analysts at multiple locations
worldwide via classified networks. Analysts use this information to brief commanders and
develop operational recommendations.""",
        questions=[
            MultipleChoiceQuestion(
                id="1a_q1",
                text="Which CIA property is MOST critical for this system?",
                options=[
                    ("C", "Confidentiality"),
                    ("I", "Integrity"),
                    ("A", "Availability"),
                ],
                correct_answer="C",
                feedback_correct="""Confidentiality is most critical for an intelligence database.
If disclosed to adversaries, this information could compromise operations, endanger personnel,
and provide strategic advantage to enemies. The "need to know" principle is fundamental.""",
                feedback_incorrect="""Consider the nature of intelligence data. This database contains
CLASSIFIED information about enemy positions and capabilities. While integrity and availability
matter, the classified nature makes CONFIDENTIALITY paramount. Disclosure could cost lives.""",
                model_answer="Confidentiality - Intelligence data disclosure could compromise operations and endanger personnel.",
                points=2
            ),
            ChecklistQuestion(
                id="1a_q2",
                text="Which of the following are significant threats to this system? (Select ALL that apply)",
                options=[
                    ("A", "Nation-state espionage (APT groups)"),
                    ("B", "Insider threats with legitimate access"),
                    ("C", "Random malware infections"),
                    ("D", "Credential theft via spear-phishing"),
                    ("E", "DDoS attacks from hacktivists"),
                    ("F", "Supply chain compromise"),
                ],
                correct_answers=["A", "B", "D", "F"],
                feedback_correct="""Correct! The primary threats to intelligence systems are:
- Nation-state APTs seeking classified intelligence
- Insider threats who have legitimate access
- Spear-phishing targeting analyst credentials
- Supply chain attacks on intelligence infrastructure

DDoS and random malware are less targeted threats for this high-value system.""",
                feedback_incorrect="""Key threats to intelligence databases are TARGETED attacks:
- Nation-state espionage (A) - Primary threat to classified systems
- Insider threats (B) - Those with access who misuse it
- Spear-phishing (D) - Targeted credential theft
- Supply chain (F) - Compromised hardware/software

Random malware (C) and DDoS (E) are less relevant for high-value targeted systems.""",
                model_answer="A, B, D, F - Targeted threats from sophisticated actors seeking classified information.",
                points=3
            ),
            ChecklistQuestion(
                id="1a_q3",
                text="Which controls would BEST protect this system's confidentiality? (Select ALL that apply)",
                options=[
                    ("A", "Strong encryption at rest and in transit"),
                    ("B", "Multi-factor authentication"),
                    ("C", "Strict need-to-know access controls"),
                    ("D", "Load balancing for performance"),
                    ("E", "Comprehensive audit logging"),
                    ("F", "Automated backup systems"),
                ],
                correct_answers=["A", "B", "C", "E"],
                feedback_correct="""Correct! Confidentiality controls include:
- Encryption (A) - Protects data even if intercepted
- MFA (B) - Prevents unauthorized access via stolen credentials
- Need-to-know access (C) - Limits exposure
- Audit logging (E) - Detects unauthorized access attempts

Load balancing (D) addresses availability; backups (F) address availability/integrity.""",
                feedback_incorrect="""For CONFIDENTIALITY, focus on who can access and read the data:
- Encryption (A) - Protects data content
- MFA (B) - Verifies identity
- Need-to-know (C) - Limits access
- Audit logging (E) - Detects breaches

Load balancing and backups address availability, not confidentiality.""",
                model_answer="A, B, C, E - Controls that protect who can access and read the data.",
                points=3
            ),
            MultipleChoiceQuestion(
                id="1a_q4",
                text="What is the PRIMARY trade-off when maximizing confidentiality for this system?",
                options=[
                    ("A", "Increased hardware costs"),
                    ("B", "Reduced availability - slower access for analysts who need urgent intelligence"),
                    ("C", "Lower data integrity"),
                    ("D", "Reduced network bandwidth"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Maximizing confidentiality often reduces availability:
- Strict access controls slow down analyst access
- Multiple authentication steps add latency
- Need-to-know restrictions may prevent information sharing
- Time-sensitive intelligence may be delayed to those who need it""",
                feedback_incorrect="""The main trade-off is between CONFIDENTIALITY and AVAILABILITY:
- Strict access controls slow down access
- Multiple authentication steps add time
- Need-to-know compartmentalization may delay information sharing
- Security procedures take time that urgent situations may not have""",
                model_answer="B - Strict security controls slow access to time-sensitive intelligence.",
                points=2
            ),
        ]
    )

    # Scenario 1B: Logistics System
    scenario_1b = Scenario(
        id="1b",
        title="Scenario 1B: Logistics System During Combat Operations",
        description="""A logistics tracking system manages ammunition, fuel, food, and medical supplies
for forward-deployed forces during active combat operations. The system tracks inventory levels,
shipment status, and delivery schedules. Supply requests and allocations are processed through
this system.""",
        questions=[
            MultipleChoiceQuestion(
                id="1b_q1",
                text="Which CIA property is MOST critical during active combat?",
                options=[
                    ("C", "Confidentiality"),
                    ("I", "Integrity"),
                    ("A", "Availability"),
                ],
                correct_answer="A",
                feedback_correct="""Availability is most critical during combat operations.
Forces need supplies (ammunition, fuel, medical) regardless of whether the enemy knows
what's being shipped. If the system is down, units can't request resupply and commanders
lose visibility. Lives depend on supplies arriving when needed.""",
                feedback_incorrect="""In active combat, what matters most is that the system WORKS.
- Troops need ammunition, fuel, food, medical supplies NOW
- A secure but unavailable system doesn't help anyone
- The enemy knowing your supply schedule is less critical than having no supplies
- Availability is paramount; you can work around confidentiality issues.""",
                model_answer="Availability - Troops need supplies NOW; a down system could cost lives.",
                points=2
            ),
            RankingQuestion(
                id="1b_q2",
                text="Rank the CIA properties for a logistics system DURING COMBAT (1 = highest priority):",
                items=[
                    "Confidentiality",
                    "Integrity",
                    "Availability",
                ],
                correct_answer=[3, 2, 1],
                num_ranks=3,
                feedback_correct="""Correct! During combat:
1. Availability - Troops need supplies NOW
2. Integrity - Supplies must go to the right place
3. Confidentiality - Enemy knowing shipments is less critical than troops having supplies""",
                feedback_incorrect="""During combat operations:
1. AVAILABILITY - Without supplies, troops cannot fight
2. INTEGRITY - Wrong locations or quantities cause problems
3. CONFIDENTIALITY - Less critical; enemy knowing logistics is bad but survivable""",
                model_answer="1-Availability, 2-Integrity, 3-Confidentiality",
                points=2
            ),
            MultipleChoiceQuestion(
                id="1b_q3",
                text="An adversary compromises the INTEGRITY of the logistics system. What is the MOST dangerous consequence?",
                options=[
                    ("A", "Supply costs are reported incorrectly"),
                    ("B", "Ammunition and medical supplies are misdirected to wrong locations"),
                    ("C", "Historical supply data is corrupted"),
                    ("D", "Supply reports are delayed by 30 minutes"),
                ],
                correct_answer="B",
                feedback_correct="""Misdirected supplies is the most dangerous consequence.
If ammunition goes to the wrong unit, frontline troops may be left defenseless.
If medical supplies are misdirected, wounded personnel may not receive treatment.
This could directly result in casualties.""",
                feedback_incorrect="""Integrity compromise means DATA IS WRONG. The most dangerous outcome is:
- Supplies sent to wrong locations = units without critical resources
- Frontline troops without ammunition = defenseless
- Medical supplies misdirected = preventable casualties

Incorrect costs or delayed reports are inconvenient but not life-threatening.""",
                model_answer="B - Misdirected supplies leave troops without critical resources.",
                points=3
            ),
        ]
    )

    # Scenario 1C: Command and Control Network
    scenario_1c = Scenario(
        id="1c",
        title="Scenario 1C: Command and Control Network",
        description="""A command and control (C2) network enables real-time communication between a
headquarters and subordinate units executing combat operations. The network carries operational
orders, situation reports, requests for fire support, and coordination messages.""",
        questions=[
            RankingQuestion(
                id="1c_q1",
                text="Rank the CIA properties for a C2 network during operations (1 = highest priority):",
                items=[
                    "Confidentiality",
                    "Integrity",
                    "Availability",
                ],
                correct_answer=[3, 2, 1],
                num_ranks=3,
                feedback_correct="""Correct! For C2 networks:
1. Availability - Can't command without communications
2. Integrity - Orders must be accurate to prevent fratricide
3. Confidentiality - Important but secondary to ability to communicate

"A commander who cannot communicate cannot command." """,
                feedback_incorrect="""For Command and Control networks:
1. AVAILABILITY - Without communications, you cannot command forces
2. INTEGRITY - Orders must be accurate; corrupted orders cause fratricide
3. CONFIDENTIALITY - Important, but the ability to communicate takes priority""",
                model_answer="1-Availability, 2-Integrity, 3-Confidentiality",
                points=2
            ),
            ChecklistQuestion(
                id="1c_q2",
                text="What happens if C2 availability is lost during active operations? (Select ALL that apply)",
                options=[
                    ("A", "Units operate without current orders"),
                    ("B", "Cannot coordinate between friendly units"),
                    ("C", "Cannot request fire support or medevac"),
                    ("D", "Historical records are lost"),
                    ("E", "Risk of fratricide increases"),
                    ("F", "Office email is unavailable"),
                ],
                correct_answers=["A", "B", "C", "E"],
                feedback_correct="""Correct! Without C2 communications:
- Units follow last known orders (A)
- Cannot coordinate (B) - units act independently
- Cannot request support (C) - no fire support, no medevac
- Fratricide risk increases (E) - without coordination

Historical records (D) and office email (F) are not immediate operational concerns.""",
                feedback_incorrect="""Loss of C2 availability has immediate operational consequences:
- A - Units operate on last guidance without updates
- B - Cannot coordinate between units
- C - Cannot request fire support or medical evacuation
- E - Without coordination, friendly fire risk increases

Records and office email are not the concern during active operations.""",
                model_answer="A, B, C, E - Immediate operational consequences affecting lives.",
                points=3
            ),
            ChecklistQuestion(
                id="1c_q3",
                text="Which controls protect ALL THREE CIA properties simultaneously? (Select ALL that apply)",
                options=[
                    ("A", "Redundant encrypted communication paths"),
                    ("B", "Digitally signed messages with multiple delivery routes"),
                    ("C", "Firewall rules"),
                    ("D", "Password complexity requirements"),
                    ("E", "Mesh networks with authentication"),
                ],
                correct_answers=["A", "B", "E"],
                feedback_correct="""Correct! These controls address all three CIA properties:

Redundant encrypted comms (A):
- Confidentiality: Encryption
- Integrity: Encryption includes integrity checks
- Availability: Redundancy ensures alternate paths

Signed messages with multiple routes (B):
- Confidentiality: Can be combined with encryption
- Integrity: Digital signatures verify authenticity
- Availability: Multiple routes ensure delivery

Mesh networks with auth (E):
- Confidentiality: Authentication controls access
- Integrity: Authentication verifies sources
- Availability: Mesh topology provides redundancy""",
                feedback_incorrect="""Look for controls that address Confidentiality AND Integrity AND Availability:

- Redundant encrypted paths (A) - Yes: encryption + redundancy
- Signed messages, multiple routes (B) - Yes: signatures + redundancy
- Mesh networks with auth (E) - Yes: auth + mesh redundancy

Firewalls (C) and passwords (D) don't inherently provide all three.""",
                model_answer="A, B, E - Controls combining encryption/authentication with redundancy.",
                points=3
            ),
        ]
    )

    # Create the exercise
    exercise = Exercise(
        id="exercise1",
        number=1,
        title="CIA Triad Analysis",
        description="""This exercise reinforces your understanding of the CIA Triad—Confidentiality,
Integrity, and Availability—by applying these principles to DoD scenarios. You will analyze
different mission contexts and determine which security properties are most critical.""",
        estimated_time="30-40 minutes",
        objectives=[
            "Apply CIA Triad principles to analyze DoD system security requirements",
            "Understand how mission context affects security priorities",
            "Identify appropriate controls for different scenarios",
            "Recognize trade-offs between CIA properties",
        ],
        scenarios=[scenario_1a, scenario_1b, scenario_1c]
    )

    return exercise
