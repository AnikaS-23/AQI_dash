import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Bengaluru Weather Insights")

df = pd.read_csv("data/processed/airscope_sample.csv")
df = df[df["city"] == "Bengaluru"].copy()
df["time"] = pd.to_datetime(df["time"], errors="coerce")

weather_columns = ["temperature", "humidity", "wind_speed", "rain"]

for column in weather_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

station = st.selectbox("Choose a station", sorted(df["name"].dropna().unique()))
station_df = df[df["name"] == station].sort_values("time")

for column in weather_columns:
    chart = px.line(
        station_df,
        x="time",
        y=column,
        title=f"{column.replace('_', ' ').title()} over time — {station}",
        labels={"time": "Time", column: column.replace("_", " ").title()},
    )
    st.plotly_chart(chart, use_container_width=True)