
import pandas as pd
import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Weather Insights | AeroSense AI",
    page_icon="🌿",
    layout="wide"
)

# Load dataset
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

# Header
st.markdown("""
<div class="topbar">
    <div>
        <div class="brand">AEROSENSE <span>AI</span></div>
        <div class="brand-sub">AIR QUALITY INTELLIGENCE PLATFORM</div>
    </div>
    <div class="system-status">● WEATHER INSIGHTS</div>
</div>
""", unsafe_allow_html=True)

# Page introduction
st.markdown("""
<div style="padding: 35px 5px 20px;">
    <div class="eyebrow">ENVIRONMENTAL INTELLIGENCE · BENGALURU</div>
    <h1 style="font-size:38px; margin:12px 0;">
        Weather <span style="color:#9ac7a9;">Insights.</span>
    </h1>
    <p style="color:#89938f; font-size:13px;">
        Explore weather patterns and understand changing
        environmental conditions across Bengaluru.
    </p>
</div>
""", unsafe_allow_html=True)

# Station selector
st.markdown('<div class="section-label">STATION SELECTION</div>',
            unsafe_allow_html=True)

stations = sorted(df["name"].dropna().unique())

if not stations:
    st.warning("No Bengaluru weather station data available.")
    st.stop()

station = st.selectbox("Choose a monitoring station", stations)

station_df = df[df["name"] == station].sort_values("time")

# Latest available readings
latest = station_df.dropna(subset=weather_columns, how="all")

if latest.empty:
    st.warning("No weather readings available for this station.")
    st.stop()

latest = latest.iloc[-1]

# Metric cards
st.markdown('<div class="section-label">CURRENT WEATHER SNAPSHOT</div>',
            unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

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

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# Weather trends
st.markdown('<div class="section-label">WEATHER TREND ANALYSIS</div>',
            unsafe_allow_html=True)

st.markdown(f"""
<div class="page-subtitle">
    HISTORICAL WEATHER PATTERNS · {station.upper()}
</div>
""", unsafe_allow_html=True)

# Plotly chart styling
chart_titles = {
    "temperature": "Temperature",
    "humidity": "Humidity",
    "wind_speed": "Wind Speed",
    "rain": "Rainfall"
}

for i in range(0, len(weather_columns), 2):
    col1, col2 = st.columns(2)

    for col, column in zip(
        [col1, col2],
        weather_columns[i:i+2]
    ):
        chart_data = station_df.dropna(subset=[column])

        with col:
            st.markdown('<div class="dashboard-panel">',
                        unsafe_allow_html=True)

            if chart_data.empty:
                st.info(f"No data available for {chart_titles[column]}")
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
                    line=dict(color="#9ac7a9", width=2.5),
                    marker=dict(size=5)
                )

                fig.update_layout(
                    paper_bgcolor="#14191a",
                    plot_bgcolor="#14191a",
                    font=dict(color="#edf0ed"),
                    title_font=dict(size=16),
                    margin=dict(l=15, r=15, t=45, b=15),
                    height=320,
                    hovermode="x unified",
                    xaxis=dict(
                        showgrid=False,
                        color="#89938f"
                    ),
                    yaxis=dict(
                        gridcolor="#303939",
                        color="#89938f",
                        zeroline=False
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    AEROSENSE AI · WEATHER INTELLIGENCE · BENGALURU
</div>
""", unsafe_allow_html=True)
