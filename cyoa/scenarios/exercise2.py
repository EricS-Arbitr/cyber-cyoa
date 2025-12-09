"""Exercise 2: Threat Actor Analysis scenarios."""

from .base import (
    Exercise,
    Scenario,
    MultipleChoiceQuestion,
    RankingQuestion,
    ChecklistQuestion,
)


def get_exercise() -> Exercise:
    """Create and return Exercise 2."""

    # Part A: Threat Actor Profiling
    scenario_profiling = Scenario(
        id="2a",
        title="Part A: Threat Actor Profiling",
        description="""In this section, you will analyze different types of threat actors that target
DoD systems. Understanding threat actor motivations, capabilities, and methods is essential for
effective cyber defense.""",
        questions=[
            MultipleChoiceQuestion(
                id="2a_q1",
                text="What is the PRIMARY motivation of a nation-state APT group like APT28 (Fancy Bear)?",
                options=[
                    ("A", "Financial gain through ransomware"),
                    ("B", "Strategic intelligence and geopolitical advantage"),
                    ("C", "Notoriety and public recognition"),
                    ("D", "Disruption for ideological reasons"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Nation-state APT groups are primarily motivated by
strategic intelligence gathering and geopolitical advantage. They conduct espionage operations
to benefit their sponsoring government's political, military, and economic interests.""",
                feedback_incorrect="""Nation-state APT groups like APT28 are sponsored by governments
(in this case, Russia's GRU military intelligence). Their primary motivation is:
- Strategic intelligence gathering
- Geopolitical advantage for their nation
- Supporting military and political objectives

Unlike criminals (financial), hacktivists (ideology), or script kiddies (notoriety).""",
                model_answer="B - Strategic intelligence and geopolitical advantage for the sponsoring nation.",
                points=2
            ),
            ChecklistQuestion(
                id="2a_q2",
                text="Which are typical capabilities/TTPs of nation-state APT groups? (Select ALL that apply)",
                options=[
                    ("A", "Custom malware development"),
                    ("B", "Zero-day exploit acquisition"),
                    ("C", "Quick smash-and-grab attacks"),
                    ("D", "Long-term persistent access (months/years)"),
                    ("E", "Commodity malware from dark web"),
                    ("F", "Advanced spear-phishing campaigns"),
                    ("G", "Noisy, attention-seeking attacks"),
                ],
                correct_answers=["A", "B", "D", "F"],
                feedback_correct="""Correct! Nation-state APT characteristics:
- Custom malware (A) - Not commodity tools
- Zero-days (B) - Significant resources for exploit development
- Long-term access (D) - APT = Advanced PERSISTENT Threat
- Targeted spear-phishing (F) - Carefully crafted for specific targets

They avoid noisy tactics (G) and commodity malware (E); smash-and-grab (C) is for criminals.""",
                feedback_incorrect="""Nation-state APTs are characterized by sophistication and patience:
- A - Custom malware (not commodity)
- B - Zero-day exploits (expensive but available to nation-states)
- D - Long-term persistence (months to years of access)
- F - Targeted spear-phishing (not spray-and-pray)

Quick attacks, commodity malware, and noisy behavior are criminal characteristics.""",
                model_answer="A, B, D, F - Sophisticated, patient, custom tools, targeted attacks.",
                points=3
            ),
            MultipleChoiceQuestion(
                id="2a_q3",
                text="What is the PRIMARY motivation of a ransomware group like LockBit?",
                options=[
                    ("A", "Strategic intelligence gathering"),
                    ("B", "Political or ideological messaging"),
                    ("C", "Financial profit through extortion"),
                    ("D", "Destruction of critical infrastructure"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Ransomware groups are financially motivated. They encrypt
victim data and demand payment (usually cryptocurrency) for the decryption key. Many also use
"double extortion" - threatening to leak stolen data for additional leverage.""",
                feedback_incorrect="""Criminal ransomware groups like LockBit are purely financially motivated:
- They want money, not intelligence or ideology
- They use ransomware to extort payment
- Many use "double extortion" (encrypt + threaten to leak)
- They operate as businesses (Ransomware-as-a-Service)""",
                model_answer="C - Financial profit through extortion.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="2a_q4",
                text="How do criminal organization attacks DIFFER from nation-state attacks?",
                options=[
                    ("A", "Criminals are more patient and use custom tools"),
                    ("B", "Criminals are faster, noisier, and more opportunistic"),
                    ("C", "Criminals focus on long-term intelligence gathering"),
                    ("D", "Criminals always use zero-day exploits"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Criminal organizations differ from nation-states:
- MORE opportunistic (spray and pray vs targeted)
- FASTER timeline (days/weeks vs months/years)
- NOISIER (less concerned about detection)
- Use COMMODITY malware (cost-effective)
- Focus on QUICK monetization""",
                feedback_incorrect="""Criminal vs nation-state approach:

Criminals:
- Opportunistic targeting
- Fast timeline (days to weeks)
- Noisy, less concerned about stealth
- Commodity malware, RaaS
- Quick monetization

Nation-states are the opposite: patient, targeted, stealthy, custom tools.""",
                model_answer="B - Criminals are faster, noisier, and more opportunistic.",
                points=2
            ),
        ]
    )

    # Part B: Target Analysis
    scenario_target = Scenario(
        id="2b",
        title="Part B: Target Analysis - DoD Personnel Management System",
        description="""Target System: DoD Personnel Management System

This system contains service records, performance evaluations, security clearance status,
assignment history, and contact information for all military personnel. It is accessible
from multiple DoD installations.

Analyze how different threat actors would approach this target.""",
        questions=[
            ChecklistQuestion(
                id="2b_q1",
                text="Why would a NATION-STATE be attracted to this personnel system? (Select ALL that apply)",
                options=[
                    ("A", "Identify intelligence personnel for targeting"),
                    ("B", "Mine cryptocurrency using the servers"),
                    ("C", "Security clearance data reveals who has access to secrets"),
                    ("D", "Personal information enables blackmail/coercion"),
                    ("E", "Sell Social Security numbers on dark web"),
                    ("F", "Support recruitment of potential assets/spies"),
                ],
                correct_answers=["A", "C", "D", "F"],
                feedback_correct="""Correct! Nation-states target personnel systems for intelligence purposes:
- Identify intelligence personnel (A) - Who to target for espionage
- Clearance data (C) - Who has access to what secrets
- Personal info for blackmail (D) - Leverage for recruitment/coercion
- Asset recruitment (F) - Identify potential spies

Cryptocurrency mining (B) and selling SSNs (E) are criminal motivations.""",
                feedback_incorrect="""Nation-states want INTELLIGENCE VALUE, not money:
- A - Identify intelligence personnel to target
- C - Clearance data shows who has access to secrets
- D - Personal information for blackmail/coercion
- F - Identify candidates for recruitment as assets

Cryptocurrency and selling data are criminal (profit) motivations, not nation-state.""",
                model_answer="A, C, D, F - Intelligence value: targeting, clearances, blackmail, recruitment.",
                points=3
            ),
            ChecklistQuestion(
                id="2b_q2",
                text="What attack vectors would a nation-state APT likely use against this system? (Select ALL that apply)",
                options=[
                    ("A", "Spear-phishing targeting system administrators"),
                    ("B", "Mass spam emails to all employees"),
                    ("C", "Watering hole attacks on HR-related websites"),
                    ("D", "Supply chain compromise of connected systems"),
                    ("E", "Publicly announcing the attack on social media"),
                    ("F", "Compromising contractors with system access"),
                ],
                correct_answers=["A", "C", "D", "F"],
                feedback_correct="""Correct! APT attack vectors are targeted and stealthy:
- Spear-phishing admins (A) - Target those with access
- Watering holes (C) - Compromise sites HR staff visit
- Supply chain (D) - Target vendors/software
- Contractor compromise (F) - Third-party access

Mass spam (B) is untargeted; announcing attacks (E) is opposite of APT stealth.""",
                feedback_incorrect="""APT attack vectors are TARGETED and STEALTHY:
- A - Spear-phishing administrators (targeted)
- C - Watering hole attacks (specific to HR industry)
- D - Supply chain compromise (sophisticated)
- F - Contractor compromise (trusted third parties)

Mass spam is untargeted; public announcements defeat stealth.""",
                model_answer="A, C, D, F - Targeted, stealthy vectors against high-value targets.",
                points=3
            ),
            RankingQuestion(
                id="2b_q3",
                text="Rank these Cyber Kill Chain phases by when they occur (1 = first):",
                items=[
                    "Actions on Objectives (data exfiltration)",
                    "Delivery (phishing email sent)",
                    "Reconnaissance (researching targets)",
                ],
                correct_answer=[3, 2, 1],
                num_ranks=3,
                feedback_correct="""Correct! The Cyber Kill Chain order:
1. Reconnaissance - Research targets, gather info
2. Delivery - Send the phishing email/exploit
3. Actions on Objectives - Final goal (exfiltration)

(Weaponization, Exploitation, Installation, and C2 occur between Delivery and Actions)""",
                feedback_incorrect="""The Cyber Kill Chain sequence:
1. RECONNAISSANCE - Research comes first
2. DELIVERY - Send the attack
3. ACTIONS ON OBJECTIVES - The final goal

You must research before attacking, and attack before achieving your objective.""",
                model_answer="1-Reconnaissance, 2-Delivery, 3-Actions on Objectives",
                points=2
            ),
            MultipleChoiceQuestion(
                id="2b_q4",
                text="Why might CRIMINALS also target this system, and how would their approach differ?",
                options=[
                    ("A", "Same motivation and methods as nation-states"),
                    ("B", "Identity theft/fraud - faster, noisier, quick monetization"),
                    ("C", "Criminals would not be interested in this system"),
                    ("D", "Long-term persistent access for intelligence"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Criminals would target for different reasons:
- Identity theft using PII
- Sell data on dark web
- Ransomware extortion (high-profile target)

Different approach:
- More opportunistic
- Faster timeline
- Less sophisticated
- Quick monetization priority""",
                feedback_incorrect="""Criminals have different motivations and methods:
- MOTIVATION: Identity theft, fraud, ransom (money)
- APPROACH: Faster, noisier, more opportunistic
- GOAL: Quick monetization

Unlike nation-states who want long-term intelligence access.""",
                model_answer="B - Identity theft and fraud with faster, noisier approach.",
                points=2
            ),
        ]
    )

    # Part C: Defense Recommendations
    scenario_defense = Scenario(
        id="2c",
        title="Part C: Defense Recommendations",
        description="""Based on your threat analysis, provide defensive recommendations to protect
the DoD Personnel Management System from both nation-state and criminal threats.""",
        questions=[
            ChecklistQuestion(
                id="2c_q1",
                text="Select the TOP 5 most effective defensive priorities:",
                options=[
                    ("A", "Multi-factor authentication (MFA)"),
                    ("B", "Annual security awareness briefing"),
                    ("C", "Network segmentation"),
                    ("D", "Endpoint detection and response (EDR)"),
                    ("E", "Privileged access management (PAM)"),
                    ("F", "Phishing-focused user training"),
                    ("G", "Decorative security posters"),
                ],
                correct_answers=["A", "C", "D", "E", "F"],
                feedback_correct="""Correct! Top defensive priorities:
- MFA (A) - Stops credential theft exploitation
- Network segmentation (C) - Limits lateral movement
- EDR (D) - Detects malware and anomalous behavior
- PAM (E) - Limits credential theft impact
- Phishing training (F) - Reduces initial access success

Annual briefings (B) are less effective than focused training; posters (G) are decorative.""",
                feedback_incorrect="""Effective defenses address the attack vectors:
- A - MFA prevents credential theft exploitation
- C - Segmentation limits lateral movement
- D - EDR detects malware and anomalies
- E - PAM limits privileged access abuse
- F - Phishing training reduces initial access

Annual briefings are less effective than targeted training; posters don't stop attackers.""",
                model_answer="A, C, D, E, F - MFA, segmentation, EDR, PAM, phishing training.",
                points=3
            ),
            MultipleChoiceQuestion(
                id="2c_q2",
                text="Which detection capability is MOST important for identifying nation-state APT activity?",
                options=[
                    ("A", "Antivirus signature matching"),
                    ("B", "User and entity behavior analytics (UEBA)"),
                    ("C", "Daily vulnerability scans"),
                    ("D", "Firewall logs only"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! UEBA is most important for APT detection because:
- APTs use custom malware (no signatures)
- APTs are low and slow (blend in)
- Behavioral analysis detects anomalies
- Can identify compromised legitimate accounts

Signature-based AV misses custom malware; vuln scans and firewalls don't detect active intrusions.""",
                feedback_incorrect="""For APT detection, behavioral analysis is key:
- APTs use CUSTOM malware - no signatures exist
- APTs are LOW AND SLOW - they blend into normal traffic
- UEBA detects anomalies in user behavior
- Catches compromised accounts acting abnormally

Signatures miss custom malware; scans find vulnerabilities, not active attacks.""",
                model_answer="B - UEBA detects behavioral anomalies that signature-based tools miss.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="2c_q3",
                text="Which detection is MOST effective against ransomware attacks?",
                options=[
                    ("A", "Detecting mass file encryption behavior"),
                    ("B", "Annual penetration testing"),
                    ("C", "Monthly vulnerability reports"),
                    ("D", "Checking password complexity"),
                ],
                correct_answer="A",
                feedback_correct="""Correct! Detecting mass file encryption is critical for ransomware:
- Ransomware encrypts many files rapidly
- Behavioral detection catches this pattern
- Allows response before full encryption
- EDR tools can detect and stop encryption in progress

Penetration tests and vuln scans happen too infrequently; passwords don't stop ransomware.""",
                feedback_incorrect="""Ransomware detection requires real-time behavioral monitoring:
- Mass file encryption is the ransomware signature
- Behavioral detection catches this pattern immediately
- Allows incident response before complete encryption

Periodic testing and scans are too slow; password policies don't prevent ransomware.""",
                model_answer="A - Real-time detection of mass file encryption behavior.",
                points=2
            ),
        ]
    )

    # Create the exercise
    exercise = Exercise(
        id="exercise2",
        number=2,
        title="Threat Actor Analysis",
        description="""This exercise develops your ability to analyze different threat actors, understand
their motivations and capabilities, and recommend appropriate defenses. You will profile
nation-state APT groups and criminal organizations, then apply that analysis to defend
a realistic DoD system.""",
        estimated_time="45-60 minutes",
        objectives=[
            "Profile threat actor capabilities, motivations, and methods",
            "Distinguish between nation-state and criminal threat actors",
            "Understand the Cyber Kill Chain",
            "Recommend defensive measures based on threat analysis",
        ],
        scenarios=[scenario_profiling, scenario_target, scenario_defense]
    )

    return exercise
