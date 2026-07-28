from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import KeepTogether

PAGE_W, PAGE_H = A4
MARGIN_LEFT  = 18 * mm
MARGIN_RIGHT = 18 * mm
MARGIN_TOP   = 16 * mm
MARGIN_BOT   = 16 * mm

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY    = colors.HexColor("#1B2A4A")   # section headers / name
TEAL    = colors.HexColor("#1E7F8E")   # accent bar / sub-headers
LGRAY   = colors.HexColor("#5A5A5A")   # body text
RULE    = colors.HexColor("#D0D8E4")   # thin divider lines
WHITE   = colors.white
OFFWHT  = colors.HexColor("#F7F9FC")   # skill-chip background

# ── Styles ───────────────────────────────────────────────────────────────────
def make_styles():
    s = {}

    s["name"] = ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=22,
        textColor=NAVY, leading=26, alignment=TA_LEFT
    )
    s["tagline"] = ParagraphStyle(
        "tagline", fontName="Helvetica", fontSize=9,
        textColor=LGRAY, leading=13, alignment=TA_LEFT, spaceAfter=4
    )
    s["contact"] = ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.5,
        textColor=LGRAY, leading=12, alignment=TA_LEFT
    )
    s["section"] = ParagraphStyle(
        "section", fontName="Helvetica-Bold", fontSize=10,
        textColor=WHITE, leading=14, alignment=TA_LEFT,
        leftIndent=4, spaceAfter=6
    )
    s["profile"] = ParagraphStyle(
        "profile", fontName="Helvetica", fontSize=9,
        textColor=LGRAY, leading=14, alignment=TA_JUSTIFY,
        spaceAfter=2
    )
    s["job_title"] = ParagraphStyle(
        "job_title", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=NAVY, leading=13, spaceAfter=0
    )
    s["job_org"] = ParagraphStyle(
        "job_org", fontName="Helvetica-Oblique", fontSize=8.5,
        textColor=TEAL, leading=12, spaceAfter=2
    )
    s["bullet"] = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=8.8,
        textColor=LGRAY, leading=13, leftIndent=10,
        bulletIndent=2, spaceAfter=1
    )
    s["skill_head"] = ParagraphStyle(
        "skill_head", fontName="Helvetica-Bold", fontSize=8.5,
        textColor=NAVY, leading=12, spaceAfter=2
    )
    s["skill_body"] = ParagraphStyle(
        "skill_body", fontName="Helvetica", fontSize=8.5,
        textColor=LGRAY, leading=12, spaceAfter=6
    )
    s["proj_title"] = ParagraphStyle(
        "proj_title", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=NAVY, leading=13, spaceAfter=0
    )
    s["proj_meta"] = ParagraphStyle(
        "proj_meta", fontName="Helvetica-Oblique", fontSize=8.2,
        textColor=TEAL, leading=11, spaceAfter=1
    )
    s["proj_spec"] = ParagraphStyle(
        "proj_spec", fontName="Helvetica", fontSize=7.8,
        textColor=TEAL, leading=11, spaceAfter=3,
        borderColor=TEAL, borderWidth=0
    )
    s["edu_degree"] = ParagraphStyle(
        "edu_degree", fontName="Helvetica-Bold", fontSize=9.2,
        textColor=NAVY, leading=13, spaceAfter=0
    )
    s["edu_inst"] = ParagraphStyle(
        "edu_inst", fontName="Helvetica-Oblique", fontSize=8.5,
        textColor=LGRAY, leading=12, spaceAfter=1
    )
    s["edu_detail"] = ParagraphStyle(
        "edu_detail", fontName="Helvetica", fontSize=8.2,
        textColor=LGRAY, leading=11, spaceAfter=6
    )
    return s

# ── Helpers ──────────────────────────────────────────────────────────────────
def section_header(title, styles):
    """Teal background banner for section titles."""
    tbl = Table(
        [[Paragraph(f"  {title.upper()}", styles["section"])]],
        colWidths=[PAGE_W - MARGIN_LEFT - MARGIN_RIGHT]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [TEAL]),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    return tbl

def bullet(text, styles):
    return Paragraph(f"<bullet>&bull;</bullet>&nbsp;{text}", styles["bullet"])

def rule():
    return HRFlowable(
        width="100%", thickness=0.4,
        color=RULE, spaceAfter=4, spaceBefore=4
    )

def spacer(h=4):
    return Spacer(1, h * mm)

# ── Content builders ─────────────────────────────────────────────────────────
def build_header(s):
    """Two-column header: Name/tagline left | contact right."""
    left = [
        Paragraph("AJAY ARAVINDAN", s["name"]),
        Paragraph(
            "Audio Post-Production &amp; Content Delivery | Sound Technology Graduate",
            s["tagline"]
        ),
    ]
    right_lines = [
        "Liverpool, UK &nbsp;|&nbsp; +44 7471 238236",
        '<a href="mailto:ajxarx@gmail.com" color="#1E7F8E">ajxarx@gmail.com</a>',
        '<a href="https://linkedin.com/in/ajxarx" color="#1E7F8E">linkedin.com/in/ajxarx</a>',
        '<a href="https://ajayaravindan.notion.site" color="#1E7F8E">Portfolio: ajayaravindan.notion.site</a>',
        "Right to Work: British Citizen | Willing to Relocate to London",
    ]
    right = [Paragraph(line, s["contact"]) for line in right_lines]

    left_col  = [item for item in left]
    right_col = right

    tbl = Table(
        [[left_col, right_col]],
        colWidths=[
            (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.55,
            (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.45,
        ]
    )
    tbl.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("ALIGN",         (1, 0), (1, -1), "RIGHT"),
    ]))
    return tbl


def build_profile(s):
    text = (
        "Sound Technology graduate with hands-on experience in audio post-production, "
        "broadcast-compliant delivery, and professional mastering workflows. Proven technical "
        "grounding in <b>Pro Tools, Adobe Premiere, EBU R128 loudness compliance, AS-11 DPP, "
        "and DCI standards</b>. Experienced delivering multi-format outputs including "
        "<b>Dolby Atmos 7.1.2, 5.1 surround, and LtRt (LoRo) fold-down</b> to professional "
        "broadcast specifications. Eager to develop expertise in digital cinema mastering, "
        "<b>DCP creation, transcoding, and technical QC</b> within a fast-paced post-production "
        "environment. Highly detail-oriented, disciplined under tight deadlines, and fully "
        "available for <b>shift-based working including nights, weekends, and public holidays</b>."
    )
    return Paragraph(text, s["profile"])


def build_skills(s):
    categories = [
        (
            "Post-Production Software",
            "Pro Tools  ·  Adobe Premiere  ·  Avid S6 Console  ·  Ableton Live  ·  Microsoft Suite  ·  Power BI"
        ),
        (
            "Audio Post-Production",
            "Dolby Atmos Mixing (7.1.2)  ·  5.1 Surround Mixing  ·  LtRt / LoRo Fold-Down  ·  Re-Recording Mixer  "
            "·  Audio Conforming  ·  ADR Recording &amp; Editing  ·  Foley Recording &amp; Editing  ·  Sound Design for Picture"
        ),
        (
            "Broadcast &amp; Cinema Delivery Standards",
            "EBU R128 Loudness Normalisation  ·  AS-11 DPP (HD)  ·  EBU R123 (16-Channel Track Order)  "
            "·  DCI Standards  ·  Interop DCP (Familiarity)  ·  SMPTE Standards (Familiarity)"
        ),
        (
            "Technical QC &amp; Compliance",
            "Loudness Compliance &amp; Correction  ·  Broadcast Format Export  ·  Audio Stem Preparation  "
            "·  File Validation  ·  Audio Conforming to EBU R123"
        ),
    ]
    elems = []
    for head, body in categories:
        row = Table(
            [[Paragraph(head, s["skill_head"]), Paragraph(body, s["skill_body"])]],
            colWidths=[
                (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.28,
                (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.72,
            ]
        )
        row.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING",   (0, 0), (-1, -1), 0),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
            ("LINEBELOW",     (0, 0), (-1, -1), 0.3, RULE),
        ]))
        elems.append(row)
    return elems


def build_projects(s):
    projects = [
        {
            "title": "Escape — Animated Short Film",
            "meta":  "Sound Designer &amp; Re-Recording Mixer  |  LIPA  |  "
                     '<a href="INSERT_VIMEO_LINK" color="#1E7F8E">▶ Watch on Vimeo</a>  |  '
                     '<a href="INSERT_SOUNDCLOUD_LINK" color="#1E7F8E">🎧 Audio Demo</a>',
            "spec":  "Pro Tools  ·  Dolby Atmos 7.1.2  ·  EBU R128  ·  AS-11 DPP (HD)  ·  5.1  ·  LtRt Fold-Down",
            "bullets": [
                "Delivered full audio post-production pipeline — sound design, Dolby Atmos 7.1.2 mix, and broadcast-compliant stems.",
                "EBU R128 loudness normalisation; exported to AS-11 DPP (HD) conforming to EBU R123 (16-channel track order), meeting full broadcast delivery specification.",
                "Re-rendered Atmos mix to 5.1 surround and LtRt (LoRo) fold-down for multi-platform distribution compatibility.",
            ]
        },
        {
            "title": "Flow — Animated Feature Film",
            "meta":  "Sound Designer &amp; Re-Recording Mixer  |  LIPA  |  "
                     '<a href="INSERT_VIMEO_LINK" color="#1E7F8E">▶ Watch on Vimeo</a>  |  '
                     '<a href="INSERT_SOUNDCLOUD_LINK" color="#1E7F8E">🎧 Audio Demo</a>',
            "spec":  "Pro Tools  ·  Dolby Atmos 7.1.2  ·  5.1 Surround  ·  Foley  ·  ADR  ·  Music Integration",
            "bullets": [
                "End-to-end audio post-production for a full-length animated feature: sound design, Foley recording &amp; editing, ADR, and original music integration.",
                "Completed Dolby Atmos 7.1.2 mix with full 5.1 fold-down, demonstrating proficiency across immersive and standard delivery formats.",
                "Managed the full audio pipeline from production through final deliverables, ensuring technical and creative alignment with picture lock.",
            ]
        },
        {
            "title": "Superman Comic Book Audio Experience",
            "meta":  "Sound Designer &amp; Mixer  |  LIPA  |  "
                     '<a href="INSERT_LINK" color="#1E7F8E">▶ Watch / Listen</a>  |  '
                     '<a href="INSERT_PDF_LINK" color="#1E7F8E">📄 Spec Sheet</a>',
            "spec":  "Pro Tools  ·  5.1 Surround  ·  Stereo Fold-Down  ·  ADR  ·  SFX  ·  Foley  ·  Music",
            "bullets": [
                "Conceived and produced a page-synchronised audio experience accompanying a Superman comic — demonstrating creative concept development alongside technical delivery.",
                "Delivered complete sound design (Music, ADR, Foley, SFX); mixed to 5.1 surround with stereo fold-down to professional multi-format delivery standards.",
            ]
        },
    ]

    elems = []
    for p in projects:
        block = [
            Paragraph(p["title"], s["proj_title"]),
            Paragraph(p["meta"],  s["proj_meta"]),
            Paragraph(f"<font color='#1E7F8E'><b>Tools / Standards:</b></font>  {p['spec']}", s["proj_spec"]),
        ] + [bullet(b, s) for b in p["bullets"]] + [spacer(3)]
        elems.append(KeepTogether(block))
    return elems


def build_experience(s):
    jobs = [
        {
            "title": "Freelance Audio Technician",
            "org":   "Ajay Freelancer F Events Management  |  Abu Dhabi, UAE  |  Oct 2021 – Sep 2023",
            "bullets": [
                "Engineered audio systems for <b>20+ corporate events</b>; responsible for technical compliance and quality assurance of all audio output.",
                "Collaborated directly with clients through pre-production and setup phases to establish technical requirements, delivery specifications, and project design briefs.",
                "Assisted lead sound supervisor across multiple productions — radio mic deployment, system design, signal routing, and live monitoring.",
                "Installed, operated, and maintained professional sound equipment across multiple client organisations, maintaining audio integrity throughout.",
            ]
        },
        {
            "title": "Project Management Consultant",
            "org":   "Digital Qatalyst  |  Dubai, UAE  |  Nov 2021 – Feb 2022",
            "bullets": [
                "Delivered data-driven operational solutions to clients using Microsoft Excel and Power BI; managed communications for a portfolio of client accounts.",
            ]
        },
        {
            "title": "Bar Team Leader / Till Operator (Casual)",
            "org":   "Liverpool FC Stadium  |  Liverpool, UK  |  May 2024 – Present",
            "bullets": [
                "Lead a team of bar staff during matchdays and large-scale events; coordinate workflow under high-pressure, time-critical conditions — directly relevant to fast-paced post-production shift environments.",
                "Conduct health and safety compliance checks to meet venue and licensing standards.",
                "Manage stock, visual merchandising, and delivery processing; liaise with supervisors and management.",
            ]
        },
    ]

    elems = []
    for j in jobs:
        block = [
            Paragraph(j["title"], s["job_title"]),
            Paragraph(j["org"],   s["job_org"]),
        ] + [bullet(b, s) for b in j["bullets"]] + [spacer(3)]
        elems.append(KeepTogether(block))
    return elems


def build_education(s):
    entries = [
        {
            "degree": "BA (Hons) Sound Technology",
            "date":   "Expected: June 2026",
            "inst":   "Liverpool Institute for Performing Arts (LIPA)  |  Liverpool, UK",
            "detail": "Relevant modules: Audio Post-Production  ·  Broadcast Delivery Standards  ·  Dolby Atmos Production  ·  Film Sound  ·  Digital Media Delivery",
        },
        {
            "degree": "BSc Business Administration",
            "date":   "Graduated: June 2020",
            "inst":   "Rochester Institute of Technology  |  Dubai, UAE",
            "detail": "",
        },
    ]

    elems = []
    for e in entries:
        # Degree + date on same row
        row = Table(
            [[Paragraph(e["degree"], s["edu_degree"]),
              Paragraph(e["date"], s["edu_inst"])]],
            colWidths=[
                (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.70,
                (PAGE_W - MARGIN_LEFT - MARGIN_RIGHT) * 0.30,
            ]
        )
        row.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING",   (0, 0), (-1, -1), 0),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
            ("ALIGN",         (1, 0), (1, -1), "RIGHT"),
        ]))
        block = [row, Paragraph(e["inst"], s["edu_inst"])]
        if e["detail"]:
            block.append(Paragraph(e["detail"], s["edu_detail"]))
        else:
            block.append(spacer(4))
        elems.append(KeepTogether(block))
    return elems


# ── Main ──────────────────────────────────────────────────────────────────────
def build_pdf(out_path):
    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOT,
        title="Ajay Aravindan — CV",
        author="Ajay Aravindan",
    )

    s = make_styles()
    story = []

    # ── Header ────────────────────────────────────────────────────────────────
    story.append(build_header(s))
    story.append(spacer(3))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))

    # ── Professional Profile ──────────────────────────────────────────────────
    story.append(section_header("Professional Profile", s))
    story.append(spacer(2))
    story.append(build_profile(s))
    story.append(spacer(5))

    # ── Technical Skills ──────────────────────────────────────────────────────
    story.append(section_header("Technical Skills", s))
    story.append(spacer(2))
    story.extend(build_skills(s))
    story.append(spacer(5))

    # ── Portfolio Projects ────────────────────────────────────────────────────
    story.append(section_header("Portfolio Projects", s))
    story.append(spacer(2))
    story.extend(build_projects(s))
    story.append(spacer(2))

    # ── Work Experience ───────────────────────────────────────────────────────
    story.append(section_header("Work Experience", s))
    story.append(spacer(2))
    story.extend(build_experience(s))
    story.append(spacer(2))

    # ── Education ─────────────────────────────────────────────────────────────
    story.append(section_header("Education", s))
    story.append(spacer(2))
    story.extend(build_education(s))

    doc.build(story)
    print(f"PDF created: {out_path}")


if __name__ == "__main__":
    build_pdf("AJAY_ARAVINDAN_CV.pdf")
