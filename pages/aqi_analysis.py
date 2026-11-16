import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Bengaluru AQI", page_icon="🌈", layout="wide")

# Colorful page styling
st.markdown("""
<style>
    .main {background-color: #f5f7ff;}
    .aqi-card {
        padding: 18px;
        border-radius: 16px;
        color: white;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌈 Bengaluru Air Quality")
st.caption("Explore estimated air-quality readings by monitoring station.")

@st.cache_data
def load_data():
    data = pd.read_csv("data/processed/airscope_sample.csv")
    data = data[data["city"] == "Bengaluru"].copy()
    data["time"] = pd.to_datetime(data["time"], errors="coerce")
    data["aqi"] = pd.to_numeric(data["aqi"], errors="coerce")
    return data.dropna(subset=["time", "aqi"])

df = load_data()

if df.empty:
    st.warning("No Bengaluru AQI data was found.")
else:
    station = st.selectbox(
        "📍 Choose a Bengaluru station",
        sorted(df["name"].dropna().unique())
    )
    station_df = df[df["name"] == station].sort_values("time")
    latest = station_df.iloc[-1]

    aqi = latest["aqi"]
    if aqi <= 50:
        category, color, emoji = "Good", "#16a34a", "🟢"
    elif aqi <= 100:
        category, color, emoji = "Satisfactory", "#65a30d", "🟡"
    elif aqi <= 200:
        category, color, emoji = "Moderate", "#f59e0b", "🟠"
    elif aqi <= 300:
        category, color, emoji = "Poor", "#ea580c", "🔴"
    elif aqi <= 400:
        category, color, emoji = "Very Poor", "#9333ea", "🟣"
    else:
        category, color, emoji = "Severe", "#7f1d1d", "🟤"

    col1, col2, col3 = st.columns(3)
    col1.metric("Latest AQI", f"{aqi:.0f}")
    col2.metric("Category", f"{emoji} {category}")
    col3.metric("Main pollutant", str(latest.get("main_pollutant", "Unknown")))

    st.markdown(
        f'<div class="aqi-card" style="background:{color}">'
        f'{emoji} {category} air quality · AQI {aqi:.0f}</div>',
        unsafe_allow_html=True
    )

    chart = px.line(
        station_df,
        x="time",
        y="aqi",
        title=f"📈 AQI trend — {station}",
        labels={"time": "Date and time", "aqi": "AQI"},
        color_discrete_sequence=[color],
    )
    chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_color="#312e81",
    )
    st.plotly_chart(chart, use_container_width=True)

    st.caption("Dataset readings are estimates, not official real-time station measurements.")