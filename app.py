
import streamlit as st

# =========================================================
# CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AeroSense AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# GLOBAL DARK THEME
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #080B0A;
    --surface: #111815;
    --surface2: #151F1A;
    --border: #25372D;
    --green: #8CCF9B;
    --teal: #4CA99A;
    --white: #EDF5EF;
    --muted: #91A397;
}

.stApp {
    background: var(--bg);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2.4rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0B110E;
    border-right: 1px solid #1D2C23;
}

section[data-testid="stSidebar"] * {
    color: #DCE9DF;
}

section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
    border-radius: 9px;
    margin: 5px 0;
}

section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {
    background: #1B2B21;
}

section[data-testid="stSidebar"] [aria-current="page"] {
    background: #20352A;
    border-left: 3px solid #8CCF9B;
}

/* TEXT */

h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: var(--white) !important;
}

p, li, label {
    color: #C0CEC3;
}

.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--muted) !important;
}

/* BRAND */

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #EDF5EF;
}

.brand-dot {
    color: #8CCF9B;
}

.brand-sub {
    color: #82978A;
    font-size: 11px;
    letter-spacing: 2px;
    margin-top: 5px;
}

.status-pill {
    display: inline-block;
    color: #9AD8A7;
    background: #14251A;
    border: 1px solid #2D5639;
    border-radius: 30px;
    padding: 6px 12px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* HERO */

.hero-label {
    color: #8CCF9B;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(42px, 6vw, 72px);
    line-height: 1.12;
    letter-spacing: -3px;
    font-weight: 800;
    color: #F0F7F1;
    margin-top: 20px;
}

.hero-accent {
    color: #8CCF9B;
}

.hero-description {
    color: #9AABA0;
    font-size: 15px;
    line-height: 1.9;
    max-width: 720px;
}

/* SECTION LABEL */

.section-label {
    color: #9ACBA3;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

/* CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 16px;
    transition: border-color 0.2s ease, transform 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #568B65;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 9px;
}

/* CARD TEXT */

.card-index {
    color: #83C995;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.card-icon {
    font-size: 27px;
}

.card-description {
    color: #93A59A;
    font-size: 13px;
    line-height: 1.8;
}

.card-tag {
    color: #79B98A;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

/* LOWER PANELS */

.panel-description {
    color: #9AABA0;
    font-size: 13px;
    line-height: 1.9;
}

/* DIVIDERS */

hr {
    border-color: #25372D !important;
}

/* METRICS */

div[data-testid="stMetric"] {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 12px;
    padding: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #91A397;
}

div[data-testid="stMetricValue"] {
    color: #EAF5EC;
}

/* BUTTONS */

.stButton > button {
    background: #8CCF9B;
    color: #08100B;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #A7E0B1;
    color: #08100B;
}

/* HIDE DEFAULT ELEMENTS */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

div[data-testid="stDecoration"] {
    display: none;
}

/* FOOTER */

.footer-text {
    color: #71847A;
    font-size: 10px;
    letter-spacing: 1.2px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# TOP BRAND SECTION
# =========================================================

top_left, top_right = st.columns([3, 1])

with top_left:
    st.markdown(
        '<div class="brand"><span class="brand-dot">●</span> AEROSENSE AI</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="brand-sub">AIR QUALITY INTELLIGENCE PLATFORM</div>',
        unsafe_allow_html=True
    )

with top_right:
    st.markdown(
        '<div style="text-align:right; padding-top:10px;">'
        '<span class="status-pill">● SYSTEM ONLINE</span></div>',
        unsafe_allow_html=True
    )

st.write("")
st.caption("ENVIRONMENTAL INTELLIGENCE  /  BENGALURU")
st.divider()


# =========================================================
# HERO SECTION
# =========================================================

st.write("")

st.markdown(
    '<div class="hero-label">ENVIRONMENTAL DATA  ·  ANALYTICS  ·  INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero-title">
    See the air.<br>
    Understand <span class="hero-accent">the impact.</span>
</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown("""
<div class="hero-description">
    An intelligent environmental platform designed to explore
    air quality, monitor atmospheric conditions and uncover
    the relationship between weather and pollution.
    <br><br>
    From real-time insights to predictive analysis,
    understand the environment through data.
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")


# =========================================================
# FEATURE CARDS
# =========================================================

st.markdown(
    '<div class="section-label">01 / EXPLORE THE PLATFORM</div>',
    unsafe_allow_html=True
)

st.write("")

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    with st.container(border=True):
        st.markdown(
            '<div class="card-index">01 — MONITOR</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown('<div class="card-icon">◉</div>', unsafe_allow_html=True)
        st.subheader("Air Quality")
        st.markdown("""
        <div class="card-description">
        Explore AQI levels, pollutant concentrations and
        monitoring station data. Identify patterns in
        environmental pollution.
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown(
            '<div class="card-tag">AIR QUALITY ANALYSIS ↗</div>',
            unsafe_allow_html=True
        )

with c2:
    with st.container(border=True):
        st.markdown(
            '<div class="card-index">02 — ANALYSE</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown('<div class="card-icon">☁</div>', unsafe_allow_html=True)
        st.subheader("Weather Insights")
        st.markdown("""
        <div class="card-description">
        Study temperature, humidity, wind patterns and
        their relationship with changing air-quality
        conditions.
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown(
            '<div class="card-tag">WEATHER INTELLIGENCE ↗</div>',
            unsafe_allow_html=True
        )

with c3:
    with st.container(border=True):
        st.markdown(
            '<div class="card-index">03 — PREDICT</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown('<div class="card-icon">⌁</div>', unsafe_allow_html=True)
        st.subheader("AQI Predictions")
        st.markdown("""
        <div class="card-description">
        Examine historical air-quality trends and
        explore short-term forecasting through
        data-driven models.
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown(
            '<div class="card-tag">PREDICTIVE ANALYTICS ↗</div>',
            unsafe_allow_html=True
        )


# =========================================================
# PROJECT INFORMATION
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-label">02 / ABOUT THE PLATFORM</div>',
    unsafe_allow_html=True
)

st.write("")

left, right = st.columns([1.35, 1], gap="large")

with left:
    with st.container(border=True):
        st.markdown("### Environmental intelligence, in one place")

        st.markdown("""
        <div class="panel-description">
        AeroSense AI brings environmental monitoring,
        air-quality analysis and predictive insights together
        in a unified platform.

        <br><br>

        Explore pollutant behaviour, understand weather
        patterns, examine health implications and discover
        meaningful trends hidden within environmental data.
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("**ONE PLATFORM. MULTIPLE ENVIRONMENTAL INSIGHTS.**")

with right:
    with st.container(border=True):
        st.markdown("### Platform modules")

        modules = [
            ("01", "AQI Analysis", "Pollutant and AQI exploration"),
            ("02", "Weather Insights", "Atmospheric patterns"),
            ("03", "AQI Prediction", "Forecasting and trends"),
            ("04", "Health Advisory", "Health-related insights"),
            ("05", "Overview", "Environmental dashboard")
        ]

        for number, name, description in modules:
            a, b = st.columns([0.18, 1])

            with a:
                st.markdown(
                    f'<div class="card-index">{number}</div>',
                    unsafe_allow_html=True
                )

            with b:
                st.markdown(f"**{name}**")
                st.caption(description)

            st.divider()


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.divider()

f1, f2 = st.columns(2)

with f1:
    st.markdown(
        '<div class="footer-text">AEROSENSE AI · ENVIRONMENTAL INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        '<div class="footer-text" style="text-align:right;">'
        'DATA · ANALYTICS · PREDICTION</div>',
        unsafe_allow_html=True
    )
