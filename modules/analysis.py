import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Bengaluru Air Quality")

df = pd.read_csv("data/processed/airscope_sample.csv")
df = df[df["city"] == "Bengaluru"].copy()
df["time"] = pd.to_datetime(df["time"], errors="coerce")
df["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")
df = df.dropna(subset=["time", "aqi"])

if df.empty:
    st.warning("No Bengaluru AQI rows were found in the CSV.")
else:
    station = st.selectbox("Choose a station", sorted(df["name"].dropna().unique()))
    station_df = df[df["name"] == station].sort_values("time")

    chart = px.line(
        station_df,
        x="time",
        y="aqi",
        title=f"AQI over time — {station}",
        labels={"time": "Time", "aqi": "AQI"},
    )
    st.plotly_chart(chart, use_container_width=True)
    