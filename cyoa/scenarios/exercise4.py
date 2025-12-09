"""Exercise 4: Ethical Scenarios."""

from .base import (
    Exercise,
    Scenario,
    MultipleChoiceQuestion,
    ChecklistQuestion,
)


def get_exercise() -> Exercise:
    """Create and return Exercise 4."""

    # Scenario 4A: The Urgent Request
    scenario_4a = Scenario(
        id="4a",
        title="Scenario 4A: The Urgent Request",
        description="""A battalion commander in a deployed location emails you directly, requesting
immediate administrator access to a classified system. They state it's mission-critical and
there's no time for the proper authorization process.

Your security manager is on leave and unreachable. The commander outranks you significantly
and is known for a short temper.""",
        questions=[
            ChecklistQuestion(
                id="4a_q1",
                text="What ethical principles are in CONFLICT in this situation? (Select ALL that apply)",
                options=[
                    ("A", "Duty to follow chain of command vs. security responsibility"),
                    ("B", "Respect for rank vs. policy compliance"),
                    ("C", "Short-term mission needs vs. long-term security"),
                    ("D", "Personal comfort vs. doing the right thing"),
                    ("E", "Budget constraints vs. staffing needs"),
                ],
                correct_answers=["A", "B", "C", "D"],
                feedback_correct="""Correct! The ethical conflicts are:
- A - Military authority vs. security authority
- B - Respecting rank vs. following policy
- C - Immediate mission vs. security requirements
- D - Avoiding confrontation vs. doing what's right

Budget/staffing (E) is not relevant to this scenario.""",
                feedback_incorrect="""The ethical tensions in this scenario:
- A - Chain of command vs. security duties
- B - Rank respect vs. policy compliance
- C - Mission urgency vs. security procedures
- D - Personal comfort vs. correct action

These are real ethical dilemmas security professionals face.""",
                model_answer="A, B, C, D - Authority, rank, mission, and personal comfort conflicts.",
                points=2
            ),
            ChecklistQuestion(
                id="4a_q2",
                text="What could go WRONG if you grant the access without authorization? (Select ALL that apply)",
                options=[
                    ("A", "The email might be spoofed (not really from the commander)"),
                    ("B", "The commander's account might be compromised"),
                    ("C", "You bypass controls designed to prevent insider threats"),
                    ("D", "You would be personally responsible for the security bypass"),
                    ("E", "The commander will be happy"),
                ],
                correct_answers=["A", "B", "C", "D"],
                feedback_correct="""Correct! Risks of granting unauthorized access:
- A - Email spoofing: Can't verify identity via email
- B - Compromised account: Attacker using commander's email
- C - Bypassing controls: Defeats security measures
- D - Personal responsibility: You own the consequences

The commander being happy (E) is not a risk.""",
                feedback_incorrect="""Security risks of compliance:
- A - Email can be spoofed
- B - Account could be compromised
- C - Security controls exist for a reason
- D - You're accountable for bypasses

These aren't hypothetical—this is exactly how insider threats and social engineering work.""",
                model_answer="A, B, C, D - Spoofing, compromise, bypass, personal liability.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4a_q3",
                text="What is the BEST course of action?",
                options=[
                    ("A", "Grant the access immediately to support the mission"),
                    ("B", "Refuse and tell the commander to go through proper channels"),
                    ("C", "Respectfully explain requirements, offer to expedite through alternate security authority"),
                    ("D", "Ignore the email and hope it goes away"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! The best approach is to be helpful while maintaining security:
1. Respectfully explain the authorization requirements
2. Offer to help expedite through proper channels
3. Contact backup security authority
4. Document the request and your response

This maintains security while showing you're trying to help the mission.""",
                feedback_incorrect="""Best approach: Be helpful while maintaining security.

Don't just refuse—offer solutions:
- Explain why you can't grant immediate access
- Offer to expedite through alternate security personnel
- Contact backup ISSO or security chain
- Document everything

Granting access bypasses security; ignoring it fails the mission AND security.""",
                model_answer="C - Be helpful while maintaining security; find the right way to support.",
                points=2
            ),
            ChecklistQuestion(
                id="4a_q4",
                text="What should you DOCUMENT about this interaction? (Select ALL that apply)",
                options=[
                    ("A", "Date and time of the request"),
                    ("B", "Full text of the request"),
                    ("C", "Your response and reasoning"),
                    ("D", "Actions taken (who you contacted)"),
                    ("E", "Your personal opinions about the commander"),
                ],
                correct_answers=["A", "B", "C", "D"],
                feedback_correct="""Correct! Documentation should include:
- A - Date/time: Establishes timeline
- B - Request text: Exact nature of request
- C - Your response: What you said and why
- D - Actions taken: Who you contacted, what happened

Personal opinions (E) are not appropriate for official documentation.""",
                feedback_incorrect="""Document facts, not opinions:
- A - When it happened
- B - What was requested (save the email)
- C - What you did and why
- D - Who else was involved

Document as if it might become an investigation exhibit.
Personal opinions don't belong in official records.""",
                model_answer="A, B, C, D - Facts and actions, not personal opinions.",
                points=2
            ),
        ]
    )

    # Scenario 4B: Security vs. Mission
    scenario_4b = Scenario(
        id="4b",
        title="Scenario 4B: Security vs. Mission",
        description="""A critical security update requires rebooting servers supporting an ongoing
operation. The operation commander says the reboot cannot happen during their current phase,
which will last another 72 hours.

The vulnerability being patched is being actively exploited in the wild, and threat intelligence
indicates adversaries are targeting systems like yours.""",
        questions=[
            MultipleChoiceQuestion(
                id="4b_q1",
                text="Who has the AUTHORITY to make this risk decision?",
                options=[
                    ("A", "You, as the cybersecurity specialist"),
                    ("B", "The operation commander, with your risk input"),
                    ("C", "The IT help desk"),
                    ("D", "Whoever complains the loudest"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! The commander makes risk decisions with security input.

Security professionals:
- Advise on risks
- Present options
- Document decisions

Commanders:
- Accept or reject risk
- Make mission decisions
- Take responsibility for outcomes

This is a risk acceptance decision that belongs to the commander.""",
                feedback_incorrect="""Security professionals ADVISE—commanders DECIDE.

Your role:
- Present the risk clearly
- Provide options
- Document the decision

Commander's role:
- Evaluate risk vs. mission needs
- Accept or reject the risk
- Take responsibility

This is a command decision with security input, not a security decision.""",
                model_answer="B - Commander decides with security professional input.",
                points=2
            ),
            ChecklistQuestion(
                id="4b_q2",
                text="If patching is delayed, what TEMPORARY MITIGATIONS could reduce risk? (Select ALL that apply)",
                options=[
                    ("A", "Network isolation/segmentation"),
                    ("B", "Enhanced monitoring and alerting"),
                    ("C", "Hope the attackers don't notice"),
                    ("D", "IPS/IDS signatures for the exploit"),
                    ("E", "Disable vulnerable services if not needed"),
                    ("F", "Restrict access to affected systems"),
                ],
                correct_answers=["A", "B", "D", "E", "F"],
                feedback_correct="""Correct! Temporary mitigations include:
- A - Network isolation: Limit exposure
- B - Enhanced monitoring: Detect exploitation attempts
- D - IPS/IDS signatures: Block known exploit patterns
- E - Disable services: Remove attack vector if not needed
- F - Restrict access: Limit who can reach vulnerable systems

"Hope" (C) is never a security strategy.""",
                feedback_incorrect="""Valid temporary mitigations:
- A - Isolation: Limits attack surface
- B - Monitoring: Detects exploitation
- D - IPS/IDS: Blocks known patterns
- E - Disable services: Removes vector
- F - Restrict access: Limits exposure

Hope is not a mitigation strategy.
Mitigations REDUCE risk; they don't eliminate it—patch ASAP.""",
                model_answer="A, B, D, E, F - Isolation, monitoring, IPS, disabling, restricting.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4b_q3",
                text="How should you PRESENT this situation to the commander?",
                options=[
                    ("A", "Demand they patch immediately"),
                    ("B", "Present risk and options, make a recommendation, request their decision"),
                    ("C", "Tell them it's their problem"),
                    ("D", "Make the decision yourself and inform them later"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Present professionally:
1. State the situation clearly
2. Present the risk objectively
3. Provide options with pros/cons
4. Make a recommendation
5. Ask for their decision
6. Document everything

You advise; they decide.""",
                feedback_incorrect="""Professional presentation to commanders:
1. Situation: What's the vulnerability/threat
2. Risk: What could happen, likelihood
3. Options: Patch now, delay with mitigations, accept risk
4. Recommendation: Your professional opinion
5. Request decision: They own the choice

Don't demand, deflect, or decide for them.""",
                model_answer="B - Present risk, options, recommendation; request their decision.",
                points=2
            ),
        ]
    )

    # Scenario 4C: The Discovered Activity
    scenario_4c = Scenario(
        id="4c",
        title="Scenario 4C: The Discovered Activity",
        description="""While investigating a security alert, you discover a senior officer appears to be
using government systems to run a personal business during duty hours.

This activity is completely unrelated to your security investigation. The officer is well-liked
and has a reputation for taking care of their people.""",
        questions=[
            MultipleChoiceQuestion(
                id="4c_q1",
                text="Is this primarily a security issue, policy violation, or both?",
                options=[
                    ("A", "Security issue only"),
                    ("B", "Policy violation only"),
                    ("C", "Both security and policy violation"),
                    ("D", "Neither - it's personal business"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! This is BOTH a security and policy issue:

Security concerns:
- Unauthorized software may be installed
- External connections to business systems
- Potential data leakage paths

Policy violations:
- Misuse of government resources
- Personal business on duty time
- Acceptable use policy violation""",
                feedback_incorrect="""This is both security AND policy:

Security:
- What software was installed?
- What external connections exist?
- Could this create attack vectors?

Policy:
- Misuse of government resources
- Personal business on government time
- Acceptable use violation

Both aspects require appropriate reporting.""",
                model_answer="C - Both security and policy concerns.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4c_q2",
                text="What is your OBLIGATION regarding this discovery?",
                options=[
                    ("A", "Ignore it - not your job and the officer is well-liked"),
                    ("B", "Report through appropriate channels"),
                    ("C", "Confront the officer directly"),
                    ("D", "Investigate further to build a case"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! You must report through appropriate channels.

Why:
- This is not your personal decision to ignore
- Reporting is required, not optional
- Others will determine appropriate action
- You're not the investigator for this issue

Don't ignore, don't confront, don't investigate beyond your scope.""",
                feedback_incorrect="""Your obligation: Report through appropriate channels.

Why:
- Duty to report violations
- Not your decision whether to prosecute
- Others determine appropriate action
- You're not the investigator here

Why NOT the other options:
- Ignoring: Violates your obligations
- Confronting: Not your role, could tip off subject
- Investigating: Beyond your scope""",
                model_answer="B - Report through appropriate channels.",
                points=2
            ),
            ChecklistQuestion(
                id="4c_q3",
                text="Who should you report this to? (Select ALL appropriate)",
                options=[
                    ("A", "Your supervisor"),
                    ("B", "Security manager/ISSO"),
                    ("C", "Inspector General (IG)"),
                    ("D", "The officer's friends"),
                    ("E", "Social media"),
                ],
                correct_answers=["A", "B", "C"],
                feedback_correct="""Correct! Appropriate reporting channels:
- A - Your supervisor: First line reporting
- B - Security manager: For security aspects
- C - Inspector General: For fraud, waste, abuse

Do NOT report to friends (gossip) or social media (unprofessional/unauthorized).""",
                feedback_incorrect="""Appropriate reporting channels:
- A - Supervisor: Chain of command
- B - Security manager: Security concerns
- C - Inspector General: Waste/fraud/abuse

Use established channels. Don't gossip to friends or post on social media.""",
                model_answer="A, B, C - Supervisor, security manager, or IG.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4c_q4",
                text="What should you NOT document in your security investigation notes?",
                options=[
                    ("A", "Facts you directly observed"),
                    ("B", "How you discovered this activity"),
                    ("C", "Your personal opinions about the officer"),
                    ("D", "Date and time of your observations"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Do NOT document personal opinions.

Document:
- Facts you directly observed
- How you discovered the activity
- Dates, times, systems, actions

Don't document:
- Personal opinions
- Speculation
- Judgments about severity

Keep it factual and objective.""",
                feedback_incorrect="""Documentation should be FACTUAL:

Document:
- What you observed (facts)
- How you found it (context)
- When it happened (timeline)

Don't document:
- Personal opinions
- Speculation
- Character judgments

Let investigators investigate; you just report what you found.""",
                model_answer="C - Personal opinions don't belong in documentation.",
                points=2
            ),
        ]
    )

    # Scenario 4D: The Helpful Contractor
    scenario_4d = Scenario(
        id="4d",
        title="Scenario 4D: The Helpful Contractor",
        description="""A contractor working in your facility offers to help you solve a persistent
system problem that's been frustrating you for weeks.

They suggest a solution that requires them to access a system they're not authorized for.
The contractor says, "It's fine, everyone does it, and it will only take a minute. No one
will ever know." """,
        questions=[
            ChecklistQuestion(
                id="4d_q1",
                text="What RED FLAGS are present in this situation? (Select ALL that apply)",
                options=[
                    ("A", '"Everyone does it" justification'),
                    ("B", '"No one will ever know" secrecy'),
                    ("C", "Request to access unauthorized systems"),
                    ("D", "Circumventing security controls"),
                    ("E", "Time pressure ('just a minute')"),
                    ("F", "Offering to help with a problem"),
                ],
                correct_answers=["A", "B", "C", "D", "E"],
                feedback_correct="""Correct! Major red flags:
- A - "Everyone does it": Social engineering tactic
- B - "No one will know": Implies awareness it's wrong
- C - Unauthorized access request: Clear violation
- D - Circumventing controls: Security bypass
- E - Time pressure: Prevents careful thought

Offering help alone (F) isn't a red flag, but combined with others it's concerning.""",
                feedback_incorrect="""Red flags in this scenario:
- A - "Everyone does it": Classic manipulation
- B - "No one will know": Acknowledges wrongdoing
- C - Unauthorized access: Clear policy violation
- D - Circumventing controls: What attackers do
- E - Time pressure: Prevents careful thinking

These are textbook social engineering indicators.""",
                model_answer="A, B, C, D, E - Social engineering and policy violation indicators.",
                points=2
            ),
            ChecklistQuestion(
                id="4d_q2",
                text="What POLICIES or LAWS could be violated? (Select ALL that apply)",
                options=[
                    ("A", "Access control policies"),
                    ("B", "Computer Fraud and Abuse Act"),
                    ("C", "Contractor oversight requirements"),
                    ("D", "Acceptable use policy"),
                    ("E", "Dress code"),
                ],
                correct_answers=["A", "B", "C", "D"],
                feedback_correct="""Correct! Potential violations:
- A - Access control policies: Unauthorized system access
- B - CFAA: Federal law on unauthorized computer access
- C - Contractor oversight: Access limitations
- D - Acceptable use: System misuse

Dress code (E) is unrelated to this security scenario.""",
                feedback_incorrect="""Potential violations:
- A - Access control: Clear violation
- B - CFAA: Federal computer crime law
- C - Contractor requirements: Access limits
- D - Acceptable use: Misuse of systems

Both you AND the contractor could face consequences for this violation.""",
                model_answer="A, B, C, D - Access policies, federal law, contractor rules, acceptable use.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4d_q3",
                text="What is the BEST response to the contractor?",
                options=[
                    ("A", "Sure, thanks for the help!"),
                    ("B", "Politely decline and explain you can't authorize their access"),
                    ("C", "Report them immediately without saying anything"),
                    ("D", "Ask them to show you how and do it yourself"),
                ],
                correct_answer="B",
                feedback_correct="""Correct! Politely decline and explain the boundary.

This approach:
- Maintains professional relationship
- Clearly states the limitation
- Doesn't assume malicious intent (could be ignorance)
- Preserves your integrity
- Allows you to then assess if reporting is needed""",
                feedback_incorrect="""Best response: Politely decline and explain.

Example: "I appreciate the offer, but I can't authorize access to systems
you're not cleared for. Let me work with my security team to find an
appropriate solution."

Then assess whether to report the request.""",
                model_answer="B - Politely decline and explain the limitation.",
                points=2
            ),
            MultipleChoiceQuestion(
                id="4d_q4",
                text="Should you REPORT this interaction?",
                options=[
                    ("A", "No, they were just trying to help"),
                    ("B", "Only if they keep asking"),
                    ("C", "Yes, to security manager and contracting officer"),
                    ("D", "Only if the system gets compromised later"),
                ],
                correct_answer="C",
                feedback_correct="""Correct! Yes, report this interaction.

Report to:
- Security manager: Insider threat indicators
- Contracting Officer Representative: Contractor oversight

Why report:
- Multiple red flags present
- Could be social engineering attempt
- May be testing security awareness
- Pattern might exist with others
- Documentation protects you""",
                feedback_incorrect="""Yes, report this interaction because:
- Multiple insider threat indicators present
- Could be social engineering/elicitation
- May be testing your security awareness
- Pattern might exist with other employees
- Documentation protects you if questioned

You're not accusing—you're reporting concerning indicators.""",
                model_answer="C - Yes, report to security manager and contracting officer.",
                points=2
            ),
        ]
    )

    # Create the exercise
    exercise = Exercise(
        id="exercise4",
        number=4,
        title="Ethical Scenarios",
        description="""This exercise presents realistic ethical dilemmas you may face as a Cyber Defense
Infrastructure Support Specialist. You will navigate situations involving competing priorities,
policy requirements, and professional obligations.""",
        estimated_time="30-40 minutes",
        objectives=[
            "Apply ethical principles to cybersecurity dilemmas",
            "Understand applicable policies and regulations",
            "Make appropriate decisions under pressure",
            "Know proper reporting channels and documentation requirements",
        ],
        scenarios=[scenario_4a, scenario_4b, scenario_4c, scenario_4d]
    )

    return exercise
