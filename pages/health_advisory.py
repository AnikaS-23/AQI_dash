
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Health Advisory | AeroSense AI",
    page_icon="◈",
    layout="wide"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #101411;
    color: #e9eee9;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stSidebar"] {
    background: #141a16;
    border-right: 1px solid #29332c;
}
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}
h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: #e9eee9 !important;
}
.eyebrow {
    color: #8da99a;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}
.page-title {
    font-family: 'Manrope', sans-serif;
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-top: 8px;
}
.subtitle {
    color: #929e94;
    font-size: 13px;
    margin-bottom: 25px;
}
.panel {
    background: #171e19;
    border: 1px solid #303b33;
    border-radius: 13px;
    padding: 22px;
    height: 100%;
}
.panel-label {
    color: #89978d;
    font-size: 10px;
    letter-spacing: 1.7px;
    font-weight: 700;
}
.aqi-number {
    font-family: 'Manrope', sans-serif;
    font-size: 62px;
    font-weight: 800;
    color: #e6eee7;
    letter-spacing: -3px;
}
.aqi-category {
    color: #a5bea9;
    font-size: 17px;
    font-weight: 600;
}
.muted {
    color: #929e94;
    font-size: 12px;
    line-height: 1.7;
}
.section-heading {
    font-family: 'Manrope', sans-serif;
    font-size: 21px;
    font-weight: 700;
    margin-top: 32px;
    margin-bottom: 5px;
}
.section-caption {
    color: #87948a;
    font-size: 12px;
    margin-bottom: 17px;
}
.feature-card {
    background: #171e19;
    border: 1px solid #303b33;
    border-radius: 12px;
    padding: 19px;
    min-height: 145px;
}
.feature-number {
    color: #7e9f8b;
    font-size: 11px;
    letter-spacing: 1.5px;
}
.feature-title {
    color: #e2eae3;
    font-size: 15px;
    font-weight: 600;
    margin: 12px 0 8px;
}
.feature-text {
    color: #929e94;
    font-size: 12px;
    line-height: 1.7;
}
.group-row {
    padding: 14px 0;
    border-bottom: 1px solid #303b33;
}
.group-title {
    color: #dce6dd;
    font-size: 14px;
    font-weight: 600;
}
.group-desc {
    color: #89978d;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 5px;
}
.note {
    background: #1b2821;
    border: 1px solid #35483b;
    border-left: 3px solid #82ad98;
    border-radius: 8px;
    padding: 15px 18px;
    color: #b7c8ba;
    font-size: 13px;
    line-height: 1.7;
}
div[data-testid="stSlider"] {
    padding-top: 10px;
}
.stButton button {
    background: #27372d;
    border: 1px solid #526b58;
    color: #e5eee6;
    border-radius: 8px;
}
hr {
    border-color: #303b33 !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------- AQI LOGIC --------------------

def get_aqi_details(value):
    if value <= 50:
        return "Good", "Air quality is satisfactory."
    elif value <= 100:
        return "Satisfactory", "Minor breathing discomfort may occur in sensitive people."
    elif value <= 200:
        return "Moderate", "Sensitive individuals may experience discomfort."
    elif value <= 300:
        return "Poor", "Prolonged exposure may cause breathing discomfort."
    elif value <= 400:
        return "Very Poor", "Respiratory effects may occur after prolonged exposure."
    return "Severe", "Health impacts may occur even during light activity."


# -------------------- HEADER --------------------

st.markdown(
    '<div class="eyebrow">AEROSENSE AI / ENVIRONMENTAL INTELLIGENCE</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="page-title">Health Advisory</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Exposure assessment · Personalised guidance · Public health insights</div>',
    unsafe_allow_html=True
)

st.divider()


# -------------------- AQI ASSESSMENT --------------------

st.markdown('<div class="section-heading">Air quality assessment</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">Explore health guidance using an AQI reading.</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1.5], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-label">SELECT AQI VALUE</div>',
                unsafe_allow_html=True)
    aqi = st.slider("Air Quality Index", 0, 500, 104)
    st.markdown(
        '<p class="muted">Adjust the value to explore different pollution scenarios.</p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

category, description = get_aqi_details(aqi)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-label">ASSESSMENT RESULT</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="aqi-number">{aqi}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="aqi-category">{category}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<p class="muted">{description}</p>',
                unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -------------------- FEATURE 1: PERSONAL PROFILE --------------------

st.markdown('<div class="section-heading">Personalised risk assessment</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">Explore how sensitivity to air pollution can differ between individuals.</div>',
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)

with p1:
    age_group = st.selectbox(
        "Age group",
        ["Adult", "Child", "Older adult"]
    )

with p2:
    respiratory = st.selectbox(
        "Respiratory condition",
        ["No known condition", "Asthma", "Other respiratory condition"]
    )

with p3:
    heart_condition = st.selectbox(
        "Heart condition",
        ["No known condition", "Yes"]
    )

sensitive = (
    age_group in ["Child", "Older adult"]
    or respiratory != "No known condition"
    or heart_condition == "Yes"
)

if sensitive and aqi > 100:
    profile_message = (
        "This profile may be more sensitive to elevated pollution. "
        "Consider reducing prolonged outdoor exertion and follow relevant medical advice."
    )
elif aqi > 200:
    profile_message = (
        "Pollution is elevated. Consider reducing outdoor exertion "
        "and monitoring official local advisories."
    )
else:
    profile_message = (
        "Continue monitoring air quality and follow your usual health guidance."
    )

st.markdown(f"""
<div class="note">
    <b>Profile guidance</b><br><br>
    {profile_message}
</div>
""", unsafe_allow_html=True)

st.caption(
    "This is general educational guidance, not a clinical risk score or medical assessment."
)


# -------------------- FEATURE 2: EXPOSURE CALCULATOR --------------------

st.markdown('<div class="section-heading">Outdoor exposure estimator</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">Explore how time outdoors and activity intensity change exposure.</div>',
    unsafe_allow_html=True
)

e1, e2 = st.columns(2)

with e1:
    hours = st.slider("Hours spent outdoors", 0, 12, 2)

with e2:
    activity = st.selectbox(
        "Activity intensity",
        ["Low - sitting or light walking",
         "Moderate - walking",
         "High - running or strenuous exercise"]
    )

activity_factor = {
    "Low - sitting or light walking": 1,
    "Moderate - walking": 1.5,
    "High - running or strenuous exercise": 2
}

exposure_index = round(hours * activity_factor[activity] * aqi / 100, 1)

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-label">ILLUSTRATIVE EXPOSURE INDEX</div>',
            unsafe_allow_html=True)
st.markdown(f'<div class="aqi-number">{exposure_index}</div>',
            unsafe_allow_html=True)
st.markdown(
    '<p class="muted">A simple comparison indicator based on selected AQI, time and activity. '
    'It is not a measured dose or validated medical risk score.</p>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)


# -------------------- FEATURE 3: AQI TREND TRACKER --------------------

st.markdown('<div class="section-heading">AQI trend tracker</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">Enter recent readings to understand whether air quality is changing.</div>',
    unsafe_allow_html=True
)

default_readings = "145, 132, 118, 125, 104"

trend_text = st.text_input(
    "Enter AQI readings, oldest to newest, separated by commas",
    value=default_readings
)

try:
    readings = [int(x.strip()) for x in trend_text.split(",") if x.strip()]

    if len(readings) < 2 or any(x < 0 or x > 500 for x in readings):
        raise ValueError

    trend_df = pd.DataFrame({
        "Reading": range(1, len(readings) + 1),
        "AQI": readings
    })

    st.line_chart(trend_df.set_index("Reading"), y="AQI")

    difference = readings[-1] - readings[0]

    if difference < 0:
        st.success(f"AQI decreased by {abs(difference)} points across these readings.")
    elif difference > 0:
        st.warning(f"AQI increased by {difference} points across these readings.")
    else:
        st.info("AQI remained unchanged across these readings.")

except ValueError:
    st.error("Enter at least two whole-number AQI readings between 0 and 500.")


# -------------------- FEATURE 4: POLLUTANT EXPLORER --------------------

st.markdown('<div class="section-heading">Pollutant explorer</div>',
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
    <div class="aqi-category">{pollutant_name}</div>
    <p class="muted">{pollutant_description}</p>
</div>
""", unsafe_allow_html=True)


# -------------------- FEATURE 5: ACTION CHECKLIST --------------------

st.markdown('<div class="section-heading">Daily precaution checklist</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">Track useful precautions for the day.</div>',
    unsafe_allow_html=True
)

tasks = [
    "Check the latest local AQI reading",
    "Review official air-quality advisories",
    "Consider reducing strenuous outdoor activity when AQI is elevated",
    "Keep indoor air cleaner where possible",
    "Follow prescribed medical guidance if applicable"
]

completed = 0

for task in tasks:
    if st.checkbox(task, key=f"task_{task}"):
        completed += 1

st.progress(completed / len(tasks))
st.caption(f"{completed} of {len(tasks)} precautions checked")


# -------------------- SENSITIVE GROUPS --------------------

st.markdown('<div class="section-heading">Population vulnerability</div>',
            unsafe_allow_html=True)

groups = [
    ("Children", "Developing lungs can make children more sensitive to air pollution."),
    ("Older adults", "Some older adults may be more vulnerable to pollution-related effects."),
    ("Respiratory conditions", "People with asthma and other respiratory conditions may experience worsening symptoms."),
    ("Cardiovascular conditions", "People with heart conditions may be more vulnerable to pollution-related effects.")
]

for title, desc in groups:
    st.markdown(f"""
    <div class="group-row">
        <div class="group-title">{title}</div>
        <div class="group-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- FOOTER --------------------

st.divider()
st.caption(
    "AEROSENSE AI · HEALTH INTELLIGENCE · "
    "Educational guidance only. AQI categories follow the Indian CPCB scale. "
    "Not a medical diagnosis."
)
