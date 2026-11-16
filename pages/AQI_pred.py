
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from io import BytesIO

# ============================================================
# AEROSENSE AI — AQI PREDICTION
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #101512;
    color: #E7EEE8;
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    color: #E8F0E9 !important;
}

p, label, span {
    color: #C2CEC5;
}

.hero {
    background: linear-gradient(120deg, #1A2921, #17251F 55%, #1B3029);
    border: 1px solid #34483B;
    border-radius: 18px;
    padding: 28px 32px;
    margin-bottom: 25px;
}

.hero-tag {
    color: #9CBDA6;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
    text-transform: uppercase;
}

.hero-title {
    color: #F0F5F0;
    font-family: 'Manrope', sans-serif;
    font-size: 34px;
    font-weight: 800;
    margin-top: 8px;
    margin-bottom: 8px;
}

.hero-sub {
    color: #AABBB0;
    font-size: 14px;
    max-width: 750px;
    line-height: 1.7;
}

.section-title {
    font-family: 'Manrope', sans-serif;
    color: #E5EEE7;
    font-size: 19px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 13px;
}

.metric-card {
    background: #19211C;
    border: 1px solid #303E34;
    border-radius: 14px;
    padding: 18px 20px;
    min-height: 112px;
}

.metric-label {
    color: #91A397;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 700;
}

.metric-value {
    color: #EDF4EE;
    font-family: 'Manrope', sans-serif;
    font-size: 29px;
    font-weight: 800;
    margin-top: 9px;
}

.metric-note {
    color: #91A397;
    font-size: 12px;
    margin-top: 4px;
}

.panel {
    background: #19211C;
    border: 1px solid #303E34;
    border-radius: 15px;
    padding: 20px 22px;
    margin-bottom: 15px;
}

.panel-heading {
    color: #E5EEE7;
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

.status-pill {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.good {
    background: #1D3B2C;
    color: #91D6A8;
}

.satisfactory {
    background: #35412A;
    color: #C3D98C;
}

.moderate {
    background: #4A3C22;
    color: #EBC47A;
}

.poor {
    background: #4A2E24;
    color: #E6A078;
}

.very-poor {
    background: #48252A;
    color: #E58C91;
}

.severe {
    background: #4A2020;
    color: #F08D82;
}

.notice {
    background: #202C25;
    border-left: 3px solid #83B394;
    padding: 13px 16px;
    border-radius: 7px;
    color: #B7C7BB;
    font-size: 13px;
    line-height: 1.6;
    margin: 12px 0;
}

div[data-testid="stMetric"] {
    background: #19211C;
    border: 1px solid #303E34;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetric"] label {
    color: #91A397 !important;
}

div[data-testid="stMetricValue"] {
    color: #EAF2EB !important;
}

.stButton > button, .stDownloadButton > button {
    background: #789D83;
    color: #101812;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    padding: 9px 18px;
}

.stButton > button:hover, .stDownloadButton > button:hover {
    background: #91B59B;
    color: #101812;
    border: none;
}

.stTextInput input, .stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #202A23 !important;
    color: #E5EEE7 !important;
}

hr {
    border-color: #303E34;
}

.footer {
    color: #718278;
    font-size: 11px;
    text-align: center;
    margin-top: 35px;
    padding-top: 15px;
    border-top: 1px solid #29352D;
}
</style>
""", unsafe_allow_html=True)


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

    # Use up to the most recent 48 readings
    recent = values[-48:]

    x = np.arange(len(recent))

    # Estimate recent linear trend
    slope, intercept = np.polyfit(x, recent, 1)

    fitted = slope * x + intercept
    residuals = recent - fitted

    # Estimate variability from recent observations
    residual_std = float(np.std(residuals))

    # Avoid excessively aggressive extrapolation
    damped_slope = np.clip(slope, -2.5, 2.5) * 0.35

    last_value = float(recent[-1])

    future_steps = np.arange(1, forecast_hours + 1)

    predicted = last_value + damped_slope * future_steps

    # Keep predictions within the India AQI scale
    predicted = np.clip(predicted, 0, 500)

    # Uncertainty grows with forecast distance
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
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">AEROSENSE AI / INTELLIGENCE MODULE 04</div>
    <div class="hero-title">AQI Prediction</div>
    <div class="hero-sub">
        Explore short-term air quality forecasts, identify potential
        pollution changes and understand the uncertainty behind
        predicted conditions.
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# DATA INPUT
# ============================================================

st.markdown(
    '<div class="section-title">01 / Historical data source</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1.5, 1])

with left:
    uploaded_file = st.file_uploader(
        "Upload historical AQI data (CSV)",
        type=["csv"],
        help="Upload a CSV containing historical AQI readings."
    )

with right:
    st.markdown("""
    <div class="notice">
        <b>Data requirement</b><br>
        Ideally provide at least 24 historical hourly readings.
        More observations can produce a more informative baseline.
    </div>
    """, unsafe_allow_html=True)


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

    # Clearly labelled illustrative demo data
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

current_aqi = float(
    historical_data["AQI"].iloc[-1]
)

average_aqi = float(
    historical_data["AQI"].mean()
)

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

current_category, current_class = get_aqi_category(
    current_aqi
)

forecast_category, forecast_class = get_aqi_category(
    predicted_average
)


# ============================================================
# SUMMARY CARDS
# ============================================================

st.markdown(
    '<div class="section-title">02 / Forecast overview</div>',
    unsafe_allow_html=True
)

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

st.markdown(
    '<div class="section-title">03 / Expected air quality</div>',
    unsafe_allow_html=True
)

status_col, advisory_col = st.columns([1, 2])

with status_col:

    st.markdown(f"""
    <div class="panel">
        <div class="panel-caption">EXPECTED 24-HOUR CATEGORY</div>
        <div style="font-size:31px; font-weight:800;
                    font-family:Manrope; color:#EDF4EE;">
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
        <p style="font-size:14px; line-height:1.8; color:#B9C8BD;">
            {get_advisory(predicted_average)}
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FORECAST CHART
# ============================================================

st.markdown(
    '<div class="section-title">04 / 24-hour AQI forecast</div>',
    unsafe_allow_html=True
)

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

st.markdown(
    '<div class="section-title">05 / Forecast interpretation</div>',
    unsafe_allow_html=True
)

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
                    color:#A8C9AE; margin-top:12px;">
            {trend_text}
        </div>
        <p style="color:#AABBB0; font-size:13px;
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
            <span style="color:#91C9A0; font-size:12px;">
                LOWEST ESTIMATED AQI
            </span>
            <div style="font-size:19px; color:#E7EEE8;
                        font-weight:700;">
                {best_time}
            </div>
            <div class="metric-note">
                AQI {best_row['Predicted AQI']:.0f}
            </div>
        </div>
        <hr>
        <div>
            <span style="color:#D6A17E; font-size:12px;">
                HIGHEST ESTIMATED AQI
            </span>
            <div style="font-size:19px; color:#E7EEE8;
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

st.markdown(
    '<div class="section-title">06 / Historical performance</div>',
    unsafe_allow_html=True
)

hist1, hist2, hist3 = st.columns(3)

with hist1:
    st.metric(
        "Historical average",
        f"{average_aqi:.1f}"
    )

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

st.markdown(
    '<div class="section-title">07 / Detailed forecast data</div>',
    unsafe_allow_html=True
)

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

st.markdown(
    '<div class="section-title">08 / Export forecast</div>',
    unsafe_allow_html=True
)

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
    **Current forecasting method**

    This page currently uses a statistical baseline:

    1. Reads historical AQI observations.
    2. Uses up to the latest 48 readings.
    3. Estimates the recent linear trend.
    4. Dampens the trend to reduce aggressive extrapolation.
    5. Produces estimates for the next 24 hours.
    6. Calculates an illustrative uncertainty range from recent residuals.

    **Important limitations**

    - This is not a trained machine-learning model.
    - It does not currently use weather variables.
    - It cannot reliably anticipate sudden pollution events.
    - Forecast quality depends on the quality and frequency of historical data.
    - The forecast should not be treated as an official air-quality warning.

    **Planned model integration**

    The baseline can later be replaced with your team's trained model,
    using historical AQI, PM2.5, PM10, temperature, humidity, wind speed
    and other available features.
    """)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    AEROSENSE AI · AIR QUALITY INTELLIGENCE PLATFORM<br>
    Forecasts are estimates for informational and project demonstration
    purposes. Refer to official monitoring sources for current AQI.
</div>
""", unsafe_allow_html=True)
