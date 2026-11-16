
import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Weather Insights | AeroSense AI",
    page_icon="🌿",
    layout="wide"
)


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

/* GENERAL TEXT */

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

/* HEADER */

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 15px;
    padding: 19px 24px;
    margin-bottom: 32px;
}

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #EDF5EF;
}

.brand span {
    color: #8CCF9B;
}

.brand-sub {
    color: #819489;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 5px;
}

.system-status {
    color: #9AD8A7;
    background: #14251A;
    border: 1px solid #31563B;
    border-radius: 30px;
    padding: 8px 13px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* INTRODUCTION */

.eyebrow {
    color: #8CCF9B;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
}

.hero-description {
    color: #91A397;
    font-size: 14px;
    line-height: 1.9;
    max-width: 750px;
}

.page-subtitle {
    color: #819489;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;
    margin-top: -8px;
    margin-bottom: 18px;
}

/* SECTION LABELS */

.section-label {
    color: #9ACBA3;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 22px;
    margin-bottom: 15px;
}

/* SELECTBOX */

.stSelectbox label {
    color: #C7D6CA !important;
    font-weight: 600;
}

[data-baseweb="select"] > div {
    background: #151F1A !important;
    border: 1px solid #344A3A !important;
    border-radius: 9px !important;
    color: #EDF5EF !important;
}

[data-baseweb="select"] * {
    color: #EDF5EF !important;
}

[data-baseweb="popover"] {
    background: #111815 !important;
}

/* METRIC CARDS */

.metric-box {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 15px;
    padding: 21px 19px;
    min-height: 145px;
    transition: border-color 0.2s ease, transform 0.2s ease;
}

.metric-box:hover {
    border-color: #60966D;
    transform: translateY(-2px);
}

.metric-name {
    color: #91A397;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.2px;
    margin-bottom: 18px;
}

.metric-number {
    color: #EDF5EF;
    font-family: 'Manrope', sans-serif;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
}

.metric-unit {
    color: #7F9586;
    font-size: 11px;
    margin-top: 5px;
}

/* CHART PANELS */

.dashboard-panel {
    background: #111815;
    border: 1px solid #26382E;
    border-radius: 15px;
    padding: 13px;
    margin-top: 12px;
    margin-bottom: 15px;
}

.dashboard-panel:hover {
    border-color: #496B51;
}

/* PLOTLY CHART CONTAINERS */

[data-testid="stPlotlyChart"] {
    background: transparent !important;
    border-radius: 12px;
}

/* DIVIDERS */

hr {
    border-color: #26382E !important;
}

/* ALERTS */

[data-testid="stAlert"] {
    background: #142019;
    border: 1px solid #35553D;
    border-radius: 10px;
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
# LOAD DATASET
# --------------------------------------------------

df = pd.read_csv("data/processed/airscope_sample.csv")
df = df[df["city"] == "Bengaluru"].copy()

df["time"] = pd.to_datetime(df["time"], errors="coerce")

weather_columns = [
    "temperature",
    "humidity",
    "wind_speed",
    "rain"
]

for column in weather_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=["time", "name"])


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="topbar">
    <div>
        <div class="brand">● AEROSENSE <span>AI</span></div>
        <div class="brand-sub">AIR QUALITY INTELLIGENCE PLATFORM</div>
    </div>
    <div class="system-status">● WEATHER INSIGHTS</div>
</div>
""", unsafe_allow_html=True)



# --------------------------------------------------
# PAGE INTRODUCTION
# --------------------------------------------------

st.markdown(
    '<div class="eyebrow">ENVIRONMENTAL INTELLIGENCE · BENGALURU</div>',
    unsafe_allow_html=True
)

st.title("Weather Insights.")

st.markdown(
    "Explore weather patterns and understand changing "
    "environmental conditions across Bengaluru."
)

st.write("")


# --------------------------------------------------
# STATION SELECTOR
# --------------------------------------------------

st.markdown(
    '<div class="section-label">01 / STATION SELECTION</div>',
    unsafe_allow_html=True
)

stations = sorted(df["name"].dropna().unique())

if not stations:
    st.warning("No Bengaluru weather station data available.")
    st.stop()

station = st.selectbox("Choose a monitoring station", stations)

station_df = df[df["name"] == station].sort_values("time")


# --------------------------------------------------
# LATEST AVAILABLE READINGS
# --------------------------------------------------

latest = station_df.dropna(subset=weather_columns, how="all")

if latest.empty:
    st.warning("No weather readings available for this station.")
    st.stop()

latest = latest.iloc[-1]


# --------------------------------------------------
# WEATHER METRIC CARDS
# --------------------------------------------------

st.markdown(
    '<div class="section-label">02 / CURRENT WEATHER SNAPSHOT</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4, gap="medium")

metrics = [
    (col1, "TEMPERATURE", "temperature", "°C", "🌡️"),
    (col2, "HUMIDITY", "humidity", "%", "💧"),
    (col3, "WIND SPEED", "wind_speed", "m/s", "🌬️"),
    (col4, "RAINFALL", "rain", "mm", "🌧️")
]

for col, label, column, unit, icon in metrics:
    value = latest[column]

    with col:
        display_value = (
            f"{value:.1f}" if pd.notna(value) else "N/A"
        )

        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-name">{icon} {label}</div>
            <div class="metric-number">{display_value}</div>
            <div class="metric-unit">{unit}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown(
    "<div style='height:25px'></div>",
    unsafe_allow_html=True
)


# --------------------------------------------------
# WEATHER TREND ANALYSIS
# --------------------------------------------------

st.markdown(
    '<div class="section-label">03 / WEATHER TREND ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="page-subtitle">
    HISTORICAL WEATHER PATTERNS · {station.upper()}
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PLOTLY CHART STYLING
# --------------------------------------------------

chart_titles = {
    "temperature": "Temperature",
    "humidity": "Humidity",
    "wind_speed": "Wind Speed",
    "rain": "Rainfall"
}

for i in range(0, len(weather_columns), 2):
    col1, col2 = st.columns(2, gap="medium")

    for col, column in zip(
        [col1, col2],
        weather_columns[i:i+2]
    ):
        chart_data = station_df.dropna(subset=[column])

        with col:
            st.markdown(
                '<div class="dashboard-panel">',
                unsafe_allow_html=True
            )

            if chart_data.empty:
                st.info(
                    f"No data available for {chart_titles[column]}"
                )
            else:
                fig = px.line(
                    chart_data,
                    x="time",
                    y=column,
                    title=chart_titles[column],
                    labels={
                        "time": "Date and Time",
                        column: chart_titles[column]
                    },
                    markers=True
                )

                fig.update_traces(
                    line=dict(color="#8CCF9B", width=2.5),
                    marker=dict(
                        size=5,
                        color="#8CCF9B",
                        line=dict(color="#111815", width=1)
                    ),
                    hovertemplate=(
                        "%{x}<br>"
                        + chart_titles[column]
                        + ": %{y:.2f}<extra></extra>"
                    )
                )

                fig.update_layout(
                    paper_bgcolor="#111815",
                    plot_bgcolor="#111815",
                    font=dict(
                        family="DM Sans, sans-serif",
                        color="#C5D4C9",
                        size=11
                    ),
                    title=dict(
                        font=dict(
                            family="Manrope, sans-serif",
                            size=17,
                            color="#EDF5EF"
                        ),
                        x=0.03
                    ),
                    margin=dict(
                        l=15,
                        r=15,
                        t=55,
                        b=15
                    ),
                    height=320,
                    hovermode="x unified",
                    xaxis=dict(
                        showgrid=False,
                        color="#899B8F",
                        linecolor="#344A3A",
                        tickfont=dict(size=10)
                    ),
                    yaxis=dict(
                        gridcolor="#26382E",
                        color="#899B8F",
                        zeroline=False,
                        tickfont=dict(size=10)
                    ),
                    hoverlabel=dict(
                        bgcolor="#17231B",
                        bordercolor="#45634C",
                        font=dict(color="#EDF5EF")
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    AEROSENSE AI · WEATHER INTELLIGENCE · BENGALURU
</div>
""", unsafe_allow_html=True)
