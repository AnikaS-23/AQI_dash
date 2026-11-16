
import streamlit as st
import pandas as pd
import numpy as np

# ============================================================
# AEROSENSE AI — HEALTH ADVISORY
# ============================================================

st.set_page_config(
    page_title="Health Advisory | AeroSense AI",
    page_icon="🌿",
    layout="wide"
)

# ============================================================
# GLOBAL HOMEPAGE THEME — EXACT PALETTE
# ============================================================

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
    --text: #C0CEC3;
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

h1, h2, h3 {
    font-weight: 800;
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
    margin-top: 30px;
    margin-bottom: 16px;
}

/* CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 16px;
    transition: border-color 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #568B65;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 9px;
}

/* CUSTOM PANELS */

.panel {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 14px;
    transition: border-color 0.2s ease;
}

.panel:hover {
    border-color: #568B65;
}

.panel-label {
    color: #8CCF9B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.7px;
    margin-bottom: 12px;
}

.panel-title {
    color: #EDF5EF;
    font-family: 'Manrope', sans-serif;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 8px;
}

.panel-description {
    color: #91A397;
    font-size: 13px;
    line-height: 1.8;
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
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
}

/* INPUTS */

.stSelectbox label,
.stSlider label,
.stNumberInput label,
.stTextArea label,
.stTextInput label {
    color: #EDF5EF !important;
    font-weight: 600;
}

.stSelectbox div[data-baseweb="select"] > div,
.stTextInput input,
.stNumberInput input {
    background: #151F1A !important;
    color: #EDF5EF !important;
    border-color: #25372D !important;
    border-radius: 9px;
}

.stCheckbox label {
    color: #C0CEC3 !important;
}

div[data-baseweb="popover"] {
    background: #111815;
}

/* BUTTONS */

.stButton > button,
.stDownloadButton > button {
    background: #8CCF9B;
    color: #08100B;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #A7E0B1;
    color: #08100B;
}

/* EXPANDERS */

div[data-testid="stExpander"] {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 12px;
}

div[data-testid="stExpander"] summary {
    color: #EDF5EF;
}

/* DATAFRAME */

div[data-testid="stDataFrame"] {
    border: 1px solid #25372D;
    border-radius: 12px;
    overflow: hidden;
}

/* ALERTS */

div[data-testid="stAlert"] {
    background: #151F1A;
    border: 1px solid #25372D;
    border-radius: 12px;
}

/* PROGRESS */

.stProgress > div > div > div {
    background: #8CCF9B;
}

/* SLIDER */

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #8CCF9B;
}

/* CHARTS */

div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"] {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 12px;
    padding: 10px;
}

/* DIVIDERS */

hr {
    border-color: #25372D !important;
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


# ============================================================
# REUSABLE PAGE ELEMENTS
# ============================================================

def section_heading(number, title, caption=None):
    caption_html = (
        f'<div style="color:#91A397;font-size:13px;'
        f'margin-top:-8px;margin-bottom:18px;">{caption}</div>'
        if caption else ""
    )

    st.markdown(
        f"""
        <div class="section-label">
            {number} / {title.upper()}
        </div>
        {caption_html}
        """,
        unsafe_allow_html=True
    )


def info_panel(label, title=None, description=None, color=None):
    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-label">{label}</div>
            <div class="panel-title" style="color:{color or '#EDF5EF'};">
                {title or ''}
            </div>
            <div class="panel-description">
                {description or ''}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AQI CATEGORY LOGIC
# ============================================================

def get_aqi_details(value):

    if value <= 50:
        return "Good", "Air quality is satisfactory.", "#65B985"

    elif value <= 100:
        return "Satisfactory", "Minor breathing discomfort may occur in sensitive individuals.", "#A8C76D"

    elif value <= 200:
        return "Moderate", "Breathing discomfort may occur in people with lung, asthma or heart conditions.", "#D9B65D"

    elif value <= 300:
        return "Poor", "Prolonged exposure may cause breathing discomfort.", "#D98B56"

    elif value <= 400:
        return "Very Poor", "Respiratory effects may occur with prolonged exposure.", "#D66D62"

    else:
        return "Severe", "Health effects may be experienced by everyone, with greater risk for sensitive groups.", "#B94F59"


def get_health_advice(category):

    advice = {
        "Good": [
            "Enjoy normal outdoor activities.",
            "Continue regular daily routines.",
            "Maintain good indoor ventilation."
        ],
        "Satisfactory": [
            "Most people can continue normal activities.",
            "Sensitive individuals should monitor symptoms.",
            "Take breaks if outdoor conditions feel uncomfortable."
        ],
        "Moderate": [
            "Sensitive individuals should reduce prolonged outdoor exertion.",
            "Keep track of local air-quality updates.",
            "Consider indoor activities if you experience discomfort."
        ],
        "Poor": [
            "Reduce prolonged outdoor exertion.",
            "Consider a well-fitted mask when exposure cannot be avoided.",
            "Keep windows closed during periods of high pollution."
        ],
        "Very Poor": [
            "Avoid strenuous outdoor activities where possible.",
            "Keep indoor spaces as clean as possible.",
            "Sensitive individuals should follow medical advice."
        ],
        "Severe": [
            "Avoid outdoor physical exertion where possible.",
            "Stay in a cleaner indoor environment.",
            "Follow official local health and air-quality advisories."
        ]
    }

    return advice.get(category, [])


# ============================================================
# HEADER — HOMEPAGE STYLE
# ============================================================

header_col, status_col = st.columns([3, 1])

with header_col:
    st.markdown(
        """
        <div class="brand">
            <span class="brand-dot">●</span> AEROSENSE AI
        </div>
        <div class="brand-sub">
            AIR QUALITY INTELLIGENCE PLATFORM
        </div>
        """,
        unsafe_allow_html=True
    )

with status_col:
    st.markdown(
        """
        <div style="text-align:right;padding-top:10px;">
            <span class="status-pill">● HEALTH INTELLIGENCE</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.caption("ENVIRONMENTAL INTELLIGENCE  /  HEALTH & EXPOSURE")
st.divider()


# ============================================================
# HERO SECTION — HOMEPAGE STYLE
# ============================================================

st.write("")

st.markdown(
    """
    <div class="hero-label">
        HEALTH · POLLUTANTS · EXPOSURE INSIGHTS
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Understand the air.<br>
        <span class="hero-accent">Protect your health.</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div class="hero-description">
        <p>
            Explore how air quality affects health, identify pollutant
            patterns and discover practical exposure precautions through
            an integrated health intelligence dashboard.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")


# ============================================================
# FEATURE 1: AQI HEALTH ASSESSMENT
# ============================================================

section_heading(
    "01",
    "AQI health assessment",
    "Explore the health implications of different AQI levels."
)

aqi_value = st.slider(
    "Select AQI value",
    min_value=0,
    max_value=500,
    value=120,
    step=1
)

category, description, category_color = get_aqi_details(aqi_value)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AQI VALUE", aqi_value)

with col2:
    st.metric("AIR QUALITY CATEGORY", category)

with col3:
    st.metric(
        "HEALTH RISK LEVEL",
        "Low" if aqi_value <= 100 else
        "Moderate" if aqi_value <= 200 else
        "High"
    )

info_panel(
    "CURRENT ASSESSMENT",
    category,
    description,
    category_color
)


# ============================================================
# FEATURE 2: PERSONAL HEALTH ADVISORY
# ============================================================

section_heading(
    "02",
    "Personalised health advisory",
    "Explore precautions based on individual sensitivity."
)

sensitivity = st.selectbox(
    "Select your sensitivity group",
    [
        "General population",
        "People with asthma",
        "People with respiratory conditions",
        "Children",
        "Older adults",
        "People with heart conditions"
    ]
)

advice = get_health_advice(category)

if sensitivity != "General population":
    advice = advice + [
        "Pay attention to any unusual symptoms.",
        "Consider limiting outdoor exposure when pollution levels are high."
    ]

st.markdown("**Recommended precautions**")

with st.container(border=True):
    for item in advice:
        st.markdown(f"- {item}")

st.caption(
    "These are general educational precautions, not a personal medical diagnosis. "
    "Seek professional advice for concerning symptoms."
)


# ============================================================
# FEATURE 3: EXPOSURE ESTIMATOR
# ============================================================

section_heading(
    "03",
    "Exposure estimator",
    "Estimate time spent in different environments."
)

col1, col2 = st.columns(2)

with col1:
    outdoor_hours = st.number_input(
        "Outdoor exposure (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=2.0,
        step=0.5
    )

with col2:
    indoor_hours = st.number_input(
        "Indoor exposure (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=8.0,
        step=0.5
    )

total_hours = outdoor_hours + indoor_hours

if total_hours > 24:
    st.warning(
        "Your combined exposure time exceeds 24 hours. Please adjust the values."
    )
else:
    outdoor_share = (
        outdoor_hours / total_hours * 100
        if total_hours > 0 else 0
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Outdoor exposure", f"{outdoor_hours:.1f} hours")

    with col2:
        st.metric("Outdoor share of entered time", f"{outdoor_share:.1f}%")

    st.progress(int(outdoor_share))

    st.info(
        "This tool describes your entered time distribution. It does not "
        "calculate an individual's actual inhaled pollution dose."
    )


# ============================================================
# FEATURE 4: AQI TREND TRACKER
# ============================================================

section_heading(
    "04",
    "AQI trend tracker",
    "Enter recent AQI readings to inspect changes over time."
)

trend_input = st.text_input(
    "Enter AQI readings separated by commas",
    value="85, 92, 110, 105, 130, 118, 120",
    help="Example: 85, 92, 110, 105, 130"
)

try:
    trend_values = [
        float(x.strip())
        for x in trend_input.split(",")
        if x.strip()
    ]

    if not trend_values or any(
        x < 0 or x > 500 for x in trend_values
    ):
        raise ValueError

    trend_df = pd.DataFrame({
        "Reading": range(1, len(trend_values) + 1),
        "AQI": trend_values
    })

    average_aqi = np.mean(trend_values)
    change = trend_values[-1] - trend_values[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average AQI", f"{average_aqi:.1f}")

    with col2:
        st.metric("Latest AQI", f"{trend_values[-1]:.1f}")

    with col3:
        st.metric(
            "Change from first reading",
            f"{change:+.1f}"
        )

    st.line_chart(
        trend_df.set_index("Reading")["AQI"],
        color="#8CCF9B"
    )

    if change > 0:
        st.warning("The latest reading is higher than the first reading.")
    elif change < 0:
        st.success("The latest reading is lower than the first reading.")
    else:
        st.info("The first and latest readings are equal.")

except ValueError:
    st.error(
        "Enter valid AQI values between 0 and 500, separated by commas."
    )


# ============================================================
# FEATURE 5: POLLUTANT EXPLORER
# ============================================================

section_heading(
    "05",
    "Pollutant explorer",
    "Understand the major pollutants commonly monitored in air-quality assessments."
)

pollutants = {
    "PM2.5": (
        "Fine particulate matter",
        "Very small airborne particles that can penetrate deep into the lungs."
    ),
    "PM10": (
        "Coarse particulate matter",
        "Inhalable particles from sources such as dust, construction and roads."
    ),
    "NO₂": (
        "Nitrogen dioxide",
        "A gas commonly associated with traffic and fuel combustion."
    ),
    "SO₂": (
        "Sulphur dioxide",
        "A gas often associated with burning sulphur-containing fuels."
    ),
    "CO": (
        "Carbon monoxide",
        "A colourless gas produced by incomplete combustion."
    ),
    "O₃": (
        "Ground-level ozone",
        "A pollutant formed through reactions involving sunlight and other pollutants."
    )
}

selected_pollutant = st.selectbox(
    "Choose a pollutant",
    list(pollutants.keys())
)

pollutant_name, pollutant_description = pollutants[selected_pollutant]

info_panel(
    "POLLUTANT PROFILE",
    selected_pollutant,
    f"{pollutant_name} — {pollutant_description}"
)


# ============================================================
# FEATURE 6: POLLUTANT CONTRIBUTION ANALYSIS
# ============================================================

section_heading(
    "06",
    "Pollutant contribution analysis",
    "Compare pollutant sub-index values and their relative shares."
)

st.info(
    "Enter the pollutant sub-index values for a location. The dashboard "
    "compares their relative shares among the values entered. These are "
    "not official CPCB AQI contribution percentages."
)

col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input(
        "PM2.5 sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

    pm10 = st.number_input(
        "PM10 sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

with col2:
    no2 = st.number_input(
        "NO₂ sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

    so2 = st.number_input(
        "SO₂ sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

with col3:
    co = st.number_input(
        "CO sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

    ozone = st.number_input(
        "O₃ sub-index",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=1.0
    )

contribution_data = {
    "PM2.5": pm25,
    "PM10": pm10,
    "NO₂": no2,
    "SO₂": so2,
    "CO": co,
    "O₃": ozone
}

contribution_df = pd.DataFrame({
    "Pollutant": list(contribution_data.keys()),
    "Sub-index": list(contribution_data.values())
})

entered_df = contribution_df[
    contribution_df["Sub-index"] > 0
].copy()

if len(entered_df) == 0:

    st.info(
        "Enter at least one pollutant sub-index value to view the analysis."
    )

else:

    total_subindex = entered_df["Sub-index"].sum()

    entered_df["Relative share (%)"] = (
        entered_df["Sub-index"] / total_subindex
    ) * 100

    entered_df = entered_df.sort_values(
        "Relative share (%)",
        ascending=False
    )

    highest_pollutant = entered_df.iloc[0]["Pollutant"]
    highest_value = entered_df.iloc[0]["Sub-index"]
    highest_share = entered_df.iloc[0]["Relative share (%)"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Highest sub-index", highest_pollutant)

    with col2:
        st.metric("Sub-index value", f"{highest_value:.1f}")

    with col3:
        st.metric("Relative share", f"{highest_share:.1f}%")

    st.markdown("**Relative pollutant comparison**")

    chart_data = entered_df.set_index("Pollutant")[
        "Relative share (%)"
    ]

    st.bar_chart(
        chart_data,
        color="#8CCF9B"
    )

    st.markdown("**Contribution breakdown**")

    display_df = entered_df.copy()

    display_df["Relative share (%)"] = (
        display_df["Relative share (%)"].round(2)
    )

    display_df["Sub-index"] = (
        display_df["Sub-index"].round(2)
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    info_panel(
        "KEY OBSERVATION",
        f"{highest_pollutant} has the highest entered sub-index",
        f"Among the values entered, {highest_pollutant} has a sub-index "
        f"of {highest_value:.1f} and represents {highest_share:.1f}% "
        "of their combined total."
    )


# ============================================================
# FEATURE 7: DAILY PRECAUTION CHECKLIST
# ============================================================

section_heading(
    "07",
    "Daily precaution checklist",
    "Track simple actions that can help reduce avoidable exposure."
)

checklist_items = [
    "Checked the latest local AQI update",
    "Avoided unnecessary outdoor exertion during high pollution",
    "Kept indoor spaces clean",
    "Checked ventilation and indoor air conditions",
    "Followed relevant health precautions"
]

completed = 0

for item in checklist_items:
    if st.checkbox(item, key=f"check_{item}"):
        completed += 1

progress = completed / len(checklist_items)

st.progress(progress)

st.caption(
    f"{completed} of {len(checklist_items)} precautions completed"
)


# ============================================================
# FEATURE 8: POPULATION VULNERABILITY
# ============================================================

section_heading(
    "08",
    "Population vulnerability",
    "Groups that may be more sensitive to changes in air quality."
)

vulnerability = {
    "Children": "Developing lungs and higher breathing rates can increase sensitivity to air pollution.",
    "Older adults": "Age-related health factors may increase sensitivity to polluted air.",
    "People with asthma": "Air pollution can trigger or worsen respiratory symptoms.",
    "People with heart conditions": "Some pollutants can place additional stress on the cardiovascular system.",
    "Outdoor workers": "Longer periods outdoors may increase exposure to ambient pollutants."
}

for group, explanation in vulnerability.items():
    with st.expander(group):
        st.write(explanation)


# ============================================================
# FOOTER — HOMEPAGE STYLE
# ============================================================

st.write("")
st.divider()

f1, f2 = st.columns(2)

with f1:
    st.markdown(
        '<div class="footer-text">'
        'AEROSENSE AI · ENVIRONMENTAL INTELLIGENCE'
        '</div>',
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        '<div class="footer-text" style="text-align:right;">'
        'HEALTH · EXPOSURE · ADVISORY'
        '</div>',
        unsafe_allow_html=True
    )
