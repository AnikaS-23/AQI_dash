
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Air Quality Overview | AeroSense AI",
    page_icon="🌍",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

for folder in ["assets", "assests"]:
    css_file = BASE_DIR / folder / "style.css"
    if css_file.exists():
        st.markdown(
            f"<style>{css_file.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )
        break


# --------------------------------------------------
# AEROSENSE AI DARK THEME
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #080B0A;
    --surface: #111815;
    --surface2: #151F1A;
    --border: #26382E;
    --green: #8CCF9B;
    --teal: #4CA99A;
    --white: #EDF5EF;
    --muted: #91A397;
}

/* MAIN BACKGROUND */

.stApp {
    background: #080B0A !important;
    color: #EDF5EF !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: #080B0A !important;
}

[data-testid="stHeader"] {
    background: rgba(8, 11, 10, 0.95) !important;
}

.block-container {
    max-width: 1450px;
    padding-top: 2.3rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0B110E !important;
    border-right: 1px solid #1F3025;
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

/* GENERAL TYPOGRAPHY */

h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: #EDF5EF !important;
    font-weight: 700 !important;
}

p, li, label {
    color: #C0CEC3;
}

[data-testid="stCaptionContainer"] {
    color: #91A397 !important;
}

.stMarkdown {
    color: #DCE9DF;
}

/* PAGE HEADER */

.page-title {
    font-family: 'Manrope', sans-serif;
    font-size: 35px;
    font-weight: 800;
    letter-spacing: -1.3px;
    color: #EDF5EF;
    margin-bottom: 7px;
}

.page-subtitle {
    color: #8CCF9B;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

.demo-label {
    text-align: right;
    color: #9AD8A7;
    background: #14251A;
    border: 1px solid #31563B;
    border-radius: 30px;
    padding: 9px 13px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    display: inline-block;
    float: right;
}

/* SECTION HEADINGS */

h3 {
    font-size: 18px !important;
    margin-top: 28px !important;
    margin-bottom: 17px !important;
}

/* DASHBOARD PANELS */

.dashboard-panel {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 16px;
    padding: 21px;
    margin-bottom: 15px;
    color: #EDF5EF;
}

.dashboard-panel strong {
    color: #EAF4EC;
}

.dashboard-panel hr {
    border-color: #293B30;
}

/* AQI PANEL */

.aqi-panel {
    text-align: center;
    min-height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.big-aqi {
    font-family: 'Manrope', sans-serif;
    font-size: 76px;
    font-weight: 800;
    letter-spacing: -3px;
    line-height: 1.2;
    margin: 16px 0;
}

.aqi-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin: 0 auto;
}

/* METRIC CARDS */

.metric-box {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 14px;
    padding: 19px 16px;
    min-height: 115px;
    transition: border-color 0.2s ease;
}

.metric-box:hover {
    border-color: #60966D;
}

.metric-name {
    color: #91A397;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
    margin-bottom: 13px;
}

.metric-number {
    color: #EDF5EF;
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    font-weight: 800;
}

.metric-unit {
    color: #7F9586;
    font-size: 11px;
    margin-top: 3px;
}

/* HEALTH TIPS */

.tip-row {
    color: #B9C9BD;
    font-size: 13px;
    line-height: 1.7;
    padding: 11px 0;
    border-bottom: 1px solid #26382E;
}

.tip-row:last-child {
    border-bottom: none;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border: 1px solid #26382E;
    border-radius: 10px;
    overflow: hidden;
}

/* INPUTS */

.stSelectbox label,
.stDateInput label,
.stFileUploader label {
    color: #C7D6CA !important;
    font-weight: 600;
}

[data-testid="stFileUploader"] {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="stFileUploaderDropzone"] {
    background: #151F1A;
    border: 1px dashed #496C53;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #DCE9DF !important;
}

[data-baseweb="input"],
[data-baseweb="select"] > div,
[data-testid="stDateInput"] input {
    background: #151F1A !important;
    color: #EDF5EF !important;
    border-color: #344A3A !important;
}

[data-baseweb="popover"] {
    background: #111815 !important;
}

/* CHARTS */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stPlotlyChart"] {
    background: #111815;
    border-radius: 12px;
}

/* MAP */

[data-testid="stDeckGlJsonChart"] {
    border-radius: 12px;
    overflow: hidden;
}

/* DIVIDERS */

hr {
    border-color: #26382E !important;
}

/* STREAMLIT METRICS */

div[data-testid="stMetric"] {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 13px;
    padding: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #91A397;
}

div[data-testid="stMetricValue"] {
    color: #EDF5EF;
}

/* ALERTS */

[data-testid="stAlert"] {
    background: #142019;
    border: 1px solid #35553D;
    border-radius: 10px;
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

/* FOOTER */

.footer {
    color: #71847A;
    font-size: 10px;
    letter-spacing: 1.5px;
    border-top: 1px solid #26382E;
    padding-top: 20px;
    margin-top: 35px;
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
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DEMO DATA
# --------------------------------------------------

@st.cache_data
def make_demo_data():
    rng = np.random.default_rng(42)

    locations = {
        "Bengaluru Central": (12.9716, 77.5946),
        "Whitefield": (12.9698, 77.7500),
        "Electronic City": (12.8452, 77.6602),
        "Hebbal": (13.0358, 77.5970),
        "Jayanagar": (12.9250, 77.5838),
        "Peenya": (13.0285, 77.5197),
        "Silk Board": (12.9177, 77.6233)
    }

    rows = []

    for day in range(14):
        date = (
            pd.Timestamp.today().normalize()
            - pd.Timedelta(days=13-day)
        )

        for station, (lat, lon) in locations.items():
            rows.append({
                "Date": date,
                "Station": station,
                "AQI": int(rng.integers(35, 190)),
                "PM25": round(float(rng.uniform(12, 85)), 1),
                "PM10": round(float(rng.uniform(20, 130)), 1),
                "Temperature": round(float(rng.uniform(23, 33)), 1),
                "Humidity": int(rng.uniform(40, 90)),
                "Wind": round(float(rng.uniform(3, 18)), 1),
                "lat": lat,
                "lon": lon
            })

    return pd.DataFrame(rows)


def prepare_uploaded_data(file):
    data = pd.read_csv(file)

    aliases = {
        "date": "Date",
        "datetime": "Date",
        "timestamp": "Date",
        "station": "Station",
        "location": "Station",
        "aqi": "AQI",
        "pm2.5": "PM25",
        "pm25": "PM25",
        "pm10": "PM10",
        "temperature": "Temperature",
        "temp": "Temperature",
        "humidity": "Humidity",
        "wind": "Wind",
        "wind speed": "Wind",
        "latitude": "lat",
        "longitude": "lon"
    }

    rename = {}
    for column in data.columns:
        key = str(column).strip().lower()
        if key in aliases:
            rename[column] = aliases[key]

    data = data.rename(columns=rename)

    if "AQI" not in data.columns:
        raise ValueError("Your CSV needs a column named AQI.")

    if "Date" not in data.columns:
        data["Date"] = pd.Timestamp.today().normalize()
    else:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

    if "Station" not in data.columns:
        data["Station"] = "Uploaded station"

    numeric_columns = [
        "AQI", "PM25", "PM10", "Temperature",
        "Humidity", "Wind", "lat", "lon"
    ]

    for column in numeric_columns:
        if column not in data.columns:
            data[column] = np.nan
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna(subset=["AQI", "Date"]).copy()

    if data.empty:
        raise ValueError("No valid AQI and date records were found.")

    # Missing coordinates are not invented.
    return data


def get_status(aqi):
    if aqi <= 50:
        return "Good", "#65b98a"
    if aqi <= 100:
        return "Satisfactory", "#a4c77b"
    if aqi <= 200:
        return "Moderate", "#e4b65e"
    if aqi <= 300:
        return "Poor", "#e58b59"
    if aqi <= 400:
        return "Very Poor", "#dd655c"
    return "Severe", "#a95a74"


def average(data, column):
    if column not in data.columns:
        return None
    value = data[column].mean()
    return None if pd.isna(value) else float(value)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

if "aero_data" not in st.session_state:
    st.session_state.aero_data = make_demo_data()
    st.session_state.demo_mode = True

st.sidebar.markdown("## AEROSENSE AI")
st.sidebar.caption("Environmental intelligence")

uploaded_file = st.sidebar.file_uploader(
    "Upload your dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        st.session_state.aero_data = prepare_uploaded_data(uploaded_file)
        st.session_state.demo_mode = False
        st.sidebar.success("Dataset loaded!")
    except Exception as error:
        st.sidebar.error(str(error))

df = st.session_state.aero_data.copy()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date", "AQI"])

if df.empty:
    st.error("There are no valid records to display.")
    st.stop()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

title_col, status_col = st.columns([3, 1])

with title_col:
    st.markdown("""
    <div class="page-title">Air Quality Overview</div>
    <div class="page-subtitle">
        BENGALURU · ENVIRONMENTAL MONITORING
    </div>
    """, unsafe_allow_html=True)

with status_col:
    if st.session_state.demo_mode:
        st.markdown(
            '<div class="demo-label">● DEMO DATA</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="demo-label">● UPLOADED DATA</div>',
            unsafe_allow_html=True
        )


# --------------------------------------------------
# DATE FILTER
# --------------------------------------------------

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

selected_dates = st.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date)
    ].copy()
else:
    filtered = df.copy()

if filtered.empty:
    st.warning("No records found for this date range.")
    st.stop()

latest_date = filtered["Date"].max().date()
latest = filtered[filtered["Date"].dt.date == latest_date].copy()

current_aqi = int(round(latest["AQI"].mean()))
status, status_color = get_status(current_aqi)


# --------------------------------------------------
# MAP AND AQI PANEL
# --------------------------------------------------

st.markdown("### Monitoring network")

map_col, aqi_col = st.columns([2.2, 0.8], gap="medium")

with map_col:
    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown("**Bengaluru monitoring stations**")

    map_data = latest.dropna(subset=["lat", "lon"])[
        ["lat", "lon", "Station", "AQI"]
    ].copy()

    if not map_data.empty:
        st.map(
            map_data,
            latitude="lat",
            longitude="lon",
            size=50,
            color="#82b99a",
            zoom=10
        )
    else:
        st.info(
            "No latitude and longitude columns were found. "
            "Your dataset can still be analysed using its AQI values."
        )

    st.caption(
        "Map markers show available station coordinates. "
        "Demo coordinates are illustrative."
    )
    st.markdown('</div>', unsafe_allow_html=True)

with aqi_col:
    st.markdown('<div class="dashboard-panel aqi-panel">', unsafe_allow_html=True)
    st.markdown("**CITY AQI INDEX**")

    st.markdown(
        f'<div class="big-aqi" style="color:{status_color}">{current_aqi}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="aqi-badge" style="color:{status_color};background:{status_color}22">'
        f'{status.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption(f"Latest available date: {latest_date.strftime('%d %b %Y')}")
    st.caption("Average of available station readings.")
    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# ENVIRONMENTAL METRICS
# --------------------------------------------------

st.markdown("### Environmental conditions")

pm25 = average(latest, "PM25")
pm10 = average(latest, "PM10")
temp = average(latest, "Temperature")
humidity = average(latest, "Humidity")
wind = average(latest, "Wind")

metric_cols = st.columns(5)

metrics = [
    ("PM2.5", pm25, "µg/m³"),
    ("PM10", pm10, "µg/m³"),
    ("Temperature", temp, "°C"),
    ("Humidity", humidity, "%"),
    ("Wind speed", wind, "km/h")
]

for col, (label, value, unit) in zip(metric_cols, metrics):
    with col:
        display = "—" if value is None else f"{value:.1f}"
        st.markdown(
            f'<div class="metric-box">'
            f'<div class="metric-name">{label}</div>'
            f'<div class="metric-number">{display}</div>'
            f'<div class="metric-unit">{unit}</div>'
            f'</div>',
            unsafe_allow_html=True
        )


# --------------------------------------------------
# SIMPLE AQI TREND
# --------------------------------------------------

st.markdown("### Air quality trends")

trend_col, station_col = st.columns(2, gap="medium")

with trend_col:
    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown("**Daily average AQI**")

    daily = (
        filtered.groupby(filtered["Date"].dt.date)["AQI"]
        .mean()
        .reset_index()
    )

    daily.columns = ["Date", "Average AQI"]

    st.bar_chart(
        daily,
        x="Date",
        y="Average AQI",
        color="#82b99a",
        height=270
    )

    st.caption("Lower values indicate better air quality.")
    st.markdown('</div>', unsafe_allow_html=True)

with station_col:
    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown("**Station AQI comparison**")

    station_data = (
        latest.groupby("Station", as_index=False)["AQI"]
        .mean()
        .sort_values("AQI", ascending=False)
    )

    st.bar_chart(
        station_data,
        x="Station",
        y="AQI",
        color="#d6a875",
        horizontal=True,
        height=270
    )

    st.caption("Compare the average AQI across monitoring stations.")
    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# HEALTH TIPS AND WATCHLIST
# --------------------------------------------------

st.markdown("### Local insights")

tips_col, watch_col = st.columns([0.9, 1.5], gap="medium")

with tips_col:
    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown("**Health advisory**")

    if current_aqi <= 50:
        tips = [
            "Air quality is in the good category.",
            "Continue normal outdoor activities.",
            "Keep checking conditions as they change."
        ]
    elif current_aqi <= 100:
        tips = [
            "Air quality is generally satisfactory.",
            "Sensitive individuals should monitor symptoms.",
            "Check local readings before long outdoor activities."
        ]
    elif current_aqi <= 200:
        tips = [
            "Sensitive individuals should reduce prolonged outdoor exertion.",
            "Take breaks during strenuous outdoor activities.",
            "Follow local public-health guidance."
        ]
    else:
        tips = [
            "Limit prolonged outdoor exertion.",
            "Consider moving strenuous activity indoors.",
            "Follow official air-quality health advisories."
        ]

    for tip in tips:
        st.markdown(
            f'<div class="tip-row">✦ &nbsp; {tip}</div>',
            unsafe_allow_html=True
        )

    st.caption("General information, not a medical diagnosis.")
    st.markdown('</div>', unsafe_allow_html=True)

with watch_col:
    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown("**Station watchlist**")

    watchlist = (
        latest.groupby("Station", as_index=False)
        .agg(
            AQI=("AQI", "mean"),
            PM25=("PM25", "mean"),
            Temperature=("Temperature", "mean")
        )
        .sort_values("AQI", ascending=False)
    )

    watchlist["AQI"] = watchlist["AQI"].round(0).astype(int)
    watchlist["PM25"] = watchlist["PM25"].round(1)
    watchlist["Temperature"] = watchlist["Temperature"].round(1)

    st.dataframe(
        watchlist,
        use_container_width=True,
        hide_index=True,
        height=260
    )

    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    AEROSENSE AI · AIR QUALITY & WEATHER INTELLIGENCE
</div>
""", unsafe_allow_html=True)
