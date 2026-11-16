import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta
from pages.ml_prediction_ui import render_ml_prediction

# ============================================================
# AEROSENSE AI — AQI PREDICTION
# ============================================================

st.set_page_config(
    page_title="AQI Prediction | AeroSense AI",
    page_icon="🌿",
    layout="wide"
)

# ============================================================
# GLOBAL HOMEPAGE THEME
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

/* CUSTOM METRIC CARDS */

.metric-card {
    background: #111815;
    border: 1px solid #25372D;
    border-radius: 14px;
    padding: 20px;
    min-height: 120px;
    transition: border-color 0.2s ease;
}

.metric-card:hover {
    border-color: #568B65;
}

.metric-label {
    color: #91A397;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.metric-value {
    color: #EDF5EF;
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    font-weight: 800;
    margin-top: 12px;
}

.metric-note {
    color: #91A397;
    font-size: 11px;
    margin-top: 5px;
}

/* PANELS */

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

.panel-heading {
    color: #EDF5EF;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    font-size: 16px;
    margin-bottom: 5px;
}

.panel-caption {
    color: #91A397;
    font-size: 12px;
    margin-bottom: 13px;
}

/* STATUS PILLS */

.status-pill.good {
    background: #14251A;
    color: #9AD8A7;
    border: 1px solid #2D5639;
}

.status-pill.satisfactory {
    background: #252D1B;
    color: #C3D98C;
    border: 1px solid #515B35;
}

.status-pill.moderate {
    background: #302719;
    color: #EBC47A;
    border: 1px solid #66502C;
}

.status-pill.poor {
    background: #35221A;
    color: #E6A078;
    border: 1px solid #70432F;
}

.status-pill.very-poor {
    background: #351C23;
    color: #E58C91;
    border: 1px solid #71313C;
}

.status-pill.severe {
    background: #351B1B;
    color: #F08D82;
    border: 1px solid #713131;
}

/* NOTICES */

.notice {
    background: #151F1A;
    border: 1px solid #25372D;
    border-left: 3px solid #8CCF9B;
    padding: 15px 17px;
    border-radius: 9px;
    color: #C0CEC3;
    font-size: 13px;
    line-height: 1.8;
    margin: 12px 0;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input {
    background: #151F1A !important;
    color: #EDF5EF !important;
    border-color: #25372D !important;
    border-radius: 9px;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #151F1A !important;
    color: #EDF5EF !important;
    border-color: #25372D !important;
}

.stFileUploader section {
    background: #111815;
    border: 1px dashed #365541;
    border-radius: 12px;
}

.stFileUploader label {
    color: #C0CEC3 !important;
}

.stCheckbox label {
    color: #C0CEC3 !important;
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

/* CHARTS */

.stProgress > div > div > div {
    background: #8CCF9B;
}

/* ALERTS */

div[data-testid="stAlert"] {
    background: #151F1A;
    border: 1px solid #25372D;
    border-radius: 12px;
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

def section_heading(number, title):
    st.markdown(
        f'<div class="section-label">{number} / {title.upper()}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# AQI CATEGORY FUNCTIONS — INDIA CPCB SCALE
# ============================================================

def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "good"
    elif aqi <= 100:
        return "Satisfactory", "satisfactory"
    elif aqi <= 200:
        return "Moderate", "moderate"
    elif aqi <= 300:
        return "Poor", "poor"
    elif aqi <= 400:
        return "Very Poor", "very-poor"
    else:
        return "Severe", "severe"


def get_advisory(aqi):
    if aqi <= 50:
        return (
            "Air quality is in the Good range. "
            "Conditions are generally favourable for outdoor activities."
        )
    elif aqi <= 100:
        return (
            "Air quality is Satisfactory. Sensitive individuals "
            "may experience minor discomfort."
        )
    elif aqi <= 200:
        return (
            "Air quality is Moderate. People with asthma or other "
            "respiratory conditions should consider limiting prolonged "
            "outdoor exertion if they experience symptoms."
        )
    elif aqi <= 300:
        return (
            "Air quality is Poor. Reduce prolonged outdoor exertion, "
            "especially for sensitive groups."
        )
    elif aqi <= 400:
        return (
            "Air quality is Very Poor. Avoid prolonged outdoor exertion "
            "and follow local health advisories."
        )
    else:
        return (
            "Air quality is Severe. Follow official local health guidance "
            "and minimise outdoor exposure."
        )


# ============================================================
# DATA PREPARATION
# ============================================================

def prepare_data(df, time_column, aqi_column):

    data = df.copy()

    data[aqi_column] = pd.to_numeric(
        data[aqi_column], errors="coerce"
    )

    data = data.dropna(subset=[aqi_column])

    data = data[
        (data[aqi_column] >= 0) &
        (data[aqi_column] <= 500)
    ]

    if time_column != "No timestamp column":
        data[time_column] = pd.to_datetime(
            data[time_column], errors="coerce"
        )
        data = data.dropna(subset=[time_column])
        data = data.sort_values(time_column)
        data = data.rename(
            columns={time_column: "Timestamp"}
        )
    else:
        data = data.reset_index(drop=True)
        data["Timestamp"] = pd.date_range(
            end=pd.Timestamp.now(),
            periods=len(data),
            freq="h"
        )

    data = data[["Timestamp", aqi_column]].copy()
    data = data.rename(columns={aqi_column: "AQI"})

    data = data.drop_duplicates(
        subset=["Timestamp"], keep="last"
    )

    data = data.sort_values("Timestamp").reset_index(drop=True)

    return data


# ============================================================
# BASELINE FORECAST
# ============================================================

def generate_forecast(data, forecast_hours=24):

    values = data["AQI"].astype(float).values

    if len(values) < 3:
        raise ValueError(
            "At least 3 valid historical AQI readings are required."
        )

    recent = values[-48:]

    x = np.arange(len(recent))

    slope, intercept = np.polyfit(x, recent, 1)

    fitted = slope * x + intercept
    residuals = recent - fitted

    residual_std = float(np.std(residuals))

    damped_slope = np.clip(slope, -2.5, 2.5) * 0.35

    last_value = float(recent[-1])

    future_steps = np.arange(1, forecast_hours + 1)

    predicted = last_value + damped_slope * future_steps
    predicted = np.clip(predicted, 0, 500)

    uncertainty = residual_std * np.sqrt(future_steps / 3)

    lower = np.clip(predicted - uncertainty, 0, 500)
    upper = np.clip(predicted + uncertainty, 0, 500)

    last_timestamp = pd.to_datetime(
        data["Timestamp"].iloc[-1]
    )

    future_times = [
        last_timestamp + timedelta(hours=int(i))
        for i in future_steps
    ]

    forecast = pd.DataFrame({
        "Timestamp": future_times,
        "Predicted AQI": predicted,
        "Lower estimate": lower,
        "Upper estimate": upper
    })

    return forecast


# ============================================================
# TOP BRAND SECTION
# ============================================================

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
st.caption("ENVIRONMENTAL INTELLIGENCE  /  PREDICTIVE ANALYTICS")
st.divider()


# ============================================================
# HERO SECTION — CORRECTED
# ============================================================

st.write("")

st.markdown(
    '<div class="hero-label">ENVIRONMENTAL DATA · ANALYTICS · INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero-title">
    Predict the air.<br>
    Understand <span class="hero-accent">what comes next.</span>
</div>
""", unsafe_allow_html=True)

st.write("")

# IMPORTANT: No HTML <br> tags in the description.
# Separate paragraphs are created using normal HTML paragraph tags.

st.write("")
st.write("")


# ============================================================
# DATA INPUT
# ============================================================

section_heading("01", "Historical data source")

left, right = st.columns([1.5, 1])

with left:
    uploaded_file = st.file_uploader(
        "Upload historical AQI data (CSV)",
        type=["csv"],
        help="Upload a CSV containing historical AQI readings."
    )


# ============================================================
# LOAD DATA
# ============================================================

raw_data = None
demo_mode = False

if uploaded_file is not None:

    try:
        raw_data = pd.read_csv(uploaded_file)

        if raw_data.empty:
            st.error("The uploaded CSV is empty.")
            st.stop()

    except Exception as e:
        st.error(f"Could not read the uploaded CSV: {e}")
        st.stop()

else:

    demo_mode = True

    demo_values = [
        142, 139, 135, 132, 128, 124,
        121, 119, 116, 113, 110, 108,
        112, 117, 121, 118, 114, 109,
        105, 102, 104, 107, 103, 100,
        98, 101, 105, 109, 112, 108,
        104, 102, 99, 97, 100, 103,
        106, 104, 101, 98, 96, 94,
        97, 100, 102, 99, 95, 93
    ]

    demo_times = pd.date_range(
        end=pd.Timestamp.now().floor("h"),
        periods=len(demo_values),
        freq="h"
    )

    raw_data = pd.DataFrame({
        "timestamp": demo_times,
        "aqi": demo_values
    })


# ============================================================
# COLUMN DETECTION
# ============================================================

columns = list(raw_data.columns)

if not columns:
    st.error("No columns were found in the dataset.")
    st.stop()

lower_columns = {
    str(c).lower().strip(): c for c in columns
}

time_candidates = [
    "timestamp", "datetime", "date_time",
    "date", "time", "created_at"
]

aqi_candidates = [
    "aqi", "air_quality_index",
    "predicted_aqi", "overall_aqi",
    "air quality index"
]

detected_time = next(
    (lower_columns[c] for c in time_candidates
     if c in lower_columns),
    None
)

detected_aqi = next(
    (lower_columns[c] for c in aqi_candidates
     if c in lower_columns),
    None
)

numeric_candidates = []

for col in columns:
    converted = pd.to_numeric(
        raw_data[col], errors="coerce"
    )
    if converted.notna().sum() >= 3:
        numeric_candidates.append(col)

if detected_aqi is None and numeric_candidates:
    detected_aqi = numeric_candidates[0]

if detected_aqi is None:
    st.error(
        "Could not detect an AQI column. "
        "Please upload a CSV with a numeric AQI column."
    )
    st.stop()


# ============================================================
# COLUMN SELECTION
# ============================================================

if uploaded_file is not None:

    with st.expander("Configure dataset columns", expanded=True):

        col_a, col_b = st.columns(2)

        with col_a:
            time_options = ["No timestamp column"] + columns

            default_time_index = (
                time_options.index(detected_time)
                if detected_time in columns else 0
            )

            time_column = st.selectbox(
                "Timestamp column",
                time_options,
                index=default_time_index
            )

        with col_b:
            default_aqi_index = (
                columns.index(detected_aqi)
                if detected_aqi in columns else 0
            )

            aqi_column = st.selectbox(
                "AQI column",
                columns,
                index=default_aqi_index
            )

else:
    time_column = "timestamp"
    aqi_column = "aqi"


# ============================================================
# PREPARE FINAL DATA
# ============================================================

try:

    historical_data = prepare_data(
        raw_data,
        time_column,
        aqi_column
    )

    if len(historical_data) < 3:
        st.error(
            "Not enough valid AQI observations. "
            "Please provide at least 3 readings."
        )
        st.stop()

except Exception as e:

    st.error(f"Data preparation failed: {e}")
    st.stop()


# ============================================================
# DATA STATUS
# ============================================================

if demo_mode:

    st.info(
        "DEMO MODE: The dashboard is using illustrative sample readings. "
        "These values are not live Bengaluru measurements. "
        "Upload your team's dataset to analyse actual observations."
    )

else:

    st.success(
        f"Dataset loaded successfully: "
        f"{len(historical_data)} valid observations."
    )


# ============================================================
# GENERATE FORECAST
# ============================================================

try:

    forecast_data = generate_forecast(
        historical_data,
        forecast_hours=24
    )

except Exception as e:

    st.error(f"Forecast could not be generated: {e}")
    st.stop()


# ============================================================
# CALCULATE SUMMARY
# ============================================================

current_aqi = float(historical_data["AQI"].iloc[-1])
average_aqi = float(historical_data["AQI"].mean())

predicted_average = float(
    forecast_data["Predicted AQI"].mean()
)

predicted_max = float(
    forecast_data["Predicted AQI"].max()
)

predicted_min = float(
    forecast_data["Predicted AQI"].min()
)

change = predicted_average - current_aqi

change_percent = (
    (change / current_aqi) * 100
    if current_aqi != 0 else 0
)

current_category, current_class = get_aqi_category(current_aqi)

forecast_category, forecast_class = get_aqi_category(
    predicted_average
)


# ============================================================
# RANDOM FOREST ML PREDICTION — NEW ADDITION
# ============================================================

render_ml_prediction(
    current_aqi=current_aqi,
    timestamp=pd.to_datetime(
        historical_data["Timestamp"].iloc[-1]
    ),
    get_aqi_category=get_aqi_category,
    get_advisory=get_advisory
)


# ============================================================
# SUMMARY CARDS
# ============================================================

section_heading("02", "Forecast overview")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Latest AQI</div>
        <div class="metric-value">{current_aqi:.0f}</div>
        <div class="metric-note">Last available reading</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">24H average forecast</div>
        <div class="metric-value">{predicted_average:.0f}</div>
        <div class="metric-note">Baseline estimate</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Forecast maximum</div>
        <div class="metric-value">{predicted_max:.0f}</div>
        <div class="metric-note">Highest estimated AQI</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Forecast minimum</div>
        <div class="metric-value">{predicted_min:.0f}</div>
        <div class="metric-note">Lowest estimated AQI</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FORECAST STATUS
# ============================================================

section_heading("03", "Expected air quality")

status_col, advisory_col = st.columns([1, 2])

with status_col:

    st.markdown(f"""
    <div class="panel">
        <div class="panel-caption">EXPECTED 24-HOUR CATEGORY</div>
        <div style="font-size:31px; font-weight:800;
                    font-family:Manrope; color:#EDF5EF;">
            {forecast_category}
        </div>
        <br>
        <span class="status-pill {forecast_class}">
            AQI {predicted_average:.0f}
        </span>
    </div>
    """, unsafe_allow_html=True)

with advisory_col:

    st.markdown(f"""
    <div class="panel">
        <div class="panel-heading">Environmental advisory</div>
        <div class="panel-caption">
            Based on the estimated average AQI category
        </div>
        <p style="font-size:14px; line-height:1.8; color:#C0CEC3;">
            {get_advisory(predicted_average)}
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FORECAST CHART
# ============================================================

section_heading("04", "24-hour AQI forecast")

st.markdown("""
<div class="panel">
    <div class="panel-heading">Predicted AQI trajectory</div>
    <div class="panel-caption">
        Historical readings and the next 24 hours of baseline estimates
    </div>
</div>
""", unsafe_allow_html=True)

history_chart = historical_data.tail(24).copy()
history_chart = history_chart.set_index("Timestamp")

forecast_chart = forecast_data.set_index("Timestamp")

chart_data = pd.DataFrame({
    "Historical AQI": history_chart["AQI"],
    "Predicted AQI": forecast_chart["Predicted AQI"],
    "Upper estimate": forecast_chart["Upper estimate"],
    "Lower estimate": forecast_chart["Lower estimate"]
})

st.line_chart(
    chart_data,
    height=380,
    use_container_width=True
)

st.caption(
    "The upper and lower estimates represent an illustrative uncertainty "
    "range derived from recent forecast residuals. They are not guaranteed "
    "prediction limits."
)


# ============================================================
# FORECAST INTERPRETATION
# ============================================================

section_heading("05", "Forecast interpretation")

interpret_col1, interpret_col2 = st.columns(2)

with interpret_col1:

    if change > 5:
        trend_text = "Potential deterioration"
        trend_description = (
            "The forecast average is higher than the latest reading."
        )
    elif change < -5:
        trend_text = "Potential improvement"
        trend_description = (
            "The forecast average is lower than the latest reading."
        )
    else:
        trend_text = "Relatively stable"
        trend_description = (
            "The forecast average is close to the latest reading."
        )

    st.markdown(f"""
    <div class="panel">
        <div class="panel-heading">Expected trend</div>
        <div style="font-size:23px; font-weight:800;
                    color:#8CCF9B; margin-top:12px;">
            {trend_text}
        </div>
        <p style="color:#91A397; font-size:13px;
                  line-height:1.7; margin-top:8px;">
            {trend_description}
        </p>
        <div class="metric-note">
            Estimated average change: {change:+.1f} AQI points
            ({change_percent:+.1f}%)
        </div>
    </div>
    """, unsafe_allow_html=True)


with interpret_col2:

    best_row = forecast_data.loc[
        forecast_data["Predicted AQI"].idxmin()
    ]

    worst_row = forecast_data.loc[
        forecast_data["Predicted AQI"].idxmax()
    ]

    best_time = pd.to_datetime(
        best_row["Timestamp"]
    ).strftime("%d %b, %I:%M %p")

    worst_time = pd.to_datetime(
        worst_row["Timestamp"]
    ).strftime("%d %b, %I:%M %p")

    st.markdown(f"""
    <div class="panel">
        <div class="panel-heading">Forecast time highlights</div>
        <div style="margin-top:12px;">
            <span style="color:#8CCF9B; font-size:11px;
                         letter-spacing:1px;">
                LOWEST ESTIMATED AQI
            </span>
            <div style="font-size:19px; color:#EDF5EF;
                        font-weight:700;">
                {best_time}
            </div>
            <div class="metric-note">
                AQI {best_row['Predicted AQI']:.0f}
            </div>
        </div>
        <hr>
        <div>
            <span style="color:#D6A17E; font-size:11px;
                         letter-spacing:1px;">
                HIGHEST ESTIMATED AQI
            </span>
            <div style="font-size:19px; color:#EDF5EF;
                        font-weight:700;">
                {worst_time}
            </div>
            <div class="metric-note">
                AQI {worst_row['Predicted AQI']:.0f}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HISTORICAL ANALYSIS
# ============================================================

section_heading("06", "Historical performance")

hist1, hist2, hist3 = st.columns(3)

with hist1:
    st.metric("Historical average", f"{average_aqi:.1f}")

with hist2:
    st.metric(
        "Historical highest",
        f"{historical_data['AQI'].max():.0f}"
    )

with hist3:
    st.metric(
        "Historical lowest",
        f"{historical_data['AQI'].min():.0f}"
    )


with st.expander("View historical AQI readings"):

    display_history = historical_data.copy()

    display_history["Category"] = display_history["AQI"].apply(
        lambda x: get_aqi_category(x)[0]
    )

    st.dataframe(
        display_history.sort_values(
            "Timestamp", ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FORECAST TABLE
# ============================================================

section_heading("07", "Detailed forecast data")

display_forecast = forecast_data.copy()

display_forecast["Category"] = display_forecast[
    "Predicted AQI"
].apply(lambda x: get_aqi_category(x)[0])

display_forecast["Predicted AQI"] = (
    display_forecast["Predicted AQI"].round(1)
)

display_forecast["Lower estimate"] = (
    display_forecast["Lower estimate"].round(1)
)

display_forecast["Upper estimate"] = (
    display_forecast["Upper estimate"].round(1)
)

st.dataframe(
    display_forecast,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD FORECAST
# ============================================================

section_heading("08", "Export forecast")

download_data = forecast_data.copy()

download_data["Category"] = download_data[
    "Predicted AQI"
].apply(lambda x: get_aqi_category(x)[0])

csv_data = download_data.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download 24-hour forecast CSV",
    data=csv_data,
    file_name="aerosense_aqi_forecast.csv",
    mime="text/csv",
    use_container_width=False
)


# ============================================================
# METHODOLOGY / LIMITATIONS
# ============================================================

with st.expander("How does this prediction work?"):

    st.markdown("""
    **CURRENT FORECASTING METHOD**

    This page currently uses a statistical baseline:

    1. Reads historical AQI observations.
    2. Uses up to the latest 48 readings.
    3. Estimates the recent linear trend.
    4. Dampens the trend to reduce aggressive extrapolation.
    5. Produces estimates for the next 24 hours.
    6. Calculates an illustrative uncertainty range from recent residuals.

    **IMPORTANT LIMITATIONS**

    - This is not a trained machine-learning model.
    - It does not currently use weather variables.
    - It cannot reliably anticipate sudden pollution events.
    - Forecast quality depends on the quality and frequency of historical data.
    - The forecast should not be treated as an official air-quality warning.

    **PLANNED MODEL INTEGRATION**

    The baseline can later be replaced with your team's trained model,
    using historical AQI, PM2.5, PM10, temperature, humidity, wind speed
    and other available features.
    """)


# ============================================================
# FOOTER
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
        'DATA · ANALYTICS · PREDICTION'
        '</div>',
        unsafe_allow_html=True
    )
