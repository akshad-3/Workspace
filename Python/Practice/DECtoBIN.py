from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Page setup ──────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN = 2 * cm

# ── Colour palette ───────────────────────────────────────────────────────────
C_NAVY   = colors.HexColor("#1a2a4a")
C_BLUE   = colors.HexColor("#2563eb")
C_LBLUE  = colors.HexColor("#dbeafe")
C_TEAL   = colors.HexColor("#0d9488")
C_LTEAL  = colors.HexColor("#ccfbf1")
C_PURPLE = colors.HexColor("#7c3aed")
C_LPURP  = colors.HexColor("#ede9fe")
C_ORANGE = colors.HexColor("#ea580c")
C_LORG   = colors.HexColor("#ffedd5")
C_GREEN  = colors.HexColor("#16a34a")
C_LGRN   = colors.HexColor("#dcfce7")
C_GREY   = colors.HexColor("#64748b")
C_LGREY  = colors.HexColor("#f1f5f9")
C_WHITE  = colors.white
C_BLACK  = colors.HexColor("#0f172a")

def build_styles():
    base = getSampleStyleSheet()

    def add(name, **kw):
        base.add(ParagraphStyle(name=name, **kw))

    # Cover
    add("CoverTitle",
        fontName="Helvetica-Bold", fontSize=34, textColor=C_WHITE,
        alignment=TA_CENTER, leading=42, spaceAfter=10)
    add("CoverSub",
        fontName="Helvetica", fontSize=16, textColor=colors.HexColor("#bfdbfe"),
        alignment=TA_CENTER, leading=22, spaceAfter=6)
    add("CoverMeta",
        fontName="Helvetica", fontSize=12, textColor=colors.HexColor("#e2e8f0"),
        alignment=TA_CENTER, leading=18)

    # Unit banner
    add("UnitBanner",
        fontName="Helvetica-Bold", fontSize=20, textColor=C_WHITE,
        alignment=TA_CENTER, leading=26, spaceAfter=4)
    add("UnitBannerSub",
        fontName="Helvetica", fontSize=12, textColor=colors.HexColor("#bfdbfe"),
        alignment=TA_CENTER, leading=16)

    # Headings
    add("H1", fontName="Helvetica-Bold", fontSize=18, textColor=C_NAVY,
        spaceBefore=18, spaceAfter=8, leading=24)
    add("H2", fontName="Helvetica-Bold", fontSize=14, textColor=C_BLUE,
        spaceBefore=14, spaceAfter=6, leading=20)
    add("H3", fontName="Helvetica-Bold", fontSize=12, textColor=C_TEAL,
        spaceBefore=10, spaceAfter=5, leading=18)
    add("H4", fontName="Helvetica-Bold", fontSize=11, textColor=C_PURPLE,
        spaceBefore=8, spaceAfter=4, leading=16)

    # Body text
    add("Body", fontName="Helvetica", fontSize=10.5, textColor=C_BLACK,
        leading=17, spaceAfter=6, alignment=TA_JUSTIFY)
    add("BodyBold", fontName="Helvetica-Bold", fontSize=10.5, textColor=C_BLACK,
        leading=17, spaceAfter=4)

    # Bullet / numbered
    add("MyBullet", fontName="Helvetica", fontSize=10.5, textColor=C_BLACK,
        leading=16, spaceAfter=4, leftIndent=14, firstLineIndent=0,
        bulletIndent=0)
    add("MyBullet2", fontName="Helvetica", fontSize=10, textColor=C_GREY,
        leading=15, spaceAfter=3, leftIndent=28, firstLineIndent=0)

    # Callout / definition box label
    add("BoxLabel", fontName="Helvetica-Bold", fontSize=10, textColor=C_TEAL,
        spaceAfter=2, leading=14)
    add("BoxBody", fontName="Helvetica", fontSize=10, textColor=C_BLACK,
        leading=15, spaceAfter=2)

    # Caption / note
    add("Note", fontName="Helvetica-Oblique", fontSize=9.5, textColor=C_GREY,
        leading=14, spaceAfter=4)

    # TOC entries
    add("TOCUnit", fontName="Helvetica-Bold", fontSize=12, textColor=C_NAVY,
        spaceBefore=8, spaceAfter=2, leading=18)
    add("TOCItem", fontName="Helvetica", fontSize=10.5, textColor=C_GREY,
        spaceBefore=1, spaceAfter=1, leading=15, leftIndent=14)

    return base

S = build_styles()

# ── Helper builders ──────────────────────────────────────────────────────────

def spacer(h=6):
    return Spacer(1, h)

def hr(color=C_BLUE, thickness=0.8):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=4)

def p(text, style="Body"):
    return Paragraph(text, S[style])

def h1(text): return p(text, "H1")
def h2(text): return p(text, "H2")
def h3(text): return p(text, "H3")
def h4(text): return p(text, "H4")

def bullets(items, style="MyBullet", symbol="•"):
    return [p(f"{symbol}  {item}", style) for item in items]

def numbered(items, start=1):
    return [p(f"<b>{i+start}.</b>  {item}", "Bullet") for i, item in enumerate(items)]

def sub_bullets(items):
    return [p(f"    –  {item}", "MyBullet2") for item in items]

def definition_box(label, body, bg=C_LTEAL, border=C_TEAL):
    """A coloured definition / key-concept box."""
    content = f"<b>{label}:</b>  {body}"
    tbl = Table([[Paragraph(content, S["BoxBody"])]], colWidths=[PAGE_W - 2*MARGIN - 4])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 1, border),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING",   (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[bg]),
    ]))
    return tbl

def info_box(text, bg=C_LBLUE, border=C_BLUE):
    tbl = Table([[Paragraph(text, S["BoxBody"])]], colWidths=[PAGE_W - 2*MARGIN - 4])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 1, border),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING",   (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0), (-1,-1), 8),
    ]))
    return tbl

def two_col_table(rows, headers=None, col_ratio=(0.35, 0.65)):
    """Simple 2-column table."""
    w = PAGE_W - 2*MARGIN - 4
    cw = [w * col_ratio[0], w * col_ratio[1]]
    data = []
    if headers:
        data.append([Paragraph(f"<b>{headers[0]}</b>", S["BodyBold"]),
                     Paragraph(f"<b>{headers[1]}</b>", S["BodyBold"])])
    for a, b in rows:
        data.append([Paragraph(a, S["Body"]), Paragraph(b, S["Body"])])
    tbl = Table(data, colWidths=cw)
    style = [
        ("GRID",      (0,0),(-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("BACKGROUND",(0,0),(-1,0),  C_NAVY),
        ("TEXTCOLOR", (0,0),(-1,0),  C_WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[C_WHITE, C_LGREY]),
        ("LEFTPADDING",  (0,0),(-1,-1),8),
        ("RIGHTPADDING", (0,0),(-1,-1),8),
        ("TOPPADDING",   (0,0),(-1,-1),6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("VALIGN",       (0,0),(-1,-1),"TOP"),
    ]
    if not headers:
        style[1] = ("BACKGROUND",(0,0),(-1,-1),C_WHITE)
        style[2] = ("TEXTCOLOR", (0,0),(-1,-1),C_BLACK)
    tbl.setStyle(TableStyle(style))
    return tbl

def unit_banner(unit_no, unit_title, topics):
    """Full-width coloured unit header block."""
    bg_colors = [C_NAVY, C_TEAL, C_PURPLE]
    bg = bg_colors[(unit_no - 1) % len(bg_colors)]
    rows = [
        [Paragraph(f"UNIT {unit_no}", S["UnitBanner"])],
        [Paragraph(unit_title, S["CoverSub"])],
        [Paragraph(f"Topics: {topics}", S["UnitBannerSub"])],
    ]
    tbl = Table(rows, colWidths=[PAGE_W - 2*MARGIN - 4])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), bg),
        ("LEFTPADDING",  (0,0),(-1,-1), 20),
        ("RIGHTPADDING", (0,0),(-1,-1), 20),
        ("TOPPADDING",   (0,0),(-1,-1), 16),
        ("BOTTOMPADDING",(0,0),(-1,-1), 16),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[bg]),
    ]))
    return tbl

# ═══════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ═══════════════════════════════════════════════════════════════════════════
def cover_page():
    story = []

    # Big coloured header table
    cover_rows = [
        [Paragraph("SOFTWARE TESTING", S["CoverTitle"])],
        [Paragraph("Complete Study Notes", S["CoverSub"])],
        [Spacer(1, 10)],
        [Paragraph("All Three Units — Fully Detailed & Exam Ready", S["CoverMeta"])],
        [Spacer(1, 6)],
        [Paragraph("Unit I  •  Unit II  •  Unit III", S["CoverMeta"])],
    ]
    cover_tbl = Table(cover_rows, colWidths=[PAGE_W - 2*MARGIN - 4])
    cover_tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), C_NAVY),
        ("LEFTPADDING",  (0,0),(-1,-1), 30),
        ("RIGHTPADDING", (0,0),(-1,-1), 30),
        ("TOPPADDING",   (0,0),(-1,-1), 50),
        ("BOTTOMPADDING",(0,0),(-1,-1), 50),
    ]))
    story.append(cover_tbl)
    story.append(spacer(20))

    # What's inside
    story.append(info_box(
        "<b>What's Inside:</b>  Principles of Testing · SDLC · Quality Assurance · "
        "White Box Testing · Black Box Testing · Integration Testing · "
        "System Testing · Acceptance Testing — explained simply with examples.",
        bg=C_LBLUE, border=C_BLUE
    ))
    story.append(spacer(30))

    # TOC
    story.append(p("<b>TABLE OF CONTENTS</b>", "H1"))
    story.append(hr())
    story.append(spacer(6))

    toc_entries = [
        ("UNIT I — Principles of Testing & SDLC", [
            "Phases of a Software Project",
            "Quality, Quality Assurance & Quality Control",
            "Testing: Goals & Principles",
            "Verification and Validation",
            "Process Models",
            "Life Cycle Models (Waterfall, V-Model, Spiral, Agile)",
            "Software Testing Life Cycle (STLC)",
            "Static Testing",
            "Structural Testing (White Box Testing)",
            "Challenges in White Box Testing",
            "Black Box Testing & its Process",
        ]),
        ("UNIT II — Integration Testing", [
            "Definition & Purpose",
            "Top-Down Integration",
            "Bottom-Up Integration",
            "Bi-Directional Integration",
            "System Integration",
            "Choosing an Integration Method",
            "Integration as a Phase of Testing",
            "Scenario Testing",
            "System Scenarios & Use Case Scenarios",
            "Defect Bash",
        ]),
        ("UNIT III — System & Acceptance Testing", [
            "Functional vs Non-Functional Testing",
            "Functional System Testing",
            "Non-Functional System Testing",
            "Performance, Load, Stress, Security Testing",
            "Acceptance Testing",
            "Alpha & Beta Testing",
            "User Acceptance Testing (UAT)",
        ]),
    ]

    for unit_title, items in toc_entries:
        story.append(p(f"<b>{unit_title}</b>", "TOCUnit"))
        for item in items:
            story.append(p(f"    › {item}", "TOCItem"))
        story.append(spacer(6))

    story.append(PageBreak())
    return story


# ═══════════════════════════════════════════════════════════════════════════
# UNIT I
# ═══════════════════════════════════════════════════════════════════════════
def unit1():
    s = []
    s.append(unit_banner(1, "Principles of Testing & Software Development Life Cycle",
        "SDLC · Quality · QA/QC · Testing · V&V · Process Models · STLC · WBT · BBT"))
    s.append(spacer(16))

    # ── 1.1 Phases of a Software Project ────────────────────────────────────
    s.append(h1("1.1  Phases of a Software Project"))
    s.append(hr())
    s.append(p(
        "A software project is not built in one single step — it goes through a series of "
        "well-defined <b>phases</b>. Each phase has its own goals, inputs, outputs, and people "
        "responsible. Understanding these phases is the very foundation of software testing "
        "because testing happens (or should happen) in every phase."
    ))
    s.append(spacer(6))
    s.append(h3("The 6 Core Phases"))

    phases = [
        ("<b>1. Requirements Gathering & Analysis</b>",
         "The team meets with clients/stakeholders to understand WHAT the software must do. "
         "Requirements are documented as SRS (Software Requirements Specification). "
         "<b>Key question:</b> What does the customer want?"),
        ("<b>2. System Design</b>",
         "Engineers decide HOW the software will be built — architecture, database design, "
         "technology stack, UI design. Output: Design Document (HLD + LLD). "
         "<b>Key question:</b> How will we build it?"),
        ("<b>3. Implementation (Coding)</b>",
         "Developers write actual source code based on design documents. "
         "Programming languages, frameworks, and tools are used here. "
         "<b>Key question:</b> Let's build it!"),
        ("<b>4. Testing</b>",
         "The built software is tested against requirements to find defects. "
         "Multiple levels of testing occur — Unit, Integration, System, Acceptance. "
         "<b>Key question:</b> Does it work correctly?"),
        ("<b>5. Deployment</b>",
         "The tested, approved software is released to the real environment (production). "
         "This may be done in phases — pilot release, then full release. "
         "<b>Key question:</b> Can we release it safely?"),
        ("<b>6. Maintenance</b>",
         "After release, bugs reported by users are fixed, new features are added, and "
         "the software is updated. Testing continues here too. "
         "<b>Key question:</b> How do we keep it working well?"),
    ]
    for title, desc in phases:
        s.append(definition_box(title, desc, bg=C_LGREY, border=C_BLUE))
        s.append(spacer(5))

    s.append(info_box(
        "<b>Key Insight:</b>  Testing is NOT just one phase. It spans the entire project. "
        "Errors found early (in requirements or design) are 10–100x cheaper to fix than "
        "errors found after coding is complete.",
        bg=C_LORG, border=C_ORANGE
    ))

    # ── 1.2 Quality ──────────────────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("1.2  Quality"))
    s.append(hr())
    s.append(p(
        "In everyday life, we say something is 'good quality' when it meets our expectations. "
        "In software, <b>Quality</b> has a precise meaning:"
    ))
    s.append(definition_box("Software Quality",
        "The degree to which a software product satisfies stated and implied requirements, "
        "is free from defects, and meets the needs of the user in a reliable, efficient, "
        "and usable manner.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(h3("Quality Dimensions (ISO 9126)"))
    s += bullets([
        "<b>Functionality:</b> Does it do what it is supposed to do?",
        "<b>Reliability:</b> Does it work consistently without failures?",
        "<b>Usability:</b> Is it easy to use and understand?",
        "<b>Efficiency:</b> Does it use resources (CPU, memory) wisely?",
        "<b>Maintainability:</b> Is it easy to fix and modify?",
        "<b>Portability:</b> Can it run on different platforms/environments?",
    ])
    s.append(spacer(8))
    s.append(h3("Cost of Quality"))
    s.append(p(
        "Quality is not free, but neither is the lack of it. The <b>Cost of Quality</b> "
        "consists of two parts:"
    ))
    rows = [
        ("<b>Cost of Conformance</b> (doing it right)", "Prevention costs (training, process improvement), Appraisal costs (reviews, testing)"),
        ("<b>Cost of Non-Conformance</b> (fixing failures)", "Internal failure costs (rework, re-testing), External failure costs (customer complaints, recalls, loss of reputation)"),
    ]
    s.append(two_col_table(rows, headers=["Cost Type", "Examples"]))

    # ── 1.3 QA and QC ───────────────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("1.3  Quality Assurance (QA) and Quality Control (QC)"))
    s.append(hr())
    s.append(p(
        "These two terms are often confused. Let's understand both clearly."
    ))

    s.append(h3("Quality Assurance (QA)"))
    s.append(definition_box("QA Definition",
        "QA is a PROCESS-oriented activity. It ensures that the processes used to develop "
        "software are correct and will produce a quality product. QA is about PREVENTING defects.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(6))
    s += bullets([
        "QA is proactive — it catches problems BEFORE they cause defects.",
        "QA focuses on HOW the work is done (processes, standards, procedures).",
        "Examples: Code review guidelines, process audits, walkthroughs, inspections.",
        "QA involves the entire development team, not just testers.",
    ])

    s.append(spacer(8))
    s.append(h3("Quality Control (QC)"))
    s.append(definition_box("QC Definition",
        "QC is a PRODUCT-oriented activity. It involves actually examining the product "
        "(software) to find defects in the finished or partially finished product. "
        "QC is about DETECTING defects.",
        bg=C_LPURP, border=C_PURPLE))
    s.append(spacer(6))
    s += bullets([
        "QC is reactive — it finds defects AFTER they have occurred.",
        "QC focuses on WHAT was built (the actual product).",
        "Examples: Testing, code inspection, debugging.",
        "QC is primarily the responsibility of the testing team.",
    ])

    s.append(spacer(8))
    comparison_rows = [
        ("Orientation", "Process-oriented", "Product-oriented"),
        ("Goal", "Prevent defects", "Detect defects"),
        ("Approach", "Proactive", "Reactive"),
        ("Focus", "HOW work is done", "WHAT was built"),
        ("Responsibility", "Entire team", "Testing team"),
        ("Examples", "Process audits, reviews, standards", "Testing, inspection, debugging"),
    ]
    data = [[Paragraph("<b>Aspect</b>", S["BodyBold"]),
             Paragraph("<b>QA</b>", S["BodyBold"]),
             Paragraph("<b>QC</b>", S["BodyBold"])]]
    for row in comparison_rows:
        data.append([Paragraph(c, S["Body"]) for c in row])
    w = PAGE_W - 2*MARGIN - 4
    tbl = Table(data, colWidths=[w*0.3, w*0.35, w*0.35])
    tbl.setStyle(TableStyle([
        ("GRID",         (0,0),(-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("BACKGROUND",   (0,0),(-1,0),  C_NAVY),
        ("TEXTCOLOR",    (0,0),(-1,0),  C_WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[C_WHITE, C_LGREY]),
        ("LEFTPADDING",  (0,0),(-1,-1), 8),
        ("RIGHTPADDING", (0,0),(-1,-1), 8),
        ("TOPPADDING",   (0,0),(-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(tbl)

    # ── 1.4 Testing ──────────────────────────────────────────────────────────
    s.append(spacer(14))
    s.append(h1("1.4  Testing: What, Why, and Goals"))
    s.append(hr())
    s.append(definition_box("Software Testing",
        "Software Testing is the process of EXECUTING a program or system with the INTENT "
        "of FINDING ERRORS. It is a planned, structured activity to evaluate whether the "
        "software meets specified requirements and to identify any defects.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))

    s.append(h3("Why Do We Test?"))
    s += bullets([
        "To find bugs/defects before the software reaches the customer.",
        "To verify that the software meets business requirements.",
        "To gain confidence that the software works correctly.",
        "To prevent defects from reaching production (expensive to fix later).",
        "To ensure reliability, security, and performance of the software.",
        "To meet legal, regulatory, or contractual requirements.",
    ])

    s.append(spacer(8))
    s.append(h3("Seven Principles of Software Testing"))
    s.append(p("These 7 principles guide every professional tester:"))
    principles = [
        ("1. Testing shows presence of bugs",
         "Testing can prove that bugs exist, but it CANNOT prove that a program is completely bug-free."),
        ("2. Exhaustive testing is impossible",
         "You cannot test every possible input, path, or combination. Testers must prioritize using risk and importance."),
        ("3. Early testing",
         "Testing should start as early as possible in the SDLC — reviewing requirements catches defects cheapest."),
        ("4. Defect clustering",
         "A small number of modules usually contain most of the defects (80-20 rule / Pareto principle)."),
        ("5. Pesticide paradox",
         "Running the same tests again and again stops finding new bugs. Tests must be reviewed and updated regularly."),
        ("6. Testing is context dependent",
         "Different applications need different testing — a banking app needs more security testing than a simple game."),
        ("7. Absence-of-errors fallacy",
         "Finding and fixing bugs doesn't help if the software doesn't meet user needs. Building the wrong thing bug-free is still wrong."),
    ]
    for title, desc in principles:
        s.append(definition_box(title, desc, bg=C_LGREY, border=C_BLUE))
        s.append(spacer(4))

    # ── 1.5 Verification & Validation ───────────────────────────────────────
    s.append(spacer(14))
    s.append(h1("1.5  Verification and Validation (V&V)"))
    s.append(hr())
    s.append(p(
        "These two concepts sound similar but have very different meanings. "
        "A simple way to remember: Verification = building the product RIGHT. "
        "Validation = building the RIGHT product."
    ))

    s.append(h3("Verification"))
    s.append(definition_box("Verification",
        "Are we building the product RIGHT? Verification ensures that the software correctly "
        "implements a specific function or design. It checks that the product conforms to its "
        "specification. It is a STATIC activity — no code needs to run.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(6))
    s += bullets([
        "Done through reviews, walkthroughs, inspections, and audits.",
        "Asks: Does this document / design / code match the specifications?",
        "Examples: Reviewing requirements documents, inspecting design diagrams, code reviews.",
        "Can catch errors in design BEFORE coding even starts.",
    ])

    s.append(spacer(8))
    s.append(h3("Validation"))
    s.append(definition_box("Validation",
        "Are we building the RIGHT product? Validation checks that the final software meets "
        "the customer's actual needs. It is a DYNAMIC activity — involves running the software.",
        bg=C_LPURP, border=C_PURPLE))
    s.append(spacer(6))
    s += bullets([
        "Done through actual testing — running the software and observing behavior.",
        "Asks: Does this software actually do what the user needs?",
        "Examples: System testing, user acceptance testing.",
        "Happens later in the SDLC.",
    ])

    s.append(spacer(8))
    s.append(info_box(
        "<b>Easy Memory Trick:</b>  Verification = Review documents (Are we following the spec?). "
        "Validation = Run the software (Does the customer love it?).",
        bg=C_LORG, border=C_ORANGE
    ))

    # ── 1.6 Process Models ───────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("1.6  Process Models"))
    s.append(hr())
    s.append(p(
        "A <b>Process Model</b> (also called a Software Development Process or methodology) "
        "defines the sequence and manner in which software development activities are organized. "
        "Think of it as a 'blueprint' for how to run a software project."
    ))

    s.append(h3("Why Do We Need Process Models?"))
    s += bullets([
        "To bring structure and order to complex development activities.",
        "To make progress measurable and manageable.",
        "To ensure all required activities are done and not skipped.",
        "To enable team collaboration and communication.",
        "To support planning, estimation, and scheduling.",
    ])

    # ── 1.7 Life Cycle Models ────────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("1.7  Life Cycle Models"))
    s.append(hr())

    # Waterfall
    s.append(h2("1.7.1  Waterfall Model"))
    s.append(p(
        "The Waterfall Model is the oldest and most straightforward SDLC model. "
        "It is a <b>linear sequential</b> model where each phase must be completed "
        "before the next begins — like water flowing down a waterfall, you cannot go back up."
    ))
    s.append(h3("Phases (in order):"))
    s += numbered([
        "Requirements → 2. System Design → 3. Implementation → 4. Testing → 5. Deployment → 6. Maintenance"
    ])
    s.append(h3("Advantages:"))
    s += bullets([
        "Simple and easy to understand and manage.",
        "Phases are clearly defined with distinct deliverables.",
        "Good for small projects with well-understood requirements.",
        "Documentation is thorough at each stage.",
    ])
    s.append(h3("Disadvantages:"))
    s += bullets([
        "Requirements must be known completely upfront — not realistic for most projects.",
        "Testing happens very late — bugs found late are expensive to fix.",
        "No working software is produced until late in the cycle.",
        "Cannot easily accommodate changes once a phase is done.",
        "Poor model for large, complex, or research-oriented projects.",
    ])

    # V-Model
    s.append(spacer(10))
    s.append(h2("1.7.2  V-Model (Verification and Validation Model)"))
    s.append(p(
        "The V-Model is an extension of the Waterfall model. Instead of moving only "
        "downward, it forms a V-shape. The LEFT side represents development phases "
        "and the RIGHT side represents corresponding testing phases. "
        "Each development phase has a <b>corresponding testing phase</b> opposite it."
    ))
    s.append(h3("V-Model Structure:"))
    s.append(info_box(
        "Requirements Analysis ↔ Acceptance Testing  |  "
        "System Design ↔ System Testing  |  "
        "Architecture Design ↔ Integration Testing  |  "
        "Module Design ↔ Unit Testing  |  "
        "[CODING at the bottom of the V]",
        bg=C_LGREY, border=C_GREY
    ))
    s.append(h3("Key Feature:"))
    s += bullets([
        "Testing planning starts from the very beginning alongside development.",
        "Every development phase has a directly corresponding test phase.",
        "Emphasizes verification on the left and validation on the right.",
    ])
    s.append(h3("Advantages:"))
    s += bullets([
        "Testing is planned early — reduces cost of finding defects.",
        "High chance of success for small to medium projects.",
        "Clear, structured phases — easy to manage.",
    ])
    s.append(h3("Disadvantages:"))
    s += bullets([
        "Still rigid like Waterfall — hard to go back and make changes.",
        "No working prototype is produced early.",
        "Not suitable for changing or unclear requirements.",
    ])

    # Spiral
    s.append(spacer(10))
    s.append(h2("1.7.3  Spiral Model"))
    s.append(p(
        "The Spiral Model combines the iterative nature of prototyping with the systematic "
        "aspects of the Waterfall model. It is <b>risk-driven</b> — the project goes through "
        "multiple loops (spirals), and in each loop, risks are identified and managed."
    ))
    s.append(h3("Each Spiral Loop Has 4 Quadrants:"))
    s += numbered([
        "<b>Planning:</b> Define objectives, alternatives, and constraints.",
        "<b>Risk Analysis:</b> Identify and analyze risks, create prototypes.",
        "<b>Engineering:</b> Develop and test the product for this iteration.",
        "<b>Evaluation:</b> Customer evaluates, feedback taken, plan next spiral.",
    ])
    s.append(h3("Advantages:"))
    s += bullets([
        "Best for large, high-risk projects.",
        "Risk management is built into the process.",
        "Customer sees working software early through prototypes.",
        "Flexible — requirements can change between spirals.",
    ])
    s.append(h3("Disadvantages:"))
    s += bullets([
        "Complex and costly to manage.",
        "Risk analysis requires highly skilled experts.",
        "Not suitable for small or low-risk projects.",
    ])

    # Agile
    s.append(spacer(10))
    s.append(h2("1.7.4  Agile Model"))
    s.append(p(
        "Agile is a modern, flexible, <b>iterative and incremental</b> approach to software development. "
        "Instead of one big release, software is built in small chunks called <b>sprints</b> "
        "(usually 2–4 weeks). After each sprint, working software is delivered."
    ))
    s.append(h3("Core Agile Values (Agile Manifesto):"))
    s += bullets([
        "Individuals and interactions OVER processes and tools.",
        "Working software OVER comprehensive documentation.",
        "Customer collaboration OVER contract negotiation.",
        "Responding to change OVER following a plan.",
    ])
    s.append(h3("Key Practices:"))
    s += bullets([
        "<b>Daily Standups:</b> Short 15-min meetings — what did I do, what will I do, any blockers?",
        "<b>Sprints:</b> Time-boxed development cycles (2-4 weeks).",
        "<b>Sprint Review:</b> Demonstrate working software to stakeholders.",
        "<b>Sprint Retrospective:</b> Team reflects on how to improve.",
        "<b>Continuous Testing:</b> Testing happens in every sprint.",
    ])
    s.append(h3("Advantages:"))
    s += bullets([
        "Highly flexible — requirements can change at any sprint.",
        "Customer satisfaction through frequent delivery.",
        "Defects found early in each sprint.",
        "Better team collaboration and communication.",
    ])
    s.append(h3("Disadvantages:"))
    s += bullets([
        "Hard to predict total cost and timeline upfront.",
        "Requires experienced team members.",
        "Documentation may be insufficient.",
        "Scope creep is a risk if not managed well.",
    ])

    # ── 1.8 STLC ──────────────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("1.8  Software Testing Life Cycle (STLC)"))
    s.append(hr())
    s.append(p(
        "Just as software development has a life cycle (SDLC), testing itself also follows "
        "a structured life cycle called the <b>Software Testing Life Cycle (STLC)</b>. "
        "STLC defines what testing activities to do and in what order."
    ))

    stlc_phases = [
        ("Phase 1: Requirement Analysis",
         "Testers review requirements documents to understand what needs to be tested. "
         "They identify testable and non-testable requirements. Questions are raised with "
         "the business analysts if requirements are unclear.",
         ["Entry: Requirements document available", "Exit: List of testable requirements, RTM (Requirement Traceability Matrix)"]),
        ("Phase 2: Test Planning",
         "The Test Manager/Lead creates the Test Plan document. This covers: what to test, "
         "who will test, when to test, how to test, what tools to use, what risks exist, "
         "and the test schedule.",
         ["Entry: Requirements document, RTM", "Exit: Test Plan document, effort estimates"]),
        ("Phase 3: Test Case Development",
         "Testers write detailed Test Cases — step-by-step instructions for what to test, "
         "what input to give, and what the expected output is. Test data is also prepared.",
         ["Entry: Test Plan, requirements", "Exit: Test cases, test scripts, test data"]),
        ("Phase 4: Test Environment Setup",
         "The testing environment (hardware, software, network, databases) is set up and "
         "made ready. A smoke test is done to ensure the build is stable enough to test.",
         ["Entry: System design, architecture documents", "Exit: Test environment ready, smoke test passed"]),
        ("Phase 5: Test Execution",
         "Testers actually RUN the test cases. Results (Pass/Fail) are recorded. "
         "Any failures lead to defect reports being raised in a bug tracking tool.",
         ["Entry: Test cases ready, environment ready, build received", "Exit: Test execution report, defect reports"]),
        ("Phase 6: Test Cycle Closure",
         "Testing is complete. Metrics are analyzed (defects found, test coverage, pass rate). "
         "Lessons learned are documented for future projects.",
         ["Entry: Testing complete", "Exit: Test closure report, test metrics"]),
    ]

    for title, desc, criteria in stlc_phases:
        s.append(h3(title))
        s.append(p(desc))
        s += bullets([criteria[0], criteria[1]], style="Bullet2")
        s.append(spacer(6))

    # ── 1.9 Static Testing ───────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("1.9  Static Testing"))
    s.append(hr())
    s.append(definition_box("Static Testing",
        "Static testing is a type of software testing where the software code, requirements, "
        "or design documents are examined WITHOUT actually executing the code. "
        "It is a QA activity used to find defects early.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "In static testing, humans READ and EXAMINE the artifacts (documents, code) to find "
        "problems. No software is run. This is why it is called 'static' — nothing moves."
    ))

    s.append(h3("Types of Static Testing"))
    s.append(h4("A) Reviews"))
    s.append(p("A review is when one or more people examine a document, code, or design to find defects."))
    review_types = [
        ("Informal Review", "No formal process. A colleague simply reads your work and gives feedback. Quick and cheap."),
        ("Walkthrough", "The author leads the review. Author explains the work step-by-step to reviewers. Goal is to educate reviewers and get suggestions."),
        ("Technical Review", "Structured meeting with trained reviewers. Moderator leads. Defects are documented formally. No management present."),
        ("Inspection", "Most formal type. Led by a trained moderator. Uses defined entry/exit criteria, checklists, and formal defect logging. Metrics collected."),
    ]
    for rtype, rdesc in review_types:
        s.append(definition_box(rtype, rdesc, bg=C_LGREY, border=C_BLUE))
        s.append(spacer(4))

    s.append(h4("B) Static Analysis"))
    s.append(p(
        "Static analysis involves using <b>automated tools</b> to analyze source code "
        "WITHOUT executing it. Tools look for potential errors, style violations, and "
        "security vulnerabilities."
    ))
    s += bullets([
        "<b>Linters:</b> Check for code style and formatting issues (e.g., ESLint for JavaScript).",
        "<b>Code Analyzers:</b> Find potential bugs — null pointer dereferences, division by zero (e.g., SonarQube, FindBugs).",
        "<b>Security Scanners:</b> Find security vulnerabilities in code.",
        "<b>Complexity Analyzers:</b> Measure cyclomatic complexity to find overly complex code.",
    ])

    s.append(h3("Benefits of Static Testing"))
    s += bullets([
        "Finds defects early — cheaper to fix than defects found in testing or production.",
        "Does not require executable code — can start from day 1.",
        "Improves code quality, readability, and maintainability.",
        "Reduces testing effort later in the project.",
        "Can detect defects that dynamic testing might miss (e.g., security issues in code logic).",
    ])

    # ── 1.10 White Box Testing (Structural Testing) ──────────────────────────
    s.append(PageBreak())
    s.append(h1("1.10  White Box Testing (Structural / Glass Box Testing)"))
    s.append(hr())
    s.append(definition_box("White Box Testing",
        "White Box Testing (also called Structural Testing, Clear Box Testing, or Glass Box Testing) "
        "is a testing technique where the tester has full knowledge of and access to the "
        "INTERNAL structure, code, logic, and implementation of the software being tested.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "Think of it this way: In Black Box Testing, the tester sees only inputs and outputs "
        "— like looking at a black box from outside. In <b>White Box Testing</b>, the box "
        "is transparent (like glass) — the tester can see all the internal code and logic."
    ))

    s.append(h3("Goals of White Box Testing"))
    s += bullets([
        "Ensure all code paths are tested (code coverage).",
        "Find errors in internal logic and algorithms.",
        "Validate loops, conditions, and branching logic.",
        "Check security holes and backdoors in code.",
        "Verify that all branches of decision points are tested.",
    ])

    s.append(h3("White Box Testing Techniques"))
    s.append(h4("1. Statement Coverage"))
    s.append(p(
        "Ensures that every line (statement) of source code is executed at least once "
        "during testing."
    ))
    s.append(info_box(
        "<b>Formula:</b>  Statement Coverage % = (Number of statements executed / Total statements) × 100"
    ))
    s += bullets([
        "Simplest form of coverage.",
        "Does NOT guarantee all branches are tested.",
        "Example: If an IF statement has two branches, executing only one branch still covers the statement.",
    ])

    s.append(h4("2. Branch / Decision Coverage"))
    s.append(p(
        "Ensures that every possible outcome (TRUE and FALSE) of every decision/branch "
        "point in the code is tested."
    ))
    s.append(info_box(
        "<b>Formula:</b>  Branch Coverage % = (Number of branches executed / Total branches) × 100"
    ))
    s += bullets([
        "Stronger than statement coverage.",
        "For every IF-ELSE, both the IF path AND the ELSE path must be tested.",
        "Guarantees statement coverage as a byproduct.",
    ])

    s.append(h4("3. Path Coverage"))
    s.append(p(
        "Ensures that every possible path through the code (every unique sequence of "
        "statements from start to end) is tested."
    ))
    s += bullets([
        "Most thorough but also most complex and expensive.",
        "Number of paths can be enormous in complex programs.",
        "Guarantees both branch and statement coverage.",
    ])

    s.append(h4("4. Condition Coverage"))
    s.append(p(
        "Ensures that each individual boolean sub-expression within a compound condition "
        "is evaluated to both TRUE and FALSE at least once."
    ))
    s.append(info_box(
        "<b>Example:</b>  if (A AND B) — Condition coverage requires testing A=True, A=False, B=True, B=False separately.",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h4("5. Cyclomatic Complexity"))
    s.append(p(
        "A metric that measures the complexity of a program by counting the number of "
        "linearly independent paths through the code."
    ))
    s.append(info_box(
        "<b>Formula:</b>  Cyclomatic Complexity (CC) = E − N + 2P  "
        "(E = edges in flow graph, N = nodes, P = connected components). "
        "For simple programs: CC = Number of decision points + 1. "
        "Lower CC = simpler code. CC > 10 indicates high complexity.",
        bg=C_LBLUE, border=C_BLUE
    ))

    s.append(h3("Basis Path Testing"))
    s.append(p(
        "Basis Path Testing is a White Box technique developed by Tom McCabe. "
        "It uses Cyclomatic Complexity to determine the minimum number of test cases "
        "needed to cover all paths in a program."
    ))
    s += numbered([
        "Draw the Control Flow Graph (CFG) of the code.",
        "Calculate Cyclomatic Complexity (CC) = number of independent paths.",
        "Create test cases for each independent path.",
        "Execute all test cases and verify results.",
    ])

    s.append(h3("Loop Testing"))
    s.append(p(
        "Loops are a common source of errors. White Box testing specifically targets loops."
    ))
    s += bullets([
        "<b>Simple Loops:</b> Test with 0 iterations (skip loop), 1 iteration, 2 iterations, maximum iterations, and maximum + 1.",
        "<b>Nested Loops:</b> Hold outer loops at minimum, test inner loop. Then increment outer and test again.",
        "<b>Concatenated Loops:</b> Test each loop independently if they are independent.",
    ])

    # ── 1.11 Challenges in WBT ───────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("1.11  Challenges in White Box Testing"))
    s.append(hr())
    s.append(p(
        "While White Box Testing is powerful, it comes with significant challenges "
        "that testers must understand:"
    ))
    challenges = [
        ("Explosion of Paths",
         "Even small programs can have millions of possible paths. Testing every single path "
         "is practically impossible. For a program with just 10 IF statements, there could "
         "be over 1000 paths."),
        ("Tester Must Know the Code",
         "WBT requires deep programming knowledge. Testers need to read, understand, and "
         "analyze source code — this is a specialized skill not all testers have."),
        ("Cannot Find Missing Functionality",
         "WBT tests what the code DOES, but it cannot tell you if the code is MISSING "
         "something. If a feature was never coded, WBT will never find it."),
        ("Test Case Maintenance",
         "When code changes, all the test cases based on that code need to be updated. "
         "This is a heavy maintenance burden."),
        ("Tools Required",
         "To achieve proper code coverage, specialized tools are needed (e.g., JaCoCo for Java, "
         "Istanbul for JavaScript). These add cost and learning curve."),
        ("Impossible to Achieve 100% Path Coverage",
         "Full path coverage is theoretically possible but practically infeasible for most "
         "real-world programs due to the exponential growth of paths."),
        ("Does Not Reflect User Perspective",
         "WBT tests internal logic but does not verify whether the software actually "
         "meets user expectations and requirements."),
    ]
    for title, desc in challenges:
        s.append(definition_box(title, desc, bg=C_LORG, border=C_ORANGE))
        s.append(spacer(4))

    # ── 1.12 Black Box Testing ───────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("1.12  Black Box Testing"))
    s.append(hr())
    s.append(definition_box("Black Box Testing",
        "Black Box Testing is a testing technique where the tester has NO knowledge of the "
        "internal structure, code, or implementation of the software. The tester only knows "
        "the INPUTS and the expected OUTPUTS based on requirements.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "The software is treated as a 'black box' — you put in inputs and check if the "
        "outputs are correct. You don't care HOW it works inside, only WHAT it does."
    ))

    s.append(h3("Black Box Testing Techniques"))
    s.append(h4("1. Equivalence Partitioning (EP)"))
    s.append(p(
        "Divide all possible input values into groups (partitions) where each group "
        "is expected to be treated the same way by the software. "
        "Test one value from each partition — if it passes for one, it should pass for all in that partition."
    ))
    s.append(info_box(
        "<b>Example:</b>  A form accepts age between 18 and 65. "
        "Valid partition: 18–65 (test with e.g. 30). "
        "Invalid partition 1: less than 18 (test with e.g. 10). "
        "Invalid partition 2: greater than 65 (test with e.g. 80).",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h4("2. Boundary Value Analysis (BVA)"))
    s.append(p(
        "Errors tend to cluster at the boundaries of input partitions. BVA tests values "
        "AT and just beyond the boundary. For a valid range of 18–65:"
    ))
    s += bullets([
        "Test at lower boundary: 18 (valid), 17 (invalid), 19 (valid)",
        "Test at upper boundary: 65 (valid), 66 (invalid), 64 (valid)",
        "BVA is one of the most effective and commonly used BBT techniques.",
    ])

    s.append(h4("3. Decision Table Testing"))
    s.append(p(
        "Used when the system's behavior depends on MULTIPLE conditions. "
        "A decision table lists all combinations of conditions and their expected actions."
    ))
    s.append(info_box(
        "<b>Structure:</b>  Rows = Conditions (e.g., User logged in? Has subscription? Owns content?). "
        "Columns = Different combinations. Cells = Y/N for conditions, Action for results.",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h4("4. State Transition Testing"))
    s.append(p(
        "Used for systems that can be in different STATES and transition between them based "
        "on inputs. A state transition diagram maps all states and transitions."
    ))
    s.append(info_box(
        "<b>Example:</b>  ATM Machine states: Idle → Card Inserted → PIN Entered → "
        "Transaction Selected → Processing → Complete → Idle. "
        "Test each transition and invalid transitions.",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h4("5. Use Case Testing"))
    s.append(p(
        "Test cases are designed based on use cases — descriptions of how users interact "
        "with the system to achieve goals. Each use case scenario becomes a test case."
    ))

    s.append(h3("Black Box Testing Process"))
    s.append(p("The process of Black Box Testing follows these steps:"))
    bbtest_steps = [
        ("Step 1: Understand Requirements",
         "Thoroughly read and understand the software requirements and specifications. "
         "Know what the software is supposed to do."),
        ("Step 2: Identify Test Inputs",
         "Based on requirements, identify valid inputs, invalid inputs, and boundary inputs. "
         "Use EP, BVA, and other techniques."),
        ("Step 3: Determine Expected Outputs",
         "For each input or set of inputs, determine what the correct expected output "
         "should be according to requirements."),
        ("Step 4: Write Test Cases",
         "Document test cases with Test ID, description, input, steps, expected result, "
         "and actual result fields."),
        ("Step 5: Execute Test Cases",
         "Run the software with the specified inputs. Observe and record the actual outputs."),
        ("Step 6: Compare Expected vs Actual",
         "If actual output matches expected output → PASS. If not → FAIL. Log defect."),
        ("Step 7: Report Defects",
         "All failures are logged as defects in a bug tracking tool with full details "
         "for developers to investigate and fix."),
        ("Step 8: Retest (Regression Testing)",
         "After developers fix bugs, retest those specific cases. Also run regression tests "
         "to ensure fixes didn't break other things."),
    ]
    for title, desc in bbtest_steps:
        s.append(definition_box(title, desc, bg=C_LGREY, border=C_BLUE))
        s.append(spacer(4))

    s.append(h3("Advantages of Black Box Testing"))
    s += bullets([
        "Tester does NOT need to know programming or internal code.",
        "Tests from the user's perspective — validates what the customer actually sees.",
        "Can find defects that White Box Testing misses (missing features).",
        "Unbiased testing — tester has no preconceptions about the code.",
        "Applicable at all testing levels — unit, integration, system, acceptance.",
    ])

    s.append(h3("Disadvantages of Black Box Testing"))
    s += bullets([
        "Cannot achieve complete coverage — impossible to test all input combinations.",
        "Test case design can be time-consuming without internal knowledge.",
        "Some code paths may never be tested.",
        "Cannot directly test internal logic, algorithms, or data structures.",
    ])

    return s


# ═══════════════════════════════════════════════════════════════════════════
# UNIT II
# ═══════════════════════════════════════════════════════════════════════════
def unit2():
    s = []
    s.append(PageBreak())
    s.append(unit_banner(2, "Integration Testing",
        "Definition · Top-Down · Bottom-Up · Bi-Directional · System Integration · "
        "Scenario Testing · Defect Bash"))
    s.append(spacer(16))

    s.append(h1("2.1  What is Integration Testing?"))
    s.append(hr())
    s.append(definition_box("Integration Testing",
        "Integration Testing is a level of software testing where individual units or "
        "components (already tested by Unit Testing) are COMBINED and tested as a group. "
        "The goal is to find defects in the INTERACTION and INTERFACES between components.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "Imagine you are building a car. You test each part individually — engine works, "
        "brakes work, steering works. But when you assemble them together, you need to test "
        "that they work TOGETHER correctly. That is integration testing."
    ))

    s.append(h3("Why is Integration Testing Needed?"))
    s += bullets([
        "Individual modules may work perfectly alone but fail when combined.",
        "Data passed between modules may be incorrect or in wrong format.",
        "Interface mismatches — one module expects different data than another provides.",
        "Error handling between modules may be incomplete.",
        "Timing and sequencing issues may only appear when modules interact.",
        "Third-party integrations and external APIs need to be verified.",
    ])

    s.append(h3("Types of Defects Found in Integration Testing"))
    s += bullets([
        "<b>Interface Defects:</b> Wrong data type, wrong number of parameters passed.",
        "<b>Data Format Errors:</b> Date formatted as DD/MM/YYYY but module expects MM/DD/YYYY.",
        "<b>Timing Issues:</b> Module B is called before Module A has finished processing.",
        "<b>Missing Error Handling:</b> Module A crashes when Module B returns null.",
        "<b>Integration Assumption Errors:</b> Different teams had different assumptions about interfaces.",
    ])

    # ── 2.2 Top-Down Integration ─────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.2  Top-Down Integration Testing"))
    s.append(hr())
    s.append(definition_box("Top-Down Integration",
        "In Top-Down Integration, testing begins with the TOP-LEVEL module (main module) "
        "and progressively integrates and tests LOWER-LEVEL modules. "
        "Modules that have not yet been developed are replaced by STUBS.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(definition_box("STUB",
        "A STUB is a dummy module that simulates the behavior of a lower-level module "
        "that has not yet been integrated. It typically returns hard-coded values and "
        "does not contain real business logic.",
        bg=C_LPURP, border=C_PURPLE))

    s.append(spacer(8))
    s.append(h3("How Top-Down Integration Works"))
    s += numbered([
        "Start with the main/top module. Test it alone (lower modules replaced by stubs).",
        "Replace one stub at a time with the actual lower-level module.",
        "Test after each replacement to verify the integration.",
        "Repeat until all modules are integrated from top to bottom.",
    ])

    s.append(h3("Types of Top-Down Integration"))
    s += bullets([
        "<b>Depth-First:</b> Integrate all modules along one branch of the hierarchy completely before moving to the next branch.",
        "<b>Breadth-First:</b> Integrate all modules at one level before moving down to the next level.",
    ])

    s.append(h3("Advantages"))
    s += bullets([
        "Major design flaws and architectural problems are found early.",
        "The overall control flow and system behavior can be verified early.",
        "Working prototype is available early — useful for demos and stakeholder review.",
        "No need for drivers (test controllers) — the real top module is used.",
    ])

    s.append(h3("Disadvantages"))
    s += bullets([
        "Stubs must be written — takes time and effort.",
        "Lower-level modules (which often have complex logic) are tested late.",
        "Data flowing upward through the hierarchy is hard to represent in stubs.",
        "Many stubs may be needed, making testing complicated.",
    ])

    # ── 2.3 Bottom-Up Integration ────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.3  Bottom-Up Integration Testing"))
    s.append(hr())
    s.append(definition_box("Bottom-Up Integration",
        "In Bottom-Up Integration, testing starts with the LOWEST-LEVEL modules (leaves "
        "of the module hierarchy) and progressively integrates upward. "
        "Higher-level modules that don't exist yet are replaced by DRIVERS.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(definition_box("DRIVER",
        "A DRIVER is a dummy module that calls the module under test and provides "
        "it with test inputs. It simulates the behavior of a higher-level module "
        "that hasn't been integrated yet.",
        bg=C_LPURP, border=C_PURPLE))

    s.append(spacer(8))
    s.append(h3("How Bottom-Up Integration Works"))
    s += numbered([
        "Start with the lowest-level modules (no dependencies). Test each one using drivers.",
        "Group low-level modules that are needed by a higher-level module.",
        "Replace the driver with the actual higher-level module when it is ready.",
        "Test the cluster after each integration.",
        "Repeat moving upward until all modules are integrated.",
    ])

    s.append(h3("Advantages"))
    s += bullets([
        "Lower-level utility modules are tested thoroughly and early.",
        "No need for stubs — the real lower modules are always used.",
        "Easier to develop drivers than stubs (drivers just call the module).",
        "Good for systems where lower-level modules are the most critical.",
    ])

    s.append(h3("Disadvantages"))
    s += bullets([
        "No working prototype of the full system until integration is nearly complete.",
        "High-level design flaws are found late in the process.",
        "Drivers must be written — extra effort.",
        "Top-level control flow cannot be tested until late stages.",
    ])

    # ── 2.4 Bi-Directional / Sandwich Integration ────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.4  Bi-Directional Integration (Sandwich Integration)"))
    s.append(hr())
    s.append(definition_box("Bi-Directional / Sandwich Integration",
        "Bi-Directional Integration (also called Sandwich or Hybrid Integration) combines "
        "BOTH Top-Down and Bottom-Up approaches simultaneously. The top layers are tested "
        "top-down using stubs, while the bottom layers are tested bottom-up using drivers. "
        "They meet in the middle.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "Think of it as a sandwich: the top bread (top-down) and the bottom bread (bottom-up) "
        "come together to form the complete sandwich (integrated system)."
    ))

    s.append(h3("How It Works"))
    s += bullets([
        "Divide the module hierarchy into three layers: Top, Middle, Bottom.",
        "Top layer is tested using Top-Down approach with stubs for middle layer.",
        "Bottom layer is tested using Bottom-Up approach with drivers for middle layer.",
        "Middle layer is tested last, integrating the top and bottom.",
    ])

    s.append(h3("Advantages"))
    s += bullets([
        "Combines the benefits of both Top-Down and Bottom-Up.",
        "Allows parallel testing by different teams simultaneously.",
        "Better suited for large, complex systems.",
        "Reduces overall integration time.",
    ])

    s.append(h3("Disadvantages"))
    s += bullets([
        "Most complex integration strategy — requires careful coordination.",
        "Both stubs AND drivers need to be written.",
        "Middle layer testing can be complicated.",
        "Requires more resources and personnel.",
    ])

    # ── 2.5 System Integration ───────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.5  System Integration Testing"))
    s.append(hr())
    s.append(definition_box("System Integration Testing (SIT)",
        "System Integration Testing verifies the integration of the complete software system "
        "with EXTERNAL systems, hardware components, third-party services, databases, and "
        "network infrastructure — the entire ecosystem in which the software will operate.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "While module integration testing checks how internal components work together, "
        "System Integration Testing checks how the complete software interacts with its "
        "EXTERNAL environment."
    ))

    s.append(h3("What is Tested in System Integration?"))
    s += bullets([
        "<b>External APIs and Services:</b> Payment gateways, SMS services, email servers.",
        "<b>Database Integration:</b> Correct data is written to and read from databases.",
        "<b>Hardware Integration:</b> Software correctly interfaces with hardware devices.",
        "<b>Legacy System Integration:</b> New software works with old existing systems.",
        "<b>Third-Party Components:</b> Libraries, frameworks, and vendor software.",
        "<b>Network Communication:</b> Data is correctly transmitted over networks.",
    ])

    s.append(h3("Challenges in System Integration Testing"))
    s += bullets([
        "External systems may not always be available for testing.",
        "Test data in external systems may be limited or restricted.",
        "External systems may change their APIs without notice.",
        "Complex environments are hard to replicate in test settings.",
        "Vendor support may be needed to resolve integration issues.",
    ])

    # ── 2.6 Choosing Integration Method ─────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.6  Choosing the Right Integration Method"))
    s.append(hr())
    s.append(p(
        "There is no one-size-fits-all answer. The best integration method depends on "
        "several factors:"
    ))
    choice_rows = [
        ("Project Architecture", "Hierarchical → Top-Down. Layered with critical lower modules → Bottom-Up."),
        ("Available Resources", "Limited team → simpler approach like Big Bang (caution!) or one-directional."),
        ("Risk Profile", "High-level design risk → Top-Down. Critical utility modules → Bottom-Up."),
        ("Project Size", "Large projects → Sandwich/Bi-Directional to enable parallel work."),
        ("Module Availability", "Top modules ready first → Top-Down. Bottom modules ready first → Bottom-Up."),
        ("Time Constraints", "Tight deadline → Bi-Directional to parallelize testing."),
        ("Prototype Needed Early", "Customer needs early demo → Top-Down (working UI prototype early)."),
    ]
    s.append(two_col_table(choice_rows, headers=["Factor", "Recommended Approach"], col_ratio=(0.3, 0.7)))

    s.append(spacer(8))
    s.append(info_box(
        "<b>Big Bang Integration (NOT Recommended):</b>  All modules are integrated at once "
        "and tested as a complete system. Simple but risky — when failures occur, it's "
        "very hard to locate the source of the defect. Only suitable for very small, "
        "simple systems.",
        bg=C_LORG, border=C_ORANGE
    ))

    # ── 2.7 Integration as a Phase ───────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.7  Integration Testing as a Phase of Testing"))
    s.append(hr())
    s.append(p(
        "Integration testing is one of the four main LEVELS of testing in the testing hierarchy. "
        "Understanding where it fits in the overall testing process is important."
    ))

    levels = [
        ("Level 1: Unit Testing", "Tests individual functions, methods, or classes in isolation.", "Developers"),
        ("Level 2: Integration Testing", "Tests interaction between combined modules/components.", "Developers + Testers"),
        ("Level 3: System Testing", "Tests the complete, fully integrated system.", "Testing Team"),
        ("Level 4: Acceptance Testing", "Tests whether the system meets business/user requirements.", "Users + Business"),
    ]
    w = PAGE_W - 2*MARGIN - 4
    data = [[Paragraph("<b>Level</b>", S["BodyBold"]),
             Paragraph("<b>Focus</b>", S["BodyBold"]),
             Paragraph("<b>Done By</b>", S["BodyBold"])]]
    for lvl, focus, done_by in levels:
        data.append([Paragraph(lvl, S["Body"]), Paragraph(focus, S["Body"]), Paragraph(done_by, S["Body"])])
    tbl = Table(data, colWidths=[w*0.28, w*0.46, w*0.26])
    tbl.setStyle(TableStyle([
        ("GRID",         (0,0),(-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("BACKGROUND",   (0,0),(-1,0),  C_NAVY),
        ("TEXTCOLOR",    (0,0),(-1,0),  C_WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[C_WHITE, C_LGREY]),
        ("LEFTPADDING",  (0,0),(-1,-1), 8),
        ("RIGHTPADDING", (0,0),(-1,-1), 8),
        ("TOPPADDING",   (0,0),(-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
    ]))
    s.append(tbl)

    s.append(spacer(10))
    s.append(h3("Entry Criteria for Integration Testing"))
    s.append(p("Before integration testing begins, the following must be true:"))
    s += bullets([
        "Unit testing of all modules to be integrated is complete.",
        "Unit test results are reviewed and accepted.",
        "Integration test plan and test cases are ready.",
        "Test environment is set up and ready.",
        "All required modules are available (or stubs/drivers are ready).",
    ])

    s.append(h3("Exit Criteria for Integration Testing"))
    s.append(p("Integration testing is considered complete when:"))
    s += bullets([
        "All planned integration test cases have been executed.",
        "All critical and high severity defects are fixed and retested.",
        "Defect density is within acceptable thresholds.",
        "Test coverage requirements are met.",
        "Test summary report is prepared.",
    ])

    # ── 2.8 Scenario Testing ─────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("2.8  Scenario Testing"))
    s.append(hr())
    s.append(definition_box("Scenario Testing",
        "Scenario Testing is a testing technique that uses real-world scenarios (realistic "
        "stories about how users will use the system) to create and execute test cases. "
        "Instead of testing individual features in isolation, it tests end-to-end user "
        "journeys through the system.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "The key difference between scenario testing and regular testing: "
        "Regular testing asks 'Does this button work?' Scenario testing asks "
        "'Can a user complete their actual goal from start to finish?'"
    ))

    s.append(h3("Characteristics of Good Scenarios"))
    s += bullets([
        "Based on real user goals and workflows.",
        "Involve multiple features and components working together.",
        "Represent both common and exceptional cases.",
        "Written in simple language that non-technical stakeholders can understand.",
        "Cover complete end-to-end user journeys.",
    ])

    # ── 2.9 System Scenarios ─────────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.9  System Scenarios"))
    s.append(hr())
    s.append(definition_box("System Scenario",
        "A System Scenario describes a COMPLETE END-TO-END interaction with the system from "
        "a user perspective, covering multiple modules, subsystems, and potentially multiple "
        "users or roles. It tests how the entire system behaves in a realistic situation.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))

    s.append(h3("Example: E-Commerce System Scenario"))
    s.append(info_box(
        "<b>Scenario:</b> A customer browses an online store, adds items to cart, applies a discount "
        "coupon, enters payment details, completes purchase, and receives a confirmation email. "
        "Meanwhile, the inventory system is updated and the warehouse receives a fulfillment order. "
        "This single scenario tests: Product module, Cart module, Payment module, Email service, "
        "Inventory system, and Warehouse integration.",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h3("How to Create System Scenarios"))
    s += numbered([
        "Identify key user roles/actors in the system.",
        "List the most important goals users want to achieve.",
        "Write scenarios as stories: 'Given [context], When [action], Then [result].'",
        "Include both happy path (everything works) and unhappy path (errors, edge cases).",
        "Map scenarios to requirements to ensure coverage.",
        "Create test cases from each scenario.",
    ])

    s.append(h3("Types of System Scenarios"))
    s += bullets([
        "<b>Happy Path Scenarios:</b> Everything goes as expected — the 'normal' workflow.",
        "<b>Alternate Flow Scenarios:</b> User takes a different but valid path.",
        "<b>Exception/Error Scenarios:</b> What happens when something goes wrong — invalid input, system error, timeout.",
        "<b>Boundary Scenarios:</b> Testing at the edges of acceptable behavior.",
        "<b>Business Rule Scenarios:</b> Testing complex business logic that spans multiple modules.",
    ])

    # ── 2.10 Use Case Scenarios ──────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.10  Use Case Scenarios"))
    s.append(hr())
    s.append(definition_box("Use Case",
        "A Use Case is a description of a sequence of actions that a system performs in "
        "response to a request from an actor (user or external system) to achieve a goal. "
        "Use Cases form the basis for Use Case Scenario Testing.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))

    s.append(h3("Anatomy of a Use Case"))
    uc_rows = [
        ("Use Case ID", "Unique identifier, e.g., UC-001"),
        ("Use Case Name", "Short name, e.g., 'Login to System'"),
        ("Actor(s)", "Who initiates the use case — e.g., Registered User"),
        ("Preconditions", "Conditions that must be true before the UC starts — e.g., User is not logged in"),
        ("Main Flow", "The step-by-step sequence of the normal (happy) path"),
        ("Alternate Flows", "Other valid but less common paths"),
        ("Exception Flows", "What happens when errors occur"),
        ("Postconditions", "What is true after the UC completes — e.g., User is logged in"),
    ]
    s.append(two_col_table(uc_rows, headers=["Component", "Description"]))

    s.append(spacer(10))
    s.append(h3("Use Case Scenario Example: User Login"))
    s.append(info_box(
        "<b>Precondition:</b> User has a registered account. Not logged in.\n"
        "<b>Main Flow:</b> 1) User opens login page. 2) Enters email and password. "
        "3) Clicks Login. 4) System validates credentials. 5) System displays home dashboard.\n"
        "<b>Alternate Flow:</b> User checks 'Remember Me' → System stores session for 30 days.\n"
        "<b>Exception Flow:</b> Wrong password → System shows error message. After 3 attempts → Account locked.\n"
        "<b>Postcondition:</b> User is authenticated and sees personalized dashboard.",
        bg=C_LGREY, border=C_GREY
    ))

    s.append(h3("Deriving Test Cases from Use Cases"))
    s += bullets([
        "Each MAIN FLOW step becomes at least one test case (happy path).",
        "Each ALTERNATE FLOW becomes one or more test cases.",
        "Each EXCEPTION FLOW becomes one or more negative test cases.",
        "Boundary conditions in the flows need additional test cases.",
        "Combination scenarios (multiple use cases chained) are also tested.",
    ])

    # ── 2.11 Defect Bash ─────────────────────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("2.11  Defect Bash"))
    s.append(hr())
    s.append(definition_box("Defect Bash",
        "A Defect Bash (also called a 'Bug Bash') is an unstructured, time-boxed testing "
        "event where everyone on the team (developers, testers, business analysts, designers, "
        "product managers — even non-technical staff) explores the software freely to find "
        "as many defects as possible in a short period (typically 1–4 hours).",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))

    s.append(h3("Key Characteristics of a Defect Bash"))
    s += bullets([
        "<b>Exploratory:</b> No predefined test cases — participants freely explore.",
        "<b>Time-boxed:</b> Typically 1 to 4 hours of focused testing.",
        "<b>Cross-functional:</b> ALL team members participate, not just testers.",
        "<b>Collaborative:</b> Everyone works toward the same goal — find as many bugs as possible.",
        "<b>Competitive (optional):</b> Teams or individuals compete to find the most/most critical defects.",
    ])

    s.append(h3("How a Defect Bash is Conducted"))
    s += numbered([
        "<b>Preparation:</b> Ensure build is stable. Provide access to the application. Set up bug tracking tool. Brief all participants.",
        "<b>Team Formation:</b> Optionally form teams of 2-3 people with mixed skills.",
        "<b>Free Testing:</b> Everyone tests whatever they want, however they want for the allotted time.",
        "<b>Bug Logging:</b> All found defects are logged in the bug tracking tool with steps to reproduce.",
        "<b>Review:</b> After time is up, review all logged defects, remove duplicates, and prioritize.",
        "<b>Retrospective:</b> Discuss interesting findings, what areas had most defects, lessons learned.",
    ])

    s.append(h3("Benefits of a Defect Bash"))
    s += bullets([
        "Finds defects that structured testing missed — different perspectives see different things.",
        "Engages the whole team in quality — creates quality ownership across all roles.",
        "Quick and intensive — large number of defects found in short time.",
        "Non-testers discover usability and UX issues that testers might overlook.",
        "Fun and energizing — boosts team morale before a release.",
        "Especially useful before a major release to do final quality sweep.",
    ])

    s.append(h3("When to Do a Defect Bash"))
    s += bullets([
        "Before a major release or milestone to catch last-minute defects.",
        "After a major feature is developed to quickly explore it.",
        "When structured testing feels 'done' but confidence is not high.",
        "To test areas that are hard to cover with scripted tests.",
    ])

    return s


# ═══════════════════════════════════════════════════════════════════════════
# UNIT III
# ═══════════════════════════════════════════════════════════════════════════
def unit3():
    s = []
    s.append(PageBreak())
    s.append(unit_banner(3, "System Testing & Acceptance Testing",
        "Functional vs Non-Functional · System Testing · Performance · Security · UAT"))
    s.append(spacer(16))

    s.append(h1("3.1  System Testing"))
    s.append(hr())
    s.append(definition_box("System Testing",
        "System Testing is a level of software testing where the COMPLETE, fully integrated "
        "software system is tested to verify that it meets the specified requirements. "
        "It is a BLACK-BOX testing technique that evaluates the system's compliance with "
        "functional and non-functional requirements.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "System Testing is done AFTER integration testing is complete. At this point, all "
        "modules are assembled into the complete system. The system is now tested as a whole, "
        "as if it were a real user using the real application."
    ))

    s.append(h3("Objectives of System Testing"))
    s += bullets([
        "Verify that the system meets all functional requirements.",
        "Verify that the system meets all non-functional requirements (performance, security, etc.).",
        "Find defects not found in earlier testing levels.",
        "Ensure the system works correctly in the target environment.",
        "Validate end-to-end business flows and processes.",
        "Identify any integration issues with external systems.",
    ])

    s.append(h3("Who Performs System Testing?"))
    s.append(p(
        "System Testing is typically performed by an <b>independent test team</b> — "
        "separate from the development team. This independence is important because "
        "developers are often too close to their own code to find certain types of errors."
    ))

    # ── 3.2 Functional vs Non-Functional ────────────────────────────────────
    s.append(spacer(12))
    s.append(h1("3.2  Functional vs Non-Functional Testing"))
    s.append(hr())
    s.append(p(
        "System testing is divided into two major categories: Functional and Non-Functional testing."
    ))

    comparison_rows = [
        ("Definition", "Tests WHAT the system does — its features and functions", "Tests HOW WELL the system does it — qualities and characteristics"),
        ("Based On", "Functional requirements and specifications", "Non-functional requirements (performance standards, security standards)"),
        ("Tests", "Business logic, data processing, user actions", "Speed, reliability, scalability, security, usability"),
        ("Examples", "Login works, data is saved, calculations are correct", "System responds in < 2 seconds, handles 1000 users, data is encrypted"),
        ("Questions Asked", "Does it do the right thing?", "Does it do it well enough?"),
        ("When Found", "Earlier in testing", "Often needs specialized testing later"),
    ]
    data = [[Paragraph("<b>Aspect</b>", S["BodyBold"]),
             Paragraph("<b>Functional Testing</b>", S["BodyBold"]),
             Paragraph("<b>Non-Functional Testing</b>", S["BodyBold"])]]
    for row in comparison_rows:
        data.append([Paragraph(c, S["Body"]) for c in row])
    w = PAGE_W - 2*MARGIN - 4
    tbl = Table(data, colWidths=[w*0.22, w*0.39, w*0.39])
    tbl.setStyle(TableStyle([
        ("GRID",         (0,0),(-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("BACKGROUND",   (0,0),(-1,0),  C_NAVY),
        ("TEXTCOLOR",    (0,0),(-1,0),  C_WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[C_WHITE, C_LGREY]),
        ("LEFTPADDING",  (0,0),(-1,-1), 8),
        ("RIGHTPADDING", (0,0),(-1,-1), 8),
        ("TOPPADDING",   (0,0),(-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(tbl)

    # ── 3.3 Functional System Testing ───────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("3.3  Functional System Testing"))
    s.append(hr())
    s.append(p(
        "Functional System Testing verifies that every FUNCTION of the software works "
        "as specified in the requirements. It answers: 'Does the system DO what it is "
        "supposed to do?'"
    ))

    func_types = [
        ("Functionality Testing",
         "Tests that each function of the software produces the correct output for given inputs. "
         "This is the most basic form of functional testing — verify every feature works.",
         ["Login with valid credentials → User is logged in",
          "Transfer money → Correct amount debited from sender, credited to receiver",
          "Add to cart → Cart count increases, item appears in cart"]),
        ("Sanity Testing",
         "Quick, narrow testing of a specific function or area after a bug fix or minor change, "
         "to verify that the fix works and nothing obvious is broken. Done quickly before deeper testing.",
         ["After fixing a login bug, quickly test that login now works",
          "Not exhaustive — just a 'sanity check'"]),
        ("Smoke Testing / Build Verification Testing",
         "Initial testing of a new build to ensure the most basic functions work before "
         "detailed testing begins. If smoke test fails, the build is rejected and sent back to developers.",
         ["Open the application — does it launch?",
          "Can users log in?",
          "Can the main page be navigated?",
          "Named 'smoke testing' from hardware — power it on and see if smoke comes out"]),
        ("Regression Testing",
         "Regression testing is re-testing previously working functionality after changes "
         "(bug fixes, new features, code refactoring) to ensure that the changes have NOT "
         "broken any existing working functionality.",
         ["Very important — every code change carries risk of breaking other things",
          "Test cases from previous test cycles are re-run",
          "Automated regression testing is highly recommended for efficiency",
          "Run after every build, every bug fix, every new feature"]),
        ("Retesting",
         "Retesting is the testing of a specific defect after developers have fixed it, "
         "to confirm that the defect is indeed fixed.",
         ["Different from regression testing — retesting is for ONE specific defect",
          "Use the SAME test case that originally found the defect",
          "Verify the defect is closed before regression testing"]),
        ("Globalization / Internationalization (i18n) Testing",
         "Testing the software's capability to function in different locales, languages, "
         "currencies, date formats, and character sets without code changes.",
         ["Does the app work correctly in French, Arabic (right-to-left), Japanese?",
          "Are dates, currencies, and number formats locale-appropriate?",
          "Unicode characters handled correctly?"]),
        ("Localization (L10n) Testing",
         "Testing that the software has been correctly adapted for a specific locale — "
         "translated strings are correct, culturally appropriate, and fit in the UI.",
         ["Translated text is accurate and culturally appropriate",
          "UI is not broken by longer/shorter translated strings",
          "Local regulations are followed (e.g., GDPR in Europe)"]),
    ]

    for title, desc, examples in func_types:
        s.append(h3(title))
        s.append(p(desc))
        if examples:
            s += bullets(examples, style="Bullet2")
        s.append(spacer(6))

    # ── 3.4 Non-Functional System Testing ───────────────────────────────────
    s.append(PageBreak())
    s.append(h1("3.4  Non-Functional System Testing"))
    s.append(hr())
    s.append(p(
        "Non-functional testing evaluates how WELL the system performs, rather than "
        "what it does. These are the quality characteristics that determine user experience "
        "and system reliability in real-world conditions."
    ))

    nf_types = [
        ("Performance Testing",
         "Performance testing evaluates how the system behaves under expected and peak load conditions. "
         "It includes multiple sub-types:",
         [("Load Testing",
           "Testing the system's behavior under EXPECTED load (the anticipated number of users/transactions). "
           "Goal: Verify the system meets performance requirements under normal conditions.",
           ["Simulate 500 concurrent users on an e-commerce site during normal hours",
            "Measure response times, throughput, and resource utilization",
            "Identify performance bottlenecks under normal load"]),
          ("Stress Testing",
           "Testing the system BEYOND its expected maximum load, until it breaks. "
           "Goal: Find the breaking point and understand how the system fails (gracefully or catastrophically).",
           ["Push the system until it crashes — 2x, 5x, 10x normal load",
            "Observe: Does it crash suddenly or degrade gracefully?",
            "Does it recover automatically after load reduces?"]),
          ("Volume Testing",
           "Testing the system with a LARGE VOLUME OF DATA to check performance with big datasets.",
           ["Insert 10 million records into the database — does search still perform?",
            "Upload a 5GB file — does the system handle it?",
            "Fill all available disk space — how does the system react?"]),
          ("Spike Testing",
           "Testing the system's response to SUDDEN, DRAMATIC increases in load (spikes).",
           ["Normal load: 100 users. Suddenly 2000 users in 30 seconds.",
            "Does the system crash? Slow down? Recover when spike ends?",
            "Simulates flash sales, news events, viral content"]),
          ("Soak/Endurance Testing",
           "Running the system under SUSTAINED load for an EXTENDED period to find memory leaks, "
           "resource degradation, and stability issues.",
           ["Run at 70% load for 24 hours — does performance degrade over time?",
            "Detects memory leaks (slow increase in memory consumption)",
            "Ensures the system is stable for long-running production use"])]),
        ("Security Testing",
         "Security testing evaluates the software's ability to protect data and maintain "
         "functionality against malicious attacks and unauthorized access.",
         [("Authentication Testing",
           "Verifying that only legitimate users can access the system.",
           ["Test valid credentials → Access granted",
            "Test invalid credentials → Access denied",
            "Test brute force protection — account lockout after N failed attempts"]),
          ("Authorization Testing",
           "Verifying that users can only access resources they are permitted to access.",
           ["Admin can access admin panel; regular user cannot",
            "User A cannot access User B's private data",
            "Test privilege escalation attempts"]),
          ("SQL Injection Testing",
           "Attempting to inject malicious SQL code through input fields to manipulate the database.",
           ["Enter: ' OR '1'='1 in login field — should NOT bypass login",
            "Enter: DROP TABLE users; — database should NOT execute this",
            "Parameterized queries should prevent injection"]),
          ("Cross-Site Scripting (XSS) Testing",
           "Testing that malicious scripts cannot be injected into web pages viewed by other users.",
           ["Input: <script>alert('XSS')</script> — browser should NOT execute this",
            "Stored XSS: Does malicious script persist in the database?",
            "Proper input sanitization and output encoding should prevent XSS"]),
          ("Penetration Testing",
           "Ethical hacking — attempting to break into the system using real attack techniques.",
           ["Performed by security experts (pen testers)",
            "Simulates a real attacker trying to breach the system",
            "Results in a security report with vulnerabilities ranked by severity"])]),
        ("Usability Testing",
         "Usability testing evaluates how easy and intuitive the software is to use. "
         "Real users perform tasks while testers observe.",
         [("What is Measured:",
           "Effectiveness (can users complete tasks?), Efficiency (how long does it take?), "
           "Satisfaction (do users like it?), Learnability (how quickly can new users learn?), "
           "Error rate (how often do users make mistakes?).",
           ["Observe real users trying to complete key tasks",
            "Note where they get confused, frustrated, or make errors",
            "Gather subjective feedback on satisfaction"])]),
        ("Compatibility Testing",
         "Testing that the software works correctly across different environments.",
         [("Types of Compatibility Testing:",
           "Browser Compatibility, Operating System Compatibility, Device Compatibility, "
           "Resolution/Screen Size Compatibility, Database Compatibility.",
           ["Does the web app work in Chrome, Firefox, Safari, Edge?",
            "Does the desktop app run on Windows 10, 11, macOS?",
            "Does the mobile app work on iPhone and Android?"])]),
        ("Reliability Testing",
         "Testing the software's ability to perform consistently over time under specified conditions.",
         [("What Reliability Testing Checks:",
           "Mean Time Between Failures (MTBF): Average time the system runs without failing. "
           "Mean Time To Repair (MTTR): Average time to fix a failure and restore service. "
           "Failure rate and recovery behavior.",
           ["Run the system continuously for 72 hours",
            "Count failures, measure recovery time",
            "Calculate MTBF and MTTR metrics"])]),
        ("Scalability Testing",
         "Testing the software's ability to SCALE UP (handle more load) or SCALE OUT "
         "(add more servers) to accommodate growth.",
         [("What Scalability Testing Checks:",
           "Can the system handle 10x current users with added infrastructure? "
           "Does performance remain acceptable as data grows? "
           "Are there architectural bottlenecks that prevent scaling?",
           ["Add more servers — does performance improve proportionally?",
            "Double the database size — does query performance remain acceptable?"])]),
        ("Portability Testing",
         "Testing the ease with which the software can be moved from one environment to another.",
         [("Portability Aspects:",
           "Installation portability (easy to install/uninstall), "
           "Platform portability (runs on multiple OS), "
           "Data portability (data can be migrated between systems).",
           ["Install the software on a new machine — any issues?",
            "Migrate from old system to new system — data intact?",
            "Move from on-premise to cloud — functionality preserved?"])]),
    ]

    for title, main_desc, sub_types in nf_types:
        s.append(h2(title))
        s.append(p(main_desc))
        for sub_name, sub_desc, examples in sub_types:
            s.append(h4(sub_name))
            s.append(p(sub_desc))
            s += bullets(examples, style="Bullet2")
            s.append(spacer(4))
        s.append(spacer(8))

    # ── 3.5 Acceptance Testing ───────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("3.5  Acceptance Testing"))
    s.append(hr())
    s.append(definition_box("Acceptance Testing",
        "Acceptance Testing is the final level of testing performed to determine whether "
        "a system satisfies the business requirements and is acceptable for delivery to "
        "end users. It is performed to gain confidence that the system is ready for release "
        "and that the customer ACCEPTS the delivered system.",
        bg=C_LTEAL, border=C_TEAL))
    s.append(spacer(8))
    s.append(p(
        "While all previous testing levels (Unit, Integration, System) are done by the "
        "development/testing team, Acceptance Testing is done by the <b>CUSTOMER or END USERS</b>. "
        "The goal is to verify that the system delivers the expected BUSINESS VALUE."
    ))

    s.append(h3("Types of Acceptance Testing"))

    acceptance_types = [
        ("User Acceptance Testing (UAT)",
         "UAT is the most common and important type of acceptance testing. Real END USERS "
         "test the system in a realistic environment using real-world scenarios to verify "
         "it meets their needs and is ready for production use.",
         ["Performed by actual end users or representatives",
          "Uses realistic business scenarios and data",
          "Tests that the system supports users in doing their actual jobs",
          "Feedback from UAT directly determines if the system goes live",
          "Often done in a UAT environment that mirrors production"]),
        ("Business Acceptance Testing (BAT)",
         "BAT is performed by business stakeholders (managers, business analysts) to ensure "
         "the system meets BUSINESS REQUIREMENTS and business processes.",
         ["Verifies business rules are correctly implemented",
          "Checks that business workflows and processes work end-to-end",
          "Focuses on business impact rather than technical correctness"]),
        ("Contract Acceptance Testing",
         "Testing done to verify that the software meets the criteria and requirements "
         "specified in the CONTRACT between the client and the vendor.",
         ["All features listed in the contract must be present and working",
          "Performance benchmarks specified in contract must be met",
          "Acceptance sign-off releases payment to the vendor"]),
        ("Regulations Acceptance Testing",
         "Testing to verify that the software complies with legal regulations, "
         "standards, and governmental requirements applicable to the software.",
         ["Financial software: Compliance with banking regulations (SOX, PCI DSS)",
          "Healthcare software: Compliance with HIPAA",
          "European software: Compliance with GDPR",
          "Safety-critical systems: Compliance with safety standards (DO-178C for aviation)"]),
        ("Alpha Testing",
         "Alpha testing is performed by the development team or internal staff at the "
         "DEVELOPER'S SITE before releasing to external users. "
         "It is an early form of acceptance testing.",
         ["Done in a controlled environment by internal users",
          "Performed before any external release",
          "Simulated real-world usage by internal staff",
          "Bugs are found and fixed before beta release",
          "Users know they are testing and are expected to provide feedback"]),
        ("Beta Testing",
         "Beta testing is performed by a selected group of REAL END USERS at their own "
         "environment/location BEFORE the final product launch. "
         "It is a real-world test without developer control.",
         ["Done by real customers in their real environment",
          "Users are not told exactly what to test — free to use as they naturally would",
          "Feedback is collected via bug reports, surveys, feedback forms",
          "Bugs found are fixed before the general release",
          "Examples: Software 'beta programs', app beta releases on Play Store/App Store",
          "Divided into: Closed Beta (invited users only) vs Open Beta (anyone can join)"]),
        ("Operational Acceptance Testing (OAT)",
         "OAT is performed by operations/system administrators to verify that the system "
         "can be successfully deployed, maintained, and operated in the production environment.",
         ["Backup and restore procedures work correctly",
          "System startup and shutdown procedures are tested",
          "Disaster recovery procedures are validated",
          "Monitoring and alerting systems are working",
          "Security patches can be applied without issues"]),
    ]

    for title, desc, bullets_list in acceptance_types:
        s.append(h3(title))
        s.append(p(desc))
        s += bullets(bullets_list, style="Bullet2")
        s.append(spacer(8))

    s.append(h3("Acceptance Testing Process"))
    s += numbered([
        "<b>Define Acceptance Criteria:</b> Business and users agree on what 'acceptable' means — specific, measurable criteria.",
        "<b>Create Acceptance Test Plan:</b> Document scope, schedule, participants, entry/exit criteria, and test environment.",
        "<b>Develop Test Cases:</b> Based on acceptance criteria, create scenarios and test cases.",
        "<b>Set Up Test Environment:</b> Ensure the environment mirrors production as closely as possible.",
        "<b>Execute Tests:</b> Users/business stakeholders run the test cases and free exploration.",
        "<b>Log Defects:</b> Any issues found are logged and communicated to the development team.",
        "<b>Fix & Retest:</b> Critical defects are fixed and retested.",
        "<b>Go/No-Go Decision:</b> Based on results, stakeholders decide if the system is ready for release.",
        "<b>Sign-Off:</b> Formal acceptance sign-off is given by authorized stakeholders.",
    ])

    s.append(spacer(10))
    s.append(h3("Entry and Exit Criteria for Acceptance Testing"))
    criteria_rows = [
        ("<b>Entry Criteria</b>",
         "System testing complete and sign-off given\nAll critical & high defects resolved\nAcceptance test environment ready\nTest data prepared\nUsers trained and available"),
        ("<b>Exit Criteria</b>",
         "All acceptance test cases executed\nNo critical or high severity defects open\nAcceptance criteria met\nFormal sign-off received from business/users\nRelease readiness confirmed"),
    ]
    s.append(two_col_table(criteria_rows, col_ratio=(0.3, 0.7)))

    s.append(spacer(14))
    s.append(h3("Difference Between Alpha and Beta Testing"))
    ab_rows = [
        ("Performed by", "Internal team / QA", "Real external users"),
        ("Location", "Developer's site", "User's own environment"),
        ("Environment", "Controlled", "Real-world / uncontrolled"),
        ("Control", "High — developers can intervene", "Low — users test freely"),
        ("Purpose", "Find bugs before external release", "Validate in real world, find remaining issues"),
        ("Feedback", "Immediate and direct", "Via forms, bug reports, usage analytics"),
    ]
    data = [[Paragraph("<b>Aspect</b>", S["BodyBold"]),
             Paragraph("<b>Alpha Testing</b>", S["BodyBold"]),
             Paragraph("<b>Beta Testing</b>", S["BodyBold"])]]
    for row in ab_rows:
        data.append([Paragraph(c, S["Body"]) for c in row])
    w = PAGE_W - 2*MARGIN - 4
    tbl = Table(data, colWidths=[w*0.25, w*0.375, w*0.375])
    tbl.setStyle(TableStyle([
        ("GRID",         (0,0),(-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("BACKGROUND",   (0,0),(-1,0),  C_NAVY),
        ("TEXTCOLOR",    (0,0),(-1,0),  C_WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[C_WHITE, C_LGREY]),
        ("LEFTPADDING",  (0,0),(-1,-1), 8),
        ("RIGHTPADDING", (0,0),(-1,-1), 8),
        ("TOPPADDING",   (0,0),(-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(tbl)

    # ── Final summary ────────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(h1("Quick Revision Summary"))
    s.append(hr())

    summary_rows = [
        ("<b>UNIT I</b>", ""),
        ("SDLC Phases", "Requirements → Design → Coding → Testing → Deployment → Maintenance"),
        ("Quality", "Meeting requirements + free from defects + meets user needs"),
        ("QA vs QC", "QA = prevent defects (process). QC = detect defects (product)"),
        ("Verification", "Building the product RIGHT — static reviews, inspections"),
        ("Validation", "Building the RIGHT product — dynamic testing, running the software"),
        ("STLC Phases", "Req Analysis → Test Plan → Test Case Dev → Env Setup → Execution → Closure"),
        ("Static Testing", "No code execution — reviews, walkthroughs, inspections, static analysis"),
        ("White Box Testing", "Tester sees code — statement, branch, path, condition coverage"),
        ("Cyclomatic Complexity", "CC = E - N + 2P; measures independent paths in code"),
        ("Black Box Testing", "No code knowledge — EP, BVA, Decision Table, State Transition, Use Case"),
        ("<b>UNIT II</b>", ""),
        ("Integration Testing", "Tests interaction between combined modules/components"),
        ("Top-Down", "Start from top, use STUBS for lower modules not yet integrated"),
        ("Bottom-Up", "Start from bottom, use DRIVERS for higher modules not yet integrated"),
        ("Bi-Directional", "Combine both Top-Down and Bottom-Up simultaneously"),
        ("System Integration", "Tests software with external systems, APIs, hardware"),
        ("Big Bang", "All at once — NOT recommended for large systems"),
        ("Scenario Testing", "Test complete end-to-end user journeys"),
        ("System Scenarios", "Full realistic system-wide use cases with multiple modules"),
        ("Use Case Testing", "Based on use cases — main flow, alternate flow, exception flow"),
        ("Defect Bash", "Time-boxed, unstructured, everyone tests freely to find bugs"),
        ("<b>UNIT III</b>", ""),
        ("System Testing", "Complete integrated system tested against requirements"),
        ("Functional Testing", "Tests WHAT the system does — features, business logic"),
        ("Smoke Testing", "Quick initial test to verify basic build stability"),
        ("Regression Testing", "Re-test existing features after changes to ensure nothing broke"),
        ("Performance Testing", "How well system performs — Load, Stress, Volume, Spike, Soak"),
        ("Security Testing", "Auth, Authorization, SQL Injection, XSS, Penetration Testing"),
        ("Usability Testing", "How easy/intuitive is the software for real users"),
        ("Acceptance Testing", "Customer/user validates the system is ready for release"),
        ("UAT", "Real users test the system in realistic conditions"),
        ("Alpha Testing", "Internal users test at developer site before external release"),
        ("Beta Testing", "External users test in their own environment before public launch"),
    ]

    data = []
    for term, defn in summary_rows:
        if defn == "":
            data.append([Paragraph(term, S["H3"]), Paragraph("", S["Body"])])
        else:
            data.append([Paragraph(term, S["BodyBold"]), Paragraph(defn, S["Body"])])

    w = PAGE_W - 2*MARGIN - 4
    tbl = Table(data, colWidths=[w*0.32, w*0.68])
    style_cmds = [
        ("GRID",         (0,0),(-1,-1), 0.3, colors.HexColor("#e2e8f0")),
        ("LEFTPADDING",  (0,0),(-1,-1), 8),
        ("RIGHTPADDING", (0,0),(-1,-1), 8),
        ("TOPPADDING",   (0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]
    # Highlight unit headers
    for i, (term, defn) in enumerate(summary_rows):
        if defn == "":
            style_cmds.append(("BACKGROUND", (0,i),(1,i), C_NAVY))
            style_cmds.append(("TEXTCOLOR",  (0,i),(1,i), C_WHITE))
        elif i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0,i),(1,i), C_LGREY))
        else:
            style_cmds.append(("BACKGROUND", (0,i),(1,i), C_WHITE))
    tbl.setStyle(TableStyle(style_cmds))
    s.append(tbl)

    s.append(spacer(20))
    s.append(info_box(
        "<b>Best of luck with your exam!</b>  Remember: Testing is not just about finding bugs — "
        "it's about building CONFIDENCE that the software works correctly for its users. "
        "Quality is everyone's responsibility.",
        bg=C_LTEAL, border=C_TEAL
    ))

    return s


# ═══════════════════════════════════════════════════════════════════════════
# BUILD DOCUMENT
# ═══════════════════════════════════════════════════════════════════════════
def page_header_footer(canvas, doc):
    """Header and footer for all pages except cover."""
    if doc.page == 1:
        return
    canvas.saveState()
    w, h = A4
    # Header line
    canvas.setStrokeColor(C_BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, h - MARGIN + 4, w - MARGIN, h - MARGIN + 4)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(C_NAVY)
    canvas.drawString(MARGIN, h - MARGIN + 8, "SOFTWARE TESTING — Complete Study Notes")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(C_GREY)
    canvas.drawRightString(w - MARGIN, h - MARGIN + 8, f"Page {doc.page}")
    # Footer line
    canvas.setStrokeColor(C_BLUE)
    canvas.line(MARGIN, MARGIN - 4, w - MARGIN, MARGIN - 4)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(C_GREY)
    canvas.drawCentredString(w / 2, MARGIN - 14, "Unit I: Principles & SDLC  |  Unit II: Integration Testing  |  Unit III: System & Acceptance Testing")
    canvas.restoreState()

out_path = "/mnt/user-data/outputs/Software_Testing_Complete_Notes.pdf"
doc = SimpleDocTemplate(
    out_path,
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN + 0.5*cm, bottomMargin=MARGIN + 0.5*cm,
    title="Software Testing — Complete Study Notes",
    author="Study Notes Generator",
)

story = []
story += cover_page()
story += unit1()
story += unit2()
story += unit3()

doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
print("PDF generated successfully:", out_path)
if __name__ == "__main__":
    doc = SimpleDocTemplate("Software_Testing_Notes.pdf", pagesize=A4)
    story = []

    story += cover_page()
    story += unit1()
    story += unit2()

    doc.build(story)