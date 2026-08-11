"""
ATS-Optimised CV Generator for Ajay Aravindan
Uses ReportLab — clean single-column layout, machine-readable text throughout.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "CV", "AJAY ARAVINDAN.pdf")

# ── Colour palette ────────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1B2A4A")
TEAL   = colors.HexColor("#1E7F8E")
LGRAY  = colors.HexColor("#5A6A7A")
RULE   = colors.HexColor("#D0D8E4")
BLACK  = colors.HexColor("#111111")
WHITE  = colors.white

W, H = A4
ML = 18*mm
MR = 18*mm
MT = 16*mm
MB = 16*mm

# ── Styles ────────────────────────────────────────────────────────────────────
def styles():
    return {
        "name": ParagraphStyle(
            "name", fontName="Helvetica-Bold", fontSize=26,
            textColor=NAVY, spaceAfter=1*mm, alignment=TA_LEFT,
            leading=30
        ),
        "tagline": ParagraphStyle(
            "tagline", fontName="Helvetica", fontSize=9.5,
            textColor=TEAL, spaceAfter=2*mm, alignment=TA_LEFT,
            leading=14
        ),
        "contact": ParagraphStyle(
            "contact", fontName="Helvetica", fontSize=8.5,
            textColor=LGRAY, spaceAfter=0, alignment=TA_LEFT,
            leading=13
        ),
        "section": ParagraphStyle(
            "section", fontName="Helvetica-Bold", fontSize=9,
            textColor=TEAL, spaceBefore=5*mm, spaceAfter=1.5*mm,
            alignment=TA_LEFT, leading=12,
            letterSpacing=1.2, textTransform="uppercase"
        ),
        "job_title": ParagraphStyle(
            "job_title", fontName="Helvetica-Bold", fontSize=10,
            textColor=NAVY, spaceAfter=0.5*mm, leading=13
        ),
        "job_org": ParagraphStyle(
            "job_org", fontName="Helvetica", fontSize=9,
            textColor=TEAL, spaceAfter=0.5*mm, leading=12
        ),
        "date": ParagraphStyle(
            "date", fontName="Helvetica-Oblique", fontSize=8.5,
            textColor=LGRAY, spaceAfter=1.5*mm, leading=12
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName="Helvetica", fontSize=9,
            textColor=BLACK, spaceAfter=1.2*mm, leading=13,
            leftIndent=8*mm, firstLineIndent=-4*mm
        ),
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=9,
            textColor=BLACK, spaceAfter=1.5*mm, leading=13
        ),
        "skill_cat": ParagraphStyle(
            "skill_cat", fontName="Helvetica-Bold", fontSize=9,
            textColor=NAVY, spaceAfter=0.5*mm, leading=12
        ),
        "skill_val": ParagraphStyle(
            "skill_val", fontName="Helvetica", fontSize=9,
            textColor=BLACK, spaceAfter=2*mm, leading=13
        ),
        "edu_degree": ParagraphStyle(
            "edu_degree", fontName="Helvetica-Bold", fontSize=10,
            textColor=NAVY, spaceAfter=0.5*mm, leading=13
        ),
        "edu_inst": ParagraphStyle(
            "edu_inst", fontName="Helvetica", fontSize=9,
            textColor=TEAL, spaceAfter=0.3*mm, leading=12
        ),
        "edu_detail": ParagraphStyle(
            "edu_detail", fontName="Helvetica", fontSize=8.5,
            textColor=LGRAY, spaceAfter=1*mm, leading=12
        ),
        "modules": ParagraphStyle(
            "modules", fontName="Helvetica", fontSize=8.5,
            textColor=BLACK, spaceAfter=2*mm, leading=12
        ),
    }

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=2*mm, spaceBefore=0)

def section(title, s):
    return [Paragraph(title.upper(), s["section"]), rule()]

def bullet(text, s):
    return Paragraph(f"\u2022\u2002{text}", s["bullet"])

def row_table(left, right, s):
    """Two-column row: left=job info, right=date — fully readable by ATS."""
    t = Table([[left, right]], colWidths=[W - ML - MR - 40*mm, 38*mm])
    t.setStyle(TableStyle([
        ("ALIGN",    (0, 0), (0, 0), "LEFT"),
        ("ALIGN",    (1, 0), (1, 0), "RIGHT"),
        ("VALIGN",   (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING",   (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 0),
    ]))
    return t

# ── Build ─────────────────────────────────────────────────────────────────────
def build():
    s = styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT, bottomMargin=MB,
        title="Ajay Aravindan — CV",
        author="Ajay Aravindan",
        subject="Audio Post-Production | Sound Design | Digital Cinema",
        keywords="sound designer, audio post-production, dolby atmos, pro tools, digital cinema, QC, LIPA"
    )

    story = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    story.append(Paragraph("AJAY ARAVINDAN", s["name"]))
    story.append(Paragraph(
        "Audio Post-Production &amp; Sound Design | Digital Cinema &amp; Broadcast Delivery",
        s["tagline"]
    ))
    story.append(Paragraph(
        "Liverpool, United Kingdom &nbsp;|&nbsp; +44 7471 238236 &nbsp;|&nbsp; "
        "ajxarx@gmail.com &nbsp;|&nbsp; linkedin.com/in/ajxarx &nbsp;|&nbsp; "
        "Graduate Visa — Right to Work in UK &nbsp;|&nbsp; Willing to Relocate Within the UK",
        s["contact"]
    ))
    story.append(HRFlowable(width="100%", thickness=2, color=NAVY, spaceAfter=3*mm, spaceBefore=2*mm))

    # ── PERSONAL STATEMENT ───────────────────────────────────────────────────
    story += section("Personal Statement", s)
    story.append(Paragraph(
        "A motivated and ambitious Sound Technology graduate from the Liverpool Institute for Performing Arts "
        "(LIPA), specialising in audio post-production, Dolby Atmos mixing, and broadcast-compliant delivery. "
        "Complemented by a BSc in Business Administration Management from Rochester Institute of Technology, Dubai, "
        "bringing a cross-disciplinary perspective that combines creative technical excellence with professional "
        "communication and project management. Seeking an entry-level role as a runner, junior, assistant or associate "
        "in digital cinema mastering, QC, content services, or audio post-production — particularly within the UK "
        "Film and TV industry — with a strong commitment to learning and growing from experienced mentors and colleagues.",
        s["body"]
    ))

    # ── SKILLS ───────────────────────────────────────────────────────────────
    story += section("Core Skills", s)

    skills = [
        ("Post-Production & Sound Design",
         "SFX for Picture, Foley Recording & Editing, ADR, Dolby Atmos Mixing & Mastering, "
         "Re-Recording Mixer, Mixing (7.1.2, 5.1, Stereo), LtRt (LoRo) Fold-Down, Audio Conforming"),
        ("Broadcast & Cinema Delivery",
         "EBU R128 Loudness, AS-11 DPP (HD), DCP Mastering, Technical QC, EBU R123 (16ch) Track Order"),
        ("Software & Technology",
         "Pro Tools, Avid S6 Control Surface, ADR Master, Dolby Atmos Renderer, EdiLoad, "
         "Ableton Live, Adobe Premiere Pro, DaVinci Resolve, Microsoft Suite, Power BI"),
        ("Location & Production Sound",
         "Location Recording, Boom Operating, Radio Mic Fitting & Monitoring, Production Sound Assistant"),
        ("Business & Management",
         "Project Management, Client Communication, Operational Analysis, Process Improvement, "
         "Strategic Management, Sales Analysis, Team Leadership"),
    ]
    for cat, vals in skills:
        story.append(Paragraph(cat, s["skill_cat"]))
        story.append(Paragraph(vals, s["skill_val"]))

    # ── PORTFOLIO PROJECTS ───────────────────────────────────────────────────
    story += section("Portfolio Projects", s)

    projects = [
        (
            "Escape — Animated Short Film", "Sound Designer & Re-Recording Mixer · LIPA",
            "Pro Tools · Dolby Atmos 7.1.2 · EBU R128 · AS-11 DPP (HD) · EBU R123 (16ch) · 5.1 · LtRt Fold-Down",
            [
                "Mixed a short animated film in Dolby Atmos, delivering a full spatial audio experience to professional broadcast standards.",
                "Re-rendered the Atmos mix to 5.1 and LtRt (LoRo) fold-down formats, ensuring compatibility across all distribution platforms.",
                "Achieved EBU R128 loudness target and exported final stems to AS-11 DPP (HD) format, conforming to EBU R123 (16ch) track order — meeting full broadcast delivery requirements.",
            ]
        ),
        (
            "Flow — Animated Feature Film", "Sound Designer & Re-Recording Mixer · LIPA",
            "Pro Tools · Dolby Atmos 7.1.2 · 5.1 Surround · Foley · ADR · Music Integration",
            [
                "Delivered complete sound design, Foley recording and editing, and original music integration for the full-length animated feature Flow.",
                "Mixed the film to 7.1.2 Dolby Atmos, creating an immersive spatial audio experience.",
                "Folded down to a 5.1 surround version, demonstrating versatility across immersive and standard delivery formats.",
            ]
        ),
        (
            "Superman Comic Book Audio Experience", "Sound Designer & Mixer · LIPA",
            "Pro Tools · 5.1 Surround · Stereo Fold-Down · ADR · SFX · Foley · Music Design",
            [
                "Conceived and produced a fully synchronised audio experience designed to accompany a Superman comic book, allowing readers to listen along page-by-page.",
                "Delivered complete sound design covering Music, ADR, Foley, and SFX, creating an immersive audio narrative matching the visual pacing and tone of the comic.",
                "Mixed to 5.1 surround with a fold-down stereo version, demonstrating versatility in both immersive and standard audio delivery formats.",
            ]
        ),
    ]

    for title, role, tools, bullets in projects:
        story.append(Paragraph(title, s["job_title"]))
        story.append(Paragraph(role, s["job_org"]))
        story.append(Paragraph(f"Tools & Standards: {tools}", s["edu_detail"]))
        for b in bullets:
            story.append(bullet(b, s))
        story.append(Spacer(1, 2*mm))

    # ── EXPERIENCE ───────────────────────────────────────────────────────────
    story += section("Professional Experience", s)

    experience = [
        (
            "Sound Technician (Freelance Full-Time)",
            "Ajay Freelancer Events Management · Abu Dhabi, UAE",
            "October 2021 – September 2023",
            [
                "Engineered audio systems ensuring production requirements were met to a professional standard, demonstrating attention to detail and high standards.",
                "Worked directly with clients throughout pre-production and setup phases to develop personalised sound mixes, determine technical requirements, and establish project design briefs.",
                "Assisted and shadowed sound supervisor on multiple productions and shows, supporting with radio mic deployment and monitoring.",
                "Achieved audio integrity throughout productions for multiple client organisations, leading to referrals from employers to new clients.",
                "Developed strong working knowledge of live PA systems, including system design, signal routing, and troubleshooting.",
                "Implemented system designs for small-scale corporate events, demonstrating ability to execute, apply learned skills, and lead projects.",
            ]
        ),
        (
            "Project Management Consultant (Full-Time)",
            "Digital Qatalyst · Dubai, UAE",
            "November 2021 – February 2022",
            [
                "Assessed operational challenges across client organisations and delivered tailored solutions aimed at improving organisational development.",
                "Prepared and presented reports and recommendations to clients, drawing on data analysis using Microsoft Excel and Power BI.",
                "Served as primary point of contact for a portfolio of clients, providing timely and professional responses to enquiries.",
            ]
        ),
        (
            "Retail Staff (Part-Time)",
            "Liverpool FC Stadium & Everton FC Stadium · Liverpool, UK",
            "2024 – Present",
            []
        ),
    ]

    for title, org, date, bullets in experience:
        left = Paragraph(title, s["job_title"])
        right = Paragraph(date, s["date"])
        story.append(row_table(left, right, s))
        story.append(Paragraph(org, s["job_org"]))
        for b in bullets:
            story.append(bullet(b, s))
        story.append(Spacer(1, 2*mm))

    # ── EDUCATION ────────────────────────────────────────────────────────────
    story += section("Education", s)

    edu = [
        (
            "BA (Hons) Sound Technology — Graduated July 2026",
            "Liverpool Institute for Performing Arts (LIPA)",
            "Liverpool, United Kingdom · September 2023 – July 2026",
            "Audio Production, Acoustics, Live Engineering, Audio Post-Production, SFX Designing, "
            "Foley Recording & Editing, ADR, Location Recording, Mixing (7.1, 5.1, LtRt), "
            "Audio Conforming, Technical QC, EBU Standards, DCP Mastering, Video Production."
        ),
        (
            "BSc (Hons) Business Administration Management — Graduated June 2020",
            "Rochester Institute of Technology",
            "Dubai, United Arab Emirates · September 2016 – June 2020",
            "Operational Analysis, Project & Strategic Management, Organisational Effectiveness, "
            "Communication, Ad-Hoc Management. Interned in buying and operations roles; "
            "briefly worked as a Project Management Consultant."
        ),
    ]

    for degree, inst, location, modules in edu:
        story.append(Paragraph(degree, s["edu_degree"]))
        story.append(Paragraph(inst, s["edu_inst"]))
        story.append(Paragraph(location, s["edu_detail"]))
        story.append(Paragraph(f"Key Areas: {modules}", s["modules"]))
        story.append(Spacer(1, 1*mm))

    # ── ADDITIONAL ───────────────────────────────────────────────────────────
    story += section("Additional Information", s)
    story.append(Paragraph(
        "<b>Availability:</b> Fully available for shift-based working including nights, weekends, and public holidays. "
        "Open to shift rotas and comprehensive on-the-job training.",
        s["body"]
    ))
    story.append(Paragraph(
        "<b>Right to Work:</b> UK Graduate Visa — full right to work in the United Kingdom.",
        s["body"]
    ))
    story.append(Paragraph(
        "<b>Location:</b> Based in Liverpool, UK. Willing to relocate anywhere within the UK for any opportunity.",
        s["body"]
    ))

    doc.build(story)
    print(f"CV generated: {OUTPUT}")

if __name__ == "__main__":
    build()
