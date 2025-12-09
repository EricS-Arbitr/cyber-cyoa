"""Exercise 5: Comprehensive Scenario Assessment."""

from .base import (
    Exercise,
    Scenario,
    MultipleChoiceQuestion,
    RankingQuestion,
    ChecklistQuestion,
)


def get_exercise() -> Exercise:
    """Create and return Exercise 5."""

    # Part A: Initial Assessment
    scenario_initial = Scenario(
        id="5a",
        title="Part A: Initial Assessment",
        description="""Forward Operating Base (FOB) PHOENIX Incident

You are the Cyber Defense Infrastructure Support Specialist at FOB PHOENIX, supporting
a brigade combat team. The FOB relies on the following systems:

• Tactical Operations Center (TOC) Network: Classified C2 systems, intelligence feeds,
  common operational picture
• Administrative Network: Email, personnel systems, logistics applications
• Base Life Support Systems: Physical security cameras, access control, environmental controls
• SATCOM Links: Primary communications to higher headquarters
• Tactical Radio Network: Communications with subordinate units in the field

INCIDENT (0300 hours):
• Unusual outbound traffic from the administrative network to an unknown external IP
• Several failed login attempts on the TOC network from an administrative network workstation
• A phishing email was reported 48 hours ago—the user clicked the link before reporting
• Base physical security system shows intermittent camera failures
• SATCOM performance is degraded by 40%

Analyze this situation using all concepts from Module 1.""",
        questions=[
            MultipleChoiceQuestion(
                id="5a_q1",
                text="Based on the indicators, what type of threat actor is MOST likely involved?",
                options=[
                    ("A", "Script kiddie testing tools"),
                    ("B", "Hacktivist making a statement"),
                    ("C", "Nation-state or sophisticated adversary"),
                    ("D", "Disgruntled insider acting alone"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! The indicators suggest a sophisticated adversary:

• Patient approach (48 hours since phishing)
• Multiple vectors (admin network, attempting TOC access)
• Targeting military installation
• C2 traffic to external IP (exfiltration or command channel)
• Possible multi-stage attack

Script kiddies would be noisier; hacktivists would claim credit;
insider alone wouldn't need phishing.""",
                feedback_incorrect="""The indicators suggest a sophisticated adversary:

Why nation-state/sophisticated:
• Patient timeline (48 hours since initial compromise)
• Multiple attack vectors active simultaneously
• Targeting a military installation
• Attempting lateral movement to classified network
• Possible C2 channel established

Script kiddies are noisy and random. Hacktivists want publicity.
A lone insider wouldn't need to phish their own organization.""",
                model_answer="C - Nation-state or sophisticated adversary based on patience, multiple vectors, and targeting.",
                points=2
            ),
            ChecklistQuestion(
                id="5a_q2",
                text="Which Cyber Kill Chain phases have evidence of COMPLETION in this incident? (Select all with clear evidence)",
                options=[
                    ("A", "Reconnaissance - Research and target identification"),
                    ("B", "Weaponization - Creating malicious payload"),
                    ("C", "Delivery - Phishing email sent"),
                    ("D", "Exploitation - Payload executed (user clicked link)"),
                    ("E", "Installation - Malware persistence established"),
                    ("F", "Command & Control - Communication with external IP"),
                    ("G", "Actions on Objectives - Mission goal achieved"),
                ],
                correct_answers=["C", "D", "E", "F"],
                feedback_correct="""Correct! Evidence shows these phases completed:

• Delivery (C): Phishing email was sent and received
• Exploitation (D): User clicked the link—payload executed
• Installation (E): 48-hour gap + C2 traffic indicates persistence
• Command & Control (F): Outbound traffic to unknown external IP

Reconnaissance/Weaponization happened but we have no direct evidence.
Actions on Objectives—unknown if they've achieved their goal yet.
The failed TOC logins suggest they're still trying to expand access.""",
                feedback_incorrect="""Kill Chain phases with EVIDENCE of completion:

CONFIRMED:
• Delivery (C) - Phishing email was sent
• Exploitation (D) - User clicked link, payload executed
• Installation (E) - 48 hours later, still active = persistence
• Command & Control (F) - Outbound traffic to external IP

NO DIRECT EVIDENCE:
• Reconnaissance (A) - Happened but not observed
• Weaponization (B) - Happened but not observed
• Actions on Objectives (G) - Unknown if achieved yet

The attacker is in the C2/lateral movement phase, attempting to reach TOC.""",
                model_answer="C, D, E, F - Delivery through C2 phases have clear evidence.",
                points=3
            ),
            ChecklistQuestion(
                id="5a_q3",
                text="Which systems have CONFIRMED or SUSPECTED compromise? (Select all with evidence of compromise)",
                options=[
                    ("A", "Administrative Network - CONFIRMED"),
                    ("B", "TOC Network - CONFIRMED"),
                    ("C", "Administrative Network - SUSPECTED"),
                    ("D", "TOC Network - SUSPECTED"),
                    ("E", "Base Life Support - SUSPECTED"),
                    ("F", "SATCOM - SUSPECTED"),
                    ("G", "Tactical Radios - CONFIRMED"),
                ],
                correct_answers=["A", "D", "E", "F"],
                feedback_correct="""Correct assessment:

CONFIRMED:
• Admin Network: Outbound C2 traffic, source of TOC login attempts

SUSPECTED (but not confirmed):
• TOC Network: Failed logins suggest targeting, not successful compromise
• Base Life Support: Camera failures could be related or coincidental
• SATCOM: Degradation could be attack or separate issue

NOT compromised:
• Tactical Radios: No indicators of compromise mentioned""",
                feedback_incorrect="""Compromise assessment:

CONFIRMED compromise:
• Administrative Network: C2 traffic + source of login attempts proves compromise

SUSPECTED (evidence but not confirmed):
• TOC Network: Failed logins mean targeting, not successful access
• Base Life Support: Camera failures—possibly related
• SATCOM: Degradation—possibly related

No evidence of compromise:
• Tactical Radios: No indicators mentioned

Key distinction: Failed logins mean the TOC is being TARGETED,
not that it's been COMPROMISED. Evidence matters.""",
                model_answer="A, D, E, F - Admin confirmed, others suspected based on indicators.",
                points=3
            ),
        ]
    )

    # Part B: Mission Impact
    scenario_mission = Scenario(
        id="5b",
        title="Part B: Mission Impact Analysis",
        description="""The brigade has units conducting a patrol 50km from the FOB. You must assess
how this incident affects their safety and the mission.

Consider the current operations and what systems they depend on.""",
        questions=[
            ChecklistQuestion(
                id="5b_q1",
                text="How does this incident affect the patrol? (Select ALL impacts that apply)",
                options=[
                    ("A", "SATCOM degradation may affect long-range communications"),
                    ("B", "Tactical radios appear unaffected - patrol can still communicate"),
                    ("C", "TOC intelligence may be compromised - can they trust the data?"),
                    ("D", "Fire support coordination could be affected if TOC is unavailable"),
                    ("E", "Patrol is completely cut off from all support"),
                    ("F", "Medevac coordination may be impacted"),
                    ("G", "Administrative email delays will harm the patrol"),
                ],
                correct_answers=["A", "B", "C", "D", "F"],
                feedback_correct="""Correct impact assessment:

Communication Impact:
• SATCOM degraded 40% (A) - may affect long-range comms
• Tactical radios appear OK (B) - primary comms still work

Support Impact:
• TOC may be compromised (C) - trust issues with intelligence
• Fire support coordination (D) - could be affected
• Medevac coordination (F) - may be impacted

NOT true:
• Patrol is NOT completely cut off (E) - radios work
• Admin email (G) - not relevant to patrol operations""",
                feedback_incorrect="""Impact on patrol operations:

TRUE IMPACTS:
• SATCOM degraded (A) - affects reach-back capability
• Tactical radios OK (B) - primary comms still work (good news!)
• TOC trust (C) - can they trust intelligence data?
• Fire support (D) - coordination capability uncertain
• Medevac (F) - coordination could be affected

FALSE:
• Complete cutoff (E) - Tactical radios still work
• Admin email (G) - Not relevant to patrol support

Key: Patrol is NOT isolated—radios work. But support may be degraded.""",
                model_answer="A, B, C, D, F - Mixed impacts on communications and support functions.",
                points=3
            ),
            ChecklistQuestion(
                id="5b_q2",
                text="Which systems MUST remain operational to support the patrol? (Select all critical)",
                options=[
                    ("A", "Tactical Radio Network"),
                    ("B", "Administrative email"),
                    ("C", "TOC Network (if secure)"),
                    ("D", "Physical security cameras"),
                    ("E", "SATCOM links"),
                    ("F", "Personnel accountability system"),
                ],
                correct_answers=["A", "C", "E"],
                feedback_correct="""Correct! Critical for patrol support:

• Tactical Radios: Primary communication with patrol—MUST HAVE
• TOC Network: Coordination, intelligence, fire support—CRITICAL (if secure)
• SATCOM: Link to higher HQ for additional support—IMPORTANT

Not critical for immediate patrol support:
• Admin email: Can wait
• Cameras: FOB security, not patrol support
• Personnel system: Important but not immediate""",
                feedback_incorrect="""Critical systems for patrol support:

MUST HAVE:
• Tactical Radio Network: Only way to communicate with patrol
• TOC Network: Fire support, medevac, coordination (IF secure)
• SATCOM: Reach-back to higher HQ for support

CAN OPERATE WITHOUT (short-term):
• Administrative email: Not operationally critical
• Physical security cameras: FOB security, not patrol support
• Personnel accountability: Important but not immediate

The patrol needs COMMUNICATION and COORDINATION support.""",
                model_answer="A, C, E - Tactical radios, TOC network, and SATCOM are critical.",
                points=2
            ),
        ]
    )

    # Part C: Response Prioritization
    scenario_response = Scenario(
        id="5c",
        title="Part C: Response Prioritization",
        description="""You must take immediate action and recommend containment measures. The brigade
commander will need a briefing on the situation.

Prioritize your response actions.""",
        questions=[
            RankingQuestion(
                id="5c_q1",
                text="Rank these IMMEDIATE ACTIONS by priority (1 = do first):",
                items=[
                    "Isolate administrative network from TOC",
                    "Call higher headquarters for help",
                    "Verify tactical radio functionality",
                ],
                correct_answer=[1, 3, 2],
                num_ranks=3,
                feedback_correct="""Correct priority:

1. Isolate admin network - Stop lateral movement NOW
2. Verify tactical radios - Ensure patrol support capability
3. Call higher HQ - Important but can wait minutes

Isolation is urgent because the attacker is actively trying to access TOC.
Stop the bleeding first, then verify capabilities, then get help.""",
                feedback_incorrect="""Priority order:

1. Isolate admin from TOC - URGENT
   The attacker is actively trying to get to classified systems.
   Every minute of delay is another chance for them to succeed.

2. Verify tactical radio functionality
   Confirm you can still support the patrol.
   This takes seconds and is critical.

3. Call higher headquarters
   Important, but the first two actions take minutes.
   Don't wait for help to arrive before taking obvious actions.""",
                model_answer="1-Isolate, 2-Verify radios, 3-Call HQ",
                points=2
            ),
            ChecklistQuestion(
                id="5c_q2",
                text="Which containment actions should you take for the ADMINISTRATIVE NETWORK? (Select all appropriate)",
                options=[
                    ("A", "Isolate from TOC network immediately"),
                    ("B", "Shut down completely"),
                    ("C", "Monitor closely but don't disrupt"),
                    ("D", "Preserve evidence on compromised workstation"),
                    ("E", "Block external traffic to unknown IP"),
                    ("F", "Delete all suspicious files"),
                ],
                correct_answers=["A", "D", "E"],
                feedback_correct="""Correct containment actions:

• Isolate from TOC: Stop lateral movement (critical)
• Preserve evidence: Don't destroy forensic data
• Block C2 traffic: Cut attacker's communication

Why NOT others:
• Complete shutdown loses evidence and may not be necessary
• Just monitoring lets attack continue
• Deleting files destroys evidence""",
                feedback_incorrect="""Appropriate containment:

DO:
• A - Isolate from TOC: Stop lateral movement
• D - Preserve evidence: Critical for investigation
• E - Block C2 traffic: Cut attacker communication

DON'T:
• B - Complete shutdown: May not be necessary, loses volatile evidence
• C - Just monitor: Attack continues while you watch
• F - Delete files: Destroys evidence, doesn't stop attack

Balance: Contain the threat while preserving evidence.""",
                model_answer="A, D, E - Isolate, preserve evidence, block C2.",
                points=2
            ),
            ChecklistQuestion(
                id="5c_q3",
                text="What elements MUST be included in your commander briefing? (Select all required)",
                options=[
                    ("A", "What happened - suspected network intrusion"),
                    ("B", "Complete technical details of the malware"),
                    ("C", "Current status - admin compromised, TOC targeted but secure"),
                    ("D", "Impact on patrol - tactical radios working, support maintained"),
                    ("E", "Actions taken - isolating networks, investigating"),
                    ("F", "Detailed CVE numbers for vulnerabilities exploited"),
                    ("G", "Recommendation - shift to backup procedures"),
                    ("H", "Timeline - when each indicator was observed"),
                ],
                correct_answers=["A", "C", "D", "E", "G"],
                feedback_correct="""Correct! Commander brief essentials (BLUF format):

MUST INCLUDE:
• What happened (A) - Bottom line upfront
• Current status (C) - What's affected, what's secure
• Patrol impact (D) - Operational concern
• Actions taken (E) - What you're doing about it
• Recommendation (G) - What you need them to decide

DON'T NEED (for immediate brief):
• Technical malware details (B) - Too detailed for commander
• CVE numbers (F) - Technical, not decision-relevant
• Full timeline (H) - Save for written report""",
                feedback_incorrect="""Commander brief must be concise and decision-focused:

REQUIRED:
• A - What happened: The situation (BLUF)
• C - Current status: Impact assessment
• D - Patrol impact: Operational priority
• E - Actions taken: What you're doing
• G - Recommendation: What you need from them

NOT REQUIRED (for immediate brief):
• B - Technical details: Too deep for command brief
• F - CVE numbers: Irrelevant for commander decision
• H - Full timeline: Goes in written report

Commanders need: Situation, impact, actions, recommendation.""",
                model_answer="A, C, D, E, G - Situation, status, impact, actions, recommendation.",
                points=3
            ),
        ]
    )

    # Part D: Legal and Ethical
    scenario_legal = Scenario(
        id="5d",
        title="Part D: Ethical and Legal Considerations",
        description="""As you respond to this incident, you must consider what actions you can take
independently and what requires authorization.""",
        questions=[
            ChecklistQuestion(
                id="5d_q1",
                text="Which actions can you take IMMEDIATELY without additional authorization? (Select all that apply)",
                options=[
                    ("A", "Isolate compromised network segment"),
                    ("B", "Hack back against the attacker"),
                    ("C", "Preserve evidence"),
                    ("D", "Notify chain of command"),
                    ("E", "Cancel all ongoing operations"),
                    ("F", "Increase monitoring on TOC network"),
                    ("G", "Wipe all potentially compromised systems"),
                ],
                correct_answers=["A", "C", "D", "F"],
                feedback_correct="""Correct! You can immediately:
• Isolate networks (containment)
• Preserve evidence (your responsibility)
• Notify chain of command (required)
• Increase monitoring (defensive measure)

You CANNOT without authorization:
• Hack back (illegal/policy violation)
• Cancel operations (commander decision)
• Wipe systems (destroys evidence, operational impact)""",
                feedback_incorrect="""Immediate authority:

CAN DO NOW:
• Isolate networks - Defensive containment
• Preserve evidence - Your responsibility
• Notify chain of command - Required reporting
• Increase monitoring - Defensive measure

REQUIRES AUTHORIZATION:
• Hack back - Illegal without authorization
• Cancel operations - Commander decision
• Wipe systems - Destroys evidence, impacts operations

You have authority for defensive actions, not offensive or operational decisions.""",
                model_answer="A, C, D, F - Defensive containment and reporting actions.",
                points=2
            ),
            ChecklistQuestion(
                id="5d_q2",
                text="What MUST you document during this incident? (Select all required)",
                options=[
                    ("A", "Timeline of when each event/indicator was observed"),
                    ("B", "Personal opinions about who is responsible"),
                    ("C", "All actions taken and by whom"),
                    ("D", "Evidence preserved and chain of custody"),
                    ("E", "Notifications made and when"),
                    ("F", "Decisions made and the rationale"),
                    ("G", "Guesses about attacker identity"),
                    ("H", "System states before and after actions"),
                ],
                correct_answers=["A", "C", "D", "E", "F", "H"],
                feedback_correct="""Correct! Documentation requirements:

MUST DOCUMENT:
• Timeline (A) - When things happened
• Actions taken (C) - What you did and who did it
• Evidence custody (D) - What was preserved and how
• Notifications (E) - Who was told what and when
• Decisions (F) - What was decided and why
• System states (H) - Before/after snapshots

DO NOT DOCUMENT:
• Personal opinions (B) - Not factual
• Guesses (G) - Not evidentiary

Document as if this will be reviewed by investigators and lawyers.""",
                feedback_incorrect="""Incident documentation requirements:

REQUIRED:
• Timeline (A) - Chronological record
• Actions taken (C) - What, when, by whom
• Evidence chain (D) - Custody documentation
• Notifications (E) - Communication record
• Decisions (F) - Decision rationale
• System states (H) - Forensic baseline

NOT APPROPRIATE:
• Personal opinions (B) - Not factual evidence
• Guesses (G) - Speculation doesn't belong in records

Document facts, not speculation. This may be subpoenaed.""",
                model_answer="A, C, D, E, F, H - Timeline, actions, evidence, notifications, decisions, states.",
                points=2
            ),
        ]
    )

    # Part E: Lessons Learned
    scenario_lessons = Scenario(
        id="5e",
        title="Part E: Lessons Learned",
        description="""After the incident is contained, you need to identify root causes and
recommend improvements to prevent similar incidents.""",
        questions=[
            MultipleChoiceQuestion(
                id="5e_q1",
                text="What was the ROOT CAUSE that enabled this attack to succeed initially?",
                options=[
                    ("A", "SATCOM degradation"),
                    ("B", "Camera system failures"),
                    ("C", "User clicked phishing link and delayed reporting"),
                    ("D", "Weak network segmentation"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Root cause: Phishing success + delayed reporting

The attack succeeded because:
• User received phishing email
• User clicked the link (initial compromise)
• User waited 48 hours before reporting
• This gave attacker time to establish persistence

Without the successful phishing click, none of the other indicators
would have occurred. The delay allowed escalation.""",
                feedback_incorrect="""Root cause: Phishing success

The attack succeeded because:
• User clicked phishing link = initial access
• 48-hour delay in reporting = time for persistence
• Everything else (C2, lateral movement) stemmed from this

SATCOM and camera issues may be symptoms, not causes.
Weak segmentation enabled spread but wasn't the root cause.

The phishing click was the initial access vector—the root cause.""",
                model_answer="C - User clicked phishing link and waited 48 hours to report.",
                points=2
            ),
            ChecklistQuestion(
                id="5e_q2",
                text="Which THREE measures would be MOST effective at preventing similar incidents? (Select exactly 3)",
                options=[
                    ("A", "User awareness training focused on phishing"),
                    ("B", "Faster gym reservation system"),
                    ("C", "Network segmentation between admin and classified networks"),
                    ("D", "Enhanced email filtering and sandboxing"),
                    ("E", "More comfortable office chairs"),
                    ("F", "Endpoint detection and response (EDR) on all systems"),
                    ("G", "Annual security briefings"),
                ],
                correct_answers=["A", "C", "D"],
                feedback_correct="""Correct! Most effective prevention:

1. User awareness training (A) - Prevent initial phishing success
2. Network segmentation (C) - Limit lateral movement even if compromised
3. Enhanced email filtering (D) - Block phishing before it reaches users

EDR (F) is also valuable but these three address the specific attack path.""",
                feedback_incorrect="""Most effective prevention measures:

1. User awareness training (A)
   - Address root cause: user clicked phishing link
   - Reduce initial compromise risk

2. Network segmentation (C)
   - Admin network shouldn't reach TOC directly
   - Limit impact of any future compromise

3. Enhanced email filtering (D)
   - Block phishing emails before delivery
   - Reduce attack surface

These directly address the attack path observed.""",
                model_answer="A, C, D - Training, segmentation, and email filtering.",
                points=3
            ),
            ChecklistQuestion(
                id="5e_q3",
                text="At which points could this attack have been detected EARLIER? (Select all detection opportunities)",
                options=[
                    ("A", "Email security - detect/block phishing email before delivery"),
                    ("B", "User reports immediately instead of waiting 48 hours"),
                    ("C", "Endpoint detection - catch malware on installation"),
                    ("D", "Network monitoring - detect C2 traffic pattern earlier"),
                    ("E", "Authentication monitoring - flag unusual login patterns"),
                    ("F", "Wait for attacker to send a ransom note"),
                    ("G", "SIEM correlation - connect multiple indicators"),
                ],
                correct_answers=["A", "B", "C", "D", "E", "G"],
                feedback_correct="""Correct! Earlier detection opportunities:

• Email security (A) - Block phishing at perimeter
• Immediate reporting (B) - 48-hour gap was critical lost time
• Endpoint detection (C) - Catch malware on install
• Network monitoring (D) - Detect C2 beaconing earlier
• Auth monitoring (E) - Flag anomalous login attempts
• SIEM correlation (G) - Connect indicators sooner

NOT a detection strategy:
• Waiting for ransom note (F) - Reactive, not proactive

The 48-hour delay was the biggest missed opportunity.""",
                feedback_incorrect="""Detection opportunities were missed at multiple points:

COULD HAVE DETECTED EARLIER:
• Email security (A) - Block phishing before delivery
• Immediate reporting (B) - Don't wait 48 hours!
• Endpoint detection (C) - Catch malware installation
• Network monitoring (D) - Detect C2 traffic patterns
• Auth monitoring (E) - Unusual login patterns
• SIEM correlation (G) - Connect the dots

NOT A DETECTION STRATEGY:
• Waiting for ransom (F) - That's letting the attack succeed

Key gap: The 48-hour reporting delay was the biggest
missed detection opportunity.""",
                model_answer="A, B, C, D, E, G - Multiple earlier detection points were available.",
                points=3
            ),
        ]
    )

    # Create the exercise
    exercise = Exercise(
        id="exercise5",
        number=5,
        title="Comprehensive Scenario Assessment",
        description="""This capstone exercise integrates all Module 1 concepts into a realistic
incident response scenario at a forward operating base. You will apply CIA Triad analysis,
threat actor assessment, mission impact analysis, and ethical decision-making to respond
to an active cyber incident.""",
        estimated_time="45-60 minutes",
        objectives=[
            "Integrate all Module 1 concepts in a realistic scenario",
            "Assess threats and position attacks in the kill chain",
            "Analyze mission impact and prioritize response actions",
            "Apply ethical and legal principles to incident response",
            "Identify root causes and recommend preventive measures",
        ],
        scenarios=[
            scenario_initial,
            scenario_mission,
            scenario_response,
            scenario_legal,
            scenario_lessons
        ]
    )

    return exercise
