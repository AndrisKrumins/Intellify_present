from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Intellify Web Presentation",
    page_icon="🏢",
    layout="wide",
)

# ---------- PATHS ----------
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

WARNINGS_IMG = ASSETS_DIR / "Warnings.png"
WARNINGS1_IMG = ASSETS_DIR / "Warnings1.png"
ABCD_IMG = ASSETS_DIR / "ABCD_1.png"
ABCD1_IMG = ASSETS_DIR / "ABCD_2.png"
HEATING_IMG = ASSETS_DIR / "Heating_cons.png"
ELECTRICAL_IMG = ASSETS_DIR / "Electrical_cons.png"
SANKEY1_IMG = ASSETS_DIR / "sankey_1.png"
SANKEY2_IMG = ASSETS_DIR / "sankey_2.png"

TIME_SCH = ASSETS_DIR / "Schedule.png"
CHANGE = ASSETS_DIR / "Change.png"
ALG_SEND = ASSETS_DIR / "Alg_send.png"
PROGN = ASSETS_DIR / "Predict.png"

TECHN_ASSET = ASSETS_DIR / "Intellify_main_devices.png"
TECHN_DATA = Path("/mnt/data/Intellify_main_devices.png")
MAIN_DEVICES_IMG = TECHN_ASSET if TECHN_ASSET.exists() else TECHN_DATA

# DIGITAL_TWIN_IMG = Path("/mnt/data/Wisdom_data.png")
DIGITAL_TWIN_IMG = ASSETS_DIR / "Wisdom_data.png"

# ---------- THEME ----------
BG = "#22344d"
SURFACE = "#2b3f5c"
SURFACE_ALT = "#334a6b"
BORDER = "rgba(255,255,255,0.10)"
TEXT = "#ffffff"
MUTED = "#c8d6e5"
ACCENT = "#00e5ff"
ACCENT_2 = "#7ee7ff"
SUCCESS = "#79e2a0"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;800&display=swap');

    :root {{
        --bg: {BG};
        --surface: {SURFACE};
        --surface-alt: {SURFACE_ALT};
        --border: {BORDER};
        --text: {TEXT};
        --muted: {MUTED};
        --accent: {ACCENT};
        --accent-2: {ACCENT_2};
        --success: {SUCCESS};
    }}

    html, body, [class*="css"] {{
        font-family: 'Raleway', sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(circle at top right, rgba(0,229,255,0.10), transparent 20%),
            linear-gradient(180deg, #243650 0%, #1e2d43 100%);
        color: var(--text);
    }}

    .block-container {{
        max-width: 1280px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #1e2d43 0%, #21324a 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }}

    .hero {{
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(0,229,255,0.06));
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 2rem 2rem 1.8rem 2rem;
        margin-bottom: 1.3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    }}

    .hero::after {{
        content: "";
        position: absolute;
        top: -40px;
        right: -40px;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(0,229,255,0.18), transparent 65%);
        pointer-events: none;
    }}

    .eyebrow {{
        display: inline-block;
        color: var(--accent);
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }}

    .hero h1 {{
        margin: 0;
        font-size: 3rem;
        line-height: 1.0;
        color: var(--text);
        letter-spacing: 0.08em;
        font-weight: 800;
    }}

    .hero-subtitle {{
        color: var(--accent-2);
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 0.45rem;
        margin-bottom: 0.9rem;
    }}

    .hero p {{
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.6;
        margin: 0;
        max-width: 900px;
    }}

    .section-wrap {{
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }}

    .section-title {{
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.15;
        color: var(--text);
        margin-bottom: 0.2rem;
    }}

    .section-subtitle {{
        color: var(--accent-2);
        font-size: 1.02rem;
        line-height: 1.5;
        margin-bottom: 0.2rem;
        max-width: 980px;
    }}

    .card {{
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1.1rem;
        min-height: 190px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.14);
        margin-bottom: 1rem;
    }}

    .card.alt {{
        background: linear-gradient(180deg, rgba(0,229,255,0.08), rgba(255,255,255,0.03));
    }}

    .card-icon {{
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0,229,255,0.10);
        border: 1px solid rgba(0,229,255,0.18);
        color: var(--accent);
        font-size: 1.1rem;
        margin-bottom: 0.9rem;
    }}

    .card h4 {{
        color: var(--text);
        margin: 0 0 0.45rem 0;
        font-size: 1.05rem;
        line-height: 1.3;
    }}

    .card p {{
        color: var(--muted);
        margin: 0;
        line-height: 1.55;
        font-size: 0.96rem;
    }}

    .metric-card {{
        background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1rem 1rem 0.9rem 1rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        margin-bottom: 0.7rem;
    }}

    .metric-label {{
        color: var(--muted);
        font-size: 0.86rem;
        margin-bottom: 0.35rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 700;
    }}

    .metric-value {{
        color: var(--text);
        font-size: 2rem;
        font-weight: 800;
        line-height: 1;
    }}

    .metric-delta {{
        color: var(--accent-2);
        font-size: 0.92rem;
        margin-top: 0.45rem;
        font-weight: 600;
    }}

    .pill {{
        background: linear-gradient(135deg, rgba(0,229,255,0.14), rgba(255,255,255,0.06));
        border: 1px solid rgba(0,229,255,0.20);
        border-radius: 999px;
        padding: 0.55rem 0.9rem;
        text-align: center;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.8rem;
    }}

    .timeline-step {{
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1rem;
        min-height: 220px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
    }}

    .timeline-index {{
        width: 34px;
        height: 34px;
        border-radius: 999px;
        background: rgba(0,229,255,0.14);
        border: 1px solid rgba(0,229,255,0.20);
        color: var(--accent);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        margin-bottom: 0.8rem;
    }}

    .timeline-title {{
        color: var(--text);
        font-weight: 700;
        margin-bottom: 0.45rem;
        font-size: 1rem;
    }}

    .timeline-body {{
        color: var(--muted);
        font-size: 0.95rem;
        line-height: 1.5;
    }}

    .compare-label {{
        color: var(--accent-2);
        font-weight: 800;
        margin: 0.9rem 0 0.5rem 0;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-size: 0.85rem;
    }}

    .compare-box {{
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1rem;
        min-height: 120px;
        margin-bottom: 0.8rem;
    }}

    .compare-box.right {{
        background: linear-gradient(180deg, rgba(0,229,255,0.08), rgba(255,255,255,0.03));
    }}

    .compare-box p {{
        color: var(--muted);
        margin: 0;
        line-height: 1.5;
    }}

    .gallery-shell {{
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.14);
        margin-bottom: 1rem;
    }}

    .gallery-caption {{
        color: var(--text);
        font-weight: 700;
        margin-top: 0.75rem;
        margin-bottom: 0.25rem;
        font-size: 1rem;
    }}

    .gallery-desc {{
        color: var(--muted);
        font-size: 0.94rem;
        line-height: 1.5;
    }}

    .gallery-note {{
        color: var(--accent-2);
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }}

    .modal-bg {{
        background: rgba(0,0,0,0.35);
        backdrop-filter: blur(6px);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 24px;
        padding: 2rem;
    }}

    .modal-card {{
        max-width: 420px;
        margin: 0 auto;
        background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        text-align: center;
    }}

    .modal-title {{
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
        color: var(--text);
    }}

    .modal-sub {{
        color: var(--muted);
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
        line-height: 1.5;
    }}

    .tech-pill {{
        background: linear-gradient(135deg, rgba(0,229,255,0.12), rgba(255,255,255,0.05));
        border: 1px solid rgba(0,229,255,0.18);
        border-radius: 14px;
        padding: 0.8rem 0.9rem;
        color: var(--text);
        font-weight: 600;
        font-size: 0.94rem;
        margin-bottom: 0.7rem;
    }}

    .dt-input {{
        background: linear-gradient(135deg, rgba(0,229,255,0.12), rgba(255,255,255,0.05));
        border: 1px solid rgba(0,229,255,0.18);
        border-radius: 14px;
        padding: 0.8rem 0.9rem;
        color: var(--text);
        font-weight: 600;
        font-size: 0.94rem;
        margin-bottom: 0.7rem;
    }}

    div[data-testid="stTextInput"] input {{
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        color: white !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"] {{
        margin-bottom: 0.65rem;
    }}

    div[data-testid="stTextInput"] label {{
        display: none !important;
    }}

    .footer {{
        color: var(--muted);
        text-align: center;
        margin-top: 1.8rem;
        font-size: 0.9rem;
        opacity: 0.9;
    }}

    div[data-baseweb="tab-list"] {{
        gap: 0.5rem;
    }}

    button[data-baseweb="tab"] {{
        background: rgba(255,255,255,0.04) !important;
        border-radius: 12px !important;
        padding: 0.55rem 1rem !important;
    }}

    .stLinkButton a {{
        background: linear-gradient(135deg, #00e5ff, #7ee7ff) !important;
        color: #0b1c2c !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        border: none !important;
        box-shadow: 0 10px 24px rgba(0,229,255,0.24) !important;
        text-decoration: none !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

DECK = [
    {
        "type": "title",
        "title": "INTELLIFY",
        "subtitle": "Empower buildings with intelligent data solutions",
        "hero_text": "Digital infrastructure, HVAC optimisation and portfolio intelligence for modern buildings.",
        "hero_subtext": "From controls and standardisation to connected, data-driven building operations.",
        "footer": "Company overview",
    },
    {
        "type": "timeline",
        "title": "A five-stage path from controls to connected buildings",
        "subtitle": "Tested way for turning fragmented building systems into an integrated service platform",
        "items": [
            {"title": "Standardisation", "body": "Automation libraries, technical documentation, data points and communication standards."},
            {"title": "Automation", "body": "HVAC logic, BMS improvements and controller configuration for reliable local control."},
            {"title": "Digitalisation", "body": "Data transfer infrastructure, cloud ingestion, dashboards and technician visibility."},
            {"title": "Cloud computing", "body": "ML-supported HVAC management, analytics and predictive service workflows."},
            {"title": "Connected buildings", "body": "Alarms, reporting, portfolio oversight, energy-price logic and grid-ready services."},
        ],
        "footer": "Platform evolution",
    },
    {
        "type": "cards",
        "title": "Client benefits across the full building lifecycle",
        "subtitle": "Operational, financial and ESG value built on top of open building data",
        "cols": 2,
        "items": [
            {"title": "Lower energy use", "body": "Optimise HVAC operation using real building data, schedules and climate feedback."},
            {"title": "Improved maintenance", "body": "Detect faults earlier, prioritise service actions and reduce avoidable site visits."},
            {"title": "Stronger ESG reporting", "body": "Use reliable energy and indoor-climate data for reporting and compliance support."},
            {"title": "Open data foundation", "body": "Expose data points and visualise the building clearly for technicians and managers."},
            {"title": "Portfolio visibility", "body": "Monitor multiple sites consistently from the cloud instead of building by building."},
            {"title": "Better commercial control", "body": "Support pricing logic, service transparency and scalable long-term operations."},
        ],
        "footer": "Client value proposition",
    },
    {
        "type": "compare",
        "title": "Platform as a Service vs. traditional building software",
        "subtitle": "Local control remains in the building while cloud services improve scalability and visibility",
        "left_title": "Traditional software",
        "right_title": "PaaS (Intellify)",
        "rows": [
            {"label": "Deployment", "left": "Manual configuration and rollout for each building.", "right": "Cloud-based onboarding with a repeatable assess-and-discover model."},
            {"label": "Maintenance", "left": "Heavy dependency on internal IT and fragmented updates.", "right": "Vendor-managed updates and centrally maintained services."},
            {"label": "Scalability", "left": "Adding buildings is slow and project-heavy.", "right": "Easy scaling across devices, sites and portfolios."},
            {"label": "Integration", "left": "Custom integration work for each BMS or data source.", "right": "Built-in pathways for BMS, IoT and cloud data connections."},
        ],
        "footer": "Operating model comparison",
    },
    {
        "type": "modules",
        "title": "Core solution modules",
        "subtitle": "A modular platform that supports meter data, indoor climate, analytics and portfolio control",
        "items": [
            {"title": "Smart Energy Meter Management", "body": "Centralize and validate energy consumption data through remote meter readings and custom export options."},
            {"title": "Indoor Climate Intelligence", "body": "Real-time climate insights and expert evaluations for a healthier, more comfortable and well-controlled indoor environment."},
            {"title": "Building Systems Supervisor", "body": "Centralize HVAC systems, track performance and manage maintenance to ensure a top service standard."},
            {"title": "Energy & Efficiency Oversight", "body": "Transform scattered energy data into clear monitoring of energy use, CO₂ footprint and ESG performance."},
            {"title": "Portfolio Energy & Asset Suite", "body": "Gain a unified overview of energy, CO₂ and system status to guide smarter budgeting, planning and sustainability decisions."},
            {"title": "HVAC Performance Optimiser", "body": "Machine learning algorithms continuously fine-tune performance to cut energy costs while maintaining good indoor conditions."},
        ],
        "footer": "Solution modules",
    },
    {
        "type": "cards",
        "title": "Business priorities: own software, hardware-ready integration and price-efficient delivery",
        "subtitle": "Three coordinated decision areas define platform readiness and scale potential",
        "cols": 3,
        "items": [
            {"title": "Software", "body": "Cloud software located in a secure data centre with a high level of security."},
            {"title": "Hardware", "body": "Wago and Modberry libraries with BACnet, Modbus, M-Bus, W-MBus and LoRa support."},
            {"title": "Sales readiness", "body": "System is tested in multiple Latvian projects."},
        ],
        "footer": "Business decision areas",
    },
    {
        "type": "technical",
        "title": "Technical solutions",
        "subtitle": "Intellify uses two main devices — Modberry and Wago — to connect building systems, integrate field data and enable advanced control logic.",
        "image": MAIN_DEVICES_IMG,
        "description": (
            "These edge devices form the hardware foundation of the Intellify solution. "
            "They support open protocol connectivity, local HVAC logic execution, remote service access "
            "and seamless data delivery to the Intellify platform for visualisation and reporting."
        ),
        "possibilities": [
            "BACnet data integration",
            "BACnet data reporting",
            "Modbus data integration",
            "LoRa data integration",
            "W-MBus and M-Bus data integration",
            "HVAC logic",
            "Remote programming",
            "Data visualisation via Intellify",
        ],
        "footer": "Technical solutions overview",
    },
    {
        "type": "digital_twin",
        "title": "Digital twin",
        "subtitle": "We are ready to create a building digital twin and calculate annual energy-saving potential by improving building control algorithms and operational strategy.",
        "image": DIGITAL_TWIN_IMG,
        "description": (
            "Using a digital twin approach, Intellify can evaluate how building control changes affect annual "
            "energy performance, comfort and operational efficiency. This helps identify realistic savings "
            "before implementation and supports better technical and financial decision-making."
        ),
        "inputs": [
            "Building geometrical data",
            "Building location",
            "U-values",
            "Engineering systems",
            "Working hours",
            "Monthly electricity consumption",
            "Monthly heating consumption",
        ],
        "footer": "Digital twin readiness",
    },
    {
        "type": "architecture",
        "title": "Architecture for a connected building PaaS",
        "subtitle": "System consists of field devices, integrations, cloud analytics and a user-friendly interface",
        "items": [
            {"title": "Connectivity layer", "body": "IoT device connections to LoRaWAN and Intellify PaaS reduce wiring effort while maintaining high data coverage."},
            {"title": "Integration layer", "body": "Integrates with BMS, metering, HVAC nodes and different APIs."},
            {"title": "Data + ML engine", "body": "Normalise data, detect inefficiencies and support optimisation decisions."},
            {"title": "Applications", "body": "Dashboards, alarms, reporting, optimisation and portfolio management services."},
        ],
        "footer": "Reference architecture",
    },
    {
        "type": "gallery",
        "title": "Platform screenshots",
        "subtitle": "Sample pictures from the Intellify interface",
        "cols": 2,
        "items": [
            {"image": HEATING_IMG, "title": "Heating consumption", "body": "Heating energy consumption review."},
            {"image": ELECTRICAL_IMG, "title": "Electrical consumption", "body": "Electrical energy consumption review."},
            {"image": ABCD_IMG, "title": "Efficiency view", "body": "Building efficiency assessment."},
            {"image": ABCD1_IMG, "title": "Climate view", "body": "Building climate assessment."},
            {"image": WARNINGS_IMG, "title": "Warnings overview", "body": "Warning cards with activity and resolution metrics."},
            {"image": WARNINGS1_IMG, "title": "Issue monitoring", "body": "Monitoring workflow and technical review."},
            {"image": SANKEY1_IMG, "title": "Sankey flow 1", "body": "Energy flow visualisation across building systems."},
            {"image": SANKEY2_IMG, "title": "Sankey flow 2", "body": "Additional flow breakdown for analysis."},
            {"image": TIME_SCH, "title": "Time schedules", "body": "Time scheduler for a specific HVAC unit."},
            {"image": CHANGE, "title": "Parameter change", "body": "Parameter change for a specific HVAC unit."},
            {"image": ALG_SEND, "title": "Algorithm send", "body": "Prediction algorithm message for the time scheduler."},
            {"image": PROGN, "title": "Algorithm prediction & reality", "body": "Temperature prediction and on-time activation with delay."},
        ],
        "footer": "Sample UI pictures",
    },
    {
        "type": "login_cta",
        "title": "Access the Intellify platform",
        "subtitle": "Move from presentation into live product experience",
        "footer": "Live platform entry point",
    },
]

ICON_MAP = {
    "Lower energy use": "⚡",
    "Improved maintenance": "🛠️",
    "Stronger ESG reporting": "📊",
    "Open data foundation": "🗂️",
    "Portfolio visibility": "🏢",
    "Better commercial control": "📈",
    "Smart Energy Meter Management": "🔌",
    "Indoor Climate Intelligence": "🌡️",
    "Building Systems Supervisor": "🧩",
    "Energy & Efficiency Oversight": "📉",
    "Portfolio Energy & Asset Suite": "🧭",
    "HVAC Performance Optimiser": "🚀",
    "Software": "💻",
    "Hardware": "🖧",
    "Sales readiness": "🤝",
    "Connectivity layer": "📶",
    "Integration layer": "🔗",
    "Data + ML engine": "🧠",
    "Applications": "🖥️",
}


def section_header(title: str, subtitle: str = ""):
    st.markdown(
        f"""
        <div class="section-wrap">
            <div class="section-title">{title}</div>
            {f'<div class="section-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, delta: str = ""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            {f'<div class="metric-delta">{delta}</div>' if delta else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def card(title: str, body: str, alt: bool = False, icon: str = "✦"):
    klass = "card alt" if alt else "card"
    st.markdown(
        f"""
        <div class="{klass}">
            <div class="card-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def image_card(image_path: Path, title: str, body: str):
    with st.container():
        st.markdown('<div class="gallery-shell">', unsafe_allow_html=True)
        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        else:
            st.warning(f"Image not found: {image_path.name}")
            st.markdown(
                '<div class="gallery-note">Place the file in the assets folder to display it here.</div>',
                unsafe_allow_html=True,
            )
        st.markdown(f'<div class="gallery-caption">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="gallery-desc">{body}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


def render_technical_slide(slide):
    section_header(slide["title"], slide.get("subtitle", ""))

    left, right = st.columns([1.25, 1])

    with left:
        if slide["image"].exists():
            st.image(str(slide["image"]), use_container_width=True)
        else:
            st.warning("Technical solutions image not found.")
        st.markdown(
            f'<div class="gallery-desc" style="margin-top:0.8rem;">{slide["description"]}</div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            '<div class="pill">Main devices: Modberry + Wago</div>',
            unsafe_allow_html=True,
        )
        for item in slide["possibilities"]:
            st.markdown(
                f'<div class="tech-pill">{item}</div>',
                unsafe_allow_html=True,
            )


def render_digital_twin_slide(slide):
    section_header(slide["title"], slide.get("subtitle", ""))

    left, right = st.columns([1.15, 1])

    with left:
        if slide["image"].exists():
            st.image(str(slide["image"]), use_container_width=True)
        else:
            st.warning("Digital twin image not found.")

        st.markdown(
            f'<div class="gallery-desc" style="margin-top:0.8rem;">{slide["description"]}</div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            '<div class="pill">Input data required for digital twin</div>',
            unsafe_allow_html=True,
        )

        for item in slide["inputs"]:
            st.markdown(
                f'<div class="dt-input">{item}</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div style="margin-top:0.8rem; color:#7ee7ff; font-size:0.95rem; line-height:1.5;">
                Result: estimated annual energy savings from improved HVAC control algorithms and building strategy.
            </div>
            """,
            unsafe_allow_html=True,
        )


def kpi_row():
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Energy savings", "18%", "+6% YoY")
    with c2:
        metric_card("Maintenance reduction", "-25%", "-8% site visits")
    with c3:
        metric_card("CO₂ reduction", "-20%", "ESG aligned")
    with c4:
        metric_card("Existing portfolio", "24 buildings")


def render_login_cta():
    section_header(
        "Access the Intellify platform",
        "Move from presentation into live product experience",
    )

    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(
            """
            <div class="modal-bg">
                <div class="modal-card">
                    <div class="modal-title">Login preview</div>
                    <div class="modal-sub">Secure platform access</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.text_input(
            "Email",
            placeholder="Email",
            disabled=True,
            label_visibility="collapsed",
            key="login_email_preview",
        )
        st.text_input(
            "Password",
            placeholder="Password",
            disabled=True,
            type="password",
            label_visibility="collapsed",
            key="login_password_preview",
        )
        st.link_button(
            "Open Intellify Platform",
            "https://app2.intellify.lv/login",
            use_container_width=True,
        )

    st.markdown(
        '<div style="text-align:center; margin-top:0.7rem; font-size:0.8rem; color:#8fa6bf;">Demo preview • secure login required</div>',
        unsafe_allow_html=True,
    )


def render_slide(slide):
    if slide["type"] == "title":
        section_header(slide["title"], slide.get("subtitle", ""))

        c1, c2, c3 = st.columns(3)
        with c1:
            metric_card("Platform maturity stages", "5")
        with c2:
            metric_card("Core solution modules", "6")
        with c3:
            metric_card("Portfolio-wide view", "1 unified layer")

        st.markdown("<div style='height: 0.6rem;'></div>", unsafe_allow_html=True)
        st.subheader(slide.get("hero_text", ""))
        st.markdown(
            f"<p style='color:{MUTED}; font-size:1.02rem; line-height:1.7;'>{slide.get('hero_subtext', '')}</p>",
            unsafe_allow_html=True,
        )

    elif slide["type"] == "timeline":
        section_header(slide["title"], slide.get("subtitle", ""))
        cols = st.columns(len(slide["items"]))
        for i, item in enumerate(slide["items"]):
            with cols[i]:
                st.markdown(
                    f"""
                    <div class="timeline-step">
                        <div class="timeline-index">{i + 1}</div>
                        <div class="timeline-title">{item["title"]}</div>
                        <div class="timeline-body">{item["body"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    elif slide["type"] == "cards":
        section_header(slide["title"], slide.get("subtitle", ""))
        cols_n = slide.get("cols", 2)
        items = slide["items"]

        for start in range(0, len(items), cols_n):
            cols = st.columns(cols_n)
            for i, item in enumerate(items[start:start + cols_n]):
                with cols[i]:
                    card(
                        item["title"],
                        item["body"],
                        alt=bool((start + i) % 2),
                        icon=ICON_MAP.get(item["title"], "✦"),
                    )

    elif slide["type"] == "compare":
        section_header(slide["title"], slide.get("subtitle", ""))

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="pill">{slide["left_title"]}</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="pill">{slide["right_title"]}</div>', unsafe_allow_html=True)

        for row in slide["rows"]:
            st.markdown(f'<div class="compare-label">{row["label"]}</div>', unsafe_allow_html=True)
            l, r = st.columns(2)
            with l:
                st.markdown(
                    f'<div class="compare-box"><p>{row["left"]}</p></div>',
                    unsafe_allow_html=True,
                )
            with r:
                st.markdown(
                    f'<div class="compare-box right"><p>{row["right"]}</p></div>',
                    unsafe_allow_html=True,
                )

    elif slide["type"] == "modules":
        section_header(slide["title"], slide.get("subtitle", ""))
        items = slide["items"]

        for start in range(0, len(items), 3):
            cols = st.columns(3)
            for i, item in enumerate(items[start:start + 3]):
                with cols[i]:
                    card(
                        item["title"],
                        item["body"],
                        alt=bool((start + i) % 2),
                        icon=ICON_MAP.get(item["title"], "✦"),
                    )

        st.markdown("### Pricing reference")
        st.link_button(
            "Open pricing link",
            "https://docs.google.com/document/d/1gBxRWfA02gND9ZbkNRwOEhrsmDsxwW0pzpRN1DyvRoI/edit?tab=t.0",
        )

    elif slide["type"] == "technical":
        render_technical_slide(slide)

    elif slide["type"] == "digital_twin":
        render_digital_twin_slide(slide)

    elif slide["type"] == "architecture":
        section_header(slide["title"], slide.get("subtitle", ""))
        cols = st.columns(4)
        for i, item in enumerate(slide["items"]):
            with cols[i]:
                card(
                    item["title"],
                    item["body"],
                    alt=bool(i % 2),
                    icon=ICON_MAP.get(item["title"], "✦"),
                )

    elif slide["type"] == "gallery":
        section_header(slide["title"], slide.get("subtitle", ""))
        cols_n = slide.get("cols", 2)
        items = slide["items"]

        for start in range(0, len(items), cols_n):
            cols = st.columns(cols_n)
            for i, item in enumerate(items[start:start + cols_n]):
                with cols[i]:
                    image_card(item["image"], item["title"], item["body"])

    elif slide["type"] == "login_cta":
        render_login_cta()

    st.markdown(
        f'<div class="footer">{slide.get("footer", "Intellify")} • IntellifyTech.com</div>',
        unsafe_allow_html=True,
    )


# ---------- HERO ----------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Building intelligence platform</div>
        <h1>INTELLIFY</h1>
        <div class="hero-subtitle">Empower buildings with intelligent data solutions</div>
        <p>
            Digital infrastructure, HVAC optimisation and portfolio intelligence for modern buildings.
            From controls and standardisation to connected, data-driven building operations.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- TABS ----------
tab_overview, tab_value, tab_modules, tab_tech, tab_digital_twin, tab_arch, tab_gallery, tab_access = st.tabs(
    ["Overview", "Value", "Modules", "Technical solutions", "Digital twin", "Architecture", "Screenshots", "Access"]
)

with tab_overview:
    kpi_row()
    render_slide(DECK[0])
    render_slide(DECK[1])

with tab_value:
    render_slide(DECK[2])
    render_slide(DECK[3])

with tab_modules:
    render_slide(DECK[4])
    render_slide(DECK[5])

with tab_tech:
    render_slide(DECK[6])

with tab_digital_twin:
    render_slide(DECK[7])

with tab_arch:
    render_slide(DECK[8])

with tab_gallery:
    render_slide(DECK[9])

with tab_access:
    render_slide(DECK[10])