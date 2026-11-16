
import streamlit as st
import pandas as pd
import numpy as np

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Health Advisory | AeroSense AI",
    page_icon="🌿",
    layout="wide"
)

# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #101411;
    color: #E8EEE9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
    color: #EDF4EF;
}

.hero {
    background: linear-gradient(120deg, #1B2921, #17221C);
    border: 1px solid #30463A;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 28px;
}

.hero-tag {
    color: #9CC9A8;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}

.hero-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 12px;
    color: #F1F7F2;
}

.hero-subtitle {
    color: #AABBB0;
    font-size: 15px;
    margin-top: 8px;
}

.section-heading {
    font-family: 'Manrope', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #EAF2EC;
    margin-top: 28px;
    margin-bottom: 5px;
}

.section-caption {
    color: #91A197;
    font-size: 13px;
    margin-bottom: 18px;
}

.panel {
    background: #18211B;
    border: 1px solid #2D3D32;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 12px;
}

.panel-label {
    color: #91B69B;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.metric-value {
    color: #EAF4EC;
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    font-weight: 800;
}

.metric-caption {
    color: #93A398;
    font-size: 12px;
    margin-top: 4px;
}

.muted {
    color: #A8B7AC;
    font-size: 14px;
    line-height: 1.7;
}

.info-note {
    background: #1C2A21;
    border-left: 3px solid #79A989;
    border-radius: 8px;
    padding: 14px 17px;
    color: #C3D4C8;
    font-size: 13px;
    margin: 12px 0;
}

div[data-testid="stMetric"] {
    background: #18211B;
    border: 1px solid #2D3D32;
    padding: 18px;
    border-radius: 13px;
}

div[data-testid="stMetricLabel"] {
    color: #9EAEA2;
}

div[data-testid="stMetricValue"] {
    color: #EAF4EC;
}

.stButton > button {
    background: #709B7B;
    color: #101711;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    padding: 10px 20px;
}

.stButton > button:hover {
    background: #8BB797;
    color: #101711;
}

.stSelectbox label,
.stSlider label,
.stNumberInput label,
.stTextArea label {
    color: #D6E2D9 !important;
}

hr {
    border-color: #2D3D32;
}

.footer {
    text-align: center;
    color: #74867A;
    font-size: 12px;
    padding-top: 25px;
    border-top: 1px solid #29372D;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)


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
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">AEROSENSE AI / HEALTH INTELLIGENCE</div>
    <div class="hero-title">Health Advisory</div>
    <div class="hero-subtitle">
        Understand how air quality affects health, identify pollutant
        patterns and explore practical exposure precautions.
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# FEATURE 1: AQI HEALTH ASSESSMENT
# ============================================================

st.markdown('<div class="section-heading">01 / AQI health assessment</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Explore the health implications of different AQI levels.</div>',
    unsafe_allow_html=True
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
    st.metric("HEALTH RISK LEVEL",
              "Low" if aqi_value <= 100 else
              "Moderate" if aqi_value <= 200 else
              "High")

st.markdown(f"""
<div class="panel">
    <div class="panel-label">CURRENT ASSESSMENT</div>
    <h2 style="color:{category_color};">{category}</h2>
    <p class="muted">{description}</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# FEATURE 2: PERSONAL HEALTH ADVISORY
# ============================================================

st.markdown('<div class="section-heading">02 / Personalised health advisory</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Explore precautions based on individual sensitivity.</div>',
    unsafe_allow_html=True
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

st.markdown('<div class="panel">', unsafe_allow_html=True)

st.markdown("**Recommended precautions**")

for item in advice:
    st.markdown(f"- {item}")

st.markdown("</div>", unsafe_allow_html=True)

st.caption(
    "These are general educational precautions, not a personal medical diagnosis. "
    "Seek professional advice for concerning symptoms."
)


# ============================================================
# FEATURE 3: EXPOSURE ESTIMATOR
# ============================================================

st.markdown('<div class="section-heading">03 / Exposure estimator</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Estimate time spent in different environments.</div>',
    unsafe_allow_html=True
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
    st.warning("Your combined exposure time exceeds 24 hours. Please adjust the values.")
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

    st.markdown("""
    <div class="info-note">
        This tool describes your entered time distribution. It does not
        calculate an individual's actual inhaled pollution dose.
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FEATURE 4: AQI TREND TRACKER
# ============================================================

st.markdown('<div class="section-heading">04 / AQI trend tracker</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Enter recent AQI readings to inspect changes over time.</div>',
    unsafe_allow_html=True
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

    if not trend_values or any(x < 0 or x > 500 for x in trend_values):
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
        color="#83B893"
    )

    if change > 0:
        st.warning("The latest reading is higher than the first reading.")
    elif change < 0:
        st.success("The latest reading is lower than the first reading.")
    else:
        st.info("The first and latest readings are equal.")

except ValueError:
    st.error("Enter valid AQI values between 0 and 500, separated by commas.")


# ============================================================
# FEATURE 5: POLLUTANT EXPLORER
# ============================================================

st.markdown('<div class="section-heading">05 / Pollutant explorer</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Understand the major pollutants commonly monitored in air-quality assessments.</div>',
    unsafe_allow_html=True
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

st.markdown(f"""
<div class="panel">
    <div class="panel-label">POLLUTANT PROFILE</div>
    <h2>{selected_pollutant}</h2>
    <div style="color:#91B69B;font-weight:600;">{pollutant_name}</div>
    <p class="muted">{pollutant_description}</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# FEATURE 6: POLLUTANT CONTRIBUTION ANALYSIS
# ============================================================

st.markdown('<div class="section-heading">06 / Pollutant contribution analysis</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Compare pollutant sub-index values and their relative shares.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-note">
    Enter the pollutant sub-index values for a location. The dashboard
    compares their relative shares among the values entered. These are
    not official CPCB AQI contribution percentages.
</div>
""", unsafe_allow_html=True)

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

    st.info("Enter at least one pollutant sub-index value to view the analysis.")

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
        st.metric(
            "Highest sub-index",
            highest_pollutant
        )

    with col2:
        st.metric(
            "Sub-index value",
            f"{highest_value:.1f}"
        )

    with col3:
        st.metric(
            "Relative share",
            f"{highest_share:.1f}%"
        )

    st.markdown("**Relative pollutant comparison**")

    chart_data = entered_df.set_index("Pollutant")[
        "Relative share (%)"
    ]

    st.bar_chart(
        chart_data,
        color="#83B893"
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

    st.markdown(f"""
    <div class="panel">
        <div class="panel-label">KEY OBSERVATION</div>
        <h3>{highest_pollutant} has the highest entered sub-index</h3>
        <p class="muted">
            Among the values entered, {highest_pollutant} has a sub-index
            of {highest_value:.1f} and represents {highest_share:.1f}%
            of their combined total.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FEATURE 7: DAILY PRECAUTION CHECKLIST
# ============================================================

st.markdown('<div class="section-heading">07 / Daily precaution checklist</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Track simple actions that can help reduce avoidable exposure.</div>',
    unsafe_allow_html=True
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

st.markdown('<div class="section-heading">08 / Population vulnerability</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-caption">Groups that may be more sensitive to changes in air quality.</div>',
    unsafe_allow_html=True
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
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    AEROSENSE AI · HEALTH INTELLIGENCE MODULE<br>
    Air quality insights for informed everyday decisions.
</div>
""", unsafe_allow_html=True)
