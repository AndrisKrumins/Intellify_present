import streamlit as st

st.set_page_config(
    page_title="Intellify Web Presentation",
    page_icon="🏢",
    layout="wide",
)

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
        letter-spacing: 0.02em;
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
        padding: 1.1rem 1.1rem 1rem 1.1rem;
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
        position: relative;
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

    .bullet-box {{
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 1.3rem 1.4rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }}

    .bullet-item {{
        display: flex;
        gap: 0.8rem;
        align-items: flex-start;
        color: var(--muted);
        line-height: 1.6;
        margin-bottom: 0.8rem;
        font-size: 1rem;
    }}

    .bullet-dot {{
        color: var(--success);
        font-weight: 900;
        font-size: 1rem;
        line-height: 1.5;
    }}

    .modal-overlay {{
        position: relative;
        margin-top: 1rem;
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

    /* Streamlit inputs for login preview */
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
        "subtitle": "A practical roadmap for turning fragmented building systems into an integrated service platform",
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
            {"title": "Energy Meter Management", "body": "Meter data collection, export and integration support for multi-building environments."},
            {"title": "Climate Management", "body": "Indoor climate monitoring with clear visualisation and professional assessment."},
            {"title": "Technical Node Manager", "body": "Flexible device and field integration for HVAC service and automation teams."},
            {"title": "Analytics", "body": "Reliable building data, frequent transmission and support for legacy automation systems."},
            {"title": "Portfolio Manager", "body": "Single source of truth across buildings with transparency and management visibility."},
            {"title": "HVAC Performance Optimiser", "body": "Data-driven savings, ROI visibility, climate stability and equipment protection."},
        ],
        "footer": "Solution modules",
    },
    {
        "type": "cards",
        "title": "Business priorities: software, hardware and commercial model",
        "subtitle": "Three coordinated decision areas define platform readiness and scale potential",
        "cols": 3,
        "items": [
            {"title": "Software foundation", "body": "Server security, backend improvements, database logic, migration and ML enablement."},
            {"title": "Hardware enablement", "body": "Wago and Modberry libraries, BACnet support, LoRa workflows and field integration."},
            {"title": "Commercial model", "body": "Pricing policy, fast installation, scalable rollout and repeatable service delivery."},
            {"title": "Legacy transition", "body": "Move older platform components into a cleaner and more maintainable architecture."},
            {"title": "Protocol strategy", "body": "Leverage LoRa and related communication layers for efficient building connectivity."},
            {"title": "Sales readiness", "body": "Align product packaging and value messaging with the new platform capabilities."},
        ],
        "footer": "Business decision areas",
    },
    {
        "type": "architecture",
        "title": "Reference architecture for a connected-building PaaS",
        "subtitle": "A layered architecture linking field devices, integrations, cloud analytics and user-facing workflows",
        "items": [
            {"title": "Connectivity layer", "body": "LoRaWAN and field connectivity reduce wiring effort and extend data coverage."},
            {"title": "Integration hub", "body": "Bring together BMS, metering, HVAC nodes and IoT data into one platform layer."},
            {"title": "Data + ML engine", "body": "Normalise data, detect inefficiencies and support optimisation decisions."},
            {"title": "Applications", "body": "Dashboards, alarms, reporting, optimisation and portfolio management services."},
        ],
        "footer": "Reference architecture",
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
    "Energy Meter Management": "🔌",
    "Climate Management": "🌡️",
    "Technical Node Manager": "🧩",
    "Analytics": "📉",
    "Portfolio Manager": "🧭",
    "HVAC Performance Optimiser": "🚀",
    "Software foundation": "💻",
    "Hardware enablement": "🖧",
    "Commercial model": "💼",
    "Legacy transition": "🔄",
    "Protocol strategy": "📡",
    "Sales readiness": "🤝",
    "Connectivity layer": "📶",
    "Integration hub": "🔗",
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


def kpi_row():
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Energy savings", "18%", "+6% YoY")
    with c2:
        metric_card("Maintenance reduction", "-25%", "-8% site visits")
    with c3:
        metric_card("CO₂ reduction", "-32%", "ESG aligned")
    with c4:
        metric_card("Portfolio coverage", "24 buildings", "+6 connected")


def render_login_cta():
    section_header(
        "Access the Intellify platform",
        "Move from presentation into live product experience",
    )

    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(
            """
            <div class="modal-overlay">
                <div class="modal-bg">
                    <div class="modal-card">
                        <div class="modal-title">Login preview</div>
                        <div class="modal-sub">Secure platform access</div>
                    </div>
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
                        <div class="timeline-index">{i+1}</div>
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
tab_overview, tab_value, tab_modules, tab_arch = st.tabs(
    ["Overview", "Value", "Modules", "Architecture"]
)

with tab_overview:
    kpi_row()
    render_slide(DECK[0])
    render_slide(DECK[1])

with tab_value:
    render_slide(DECK[2])
    render_slide(DECK[3])
    render_slide(DECK[7])

with tab_modules:
    render_slide(DECK[4])
    render_slide(DECK[5])

with tab_arch:
    render_slide(DECK[6])