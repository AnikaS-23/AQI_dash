"""Shared look and feel. Every page starts with: apply_theme("Page name", "icon")."""
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
APP_NAME = "HazeCheck"

# (low, high, label, color, text color, advice). CPCB India bands.
# Keep in sync with utils/aqi_calculator.py (Person 3).
BANDS = [
    (0, 50, "Good", "#2FA36B", "#10262E", "Clean air. Enjoy the outdoors."),
    (51, 100, "Satisfactory", "#9CC94B", "#10262E", "Fine for most people. Very sensitive groups may notice it."),
    (101, 200, "Moderate", "#F2C230", "#10262E", "People with asthma or heart conditions should take it easy outside."),
    (201, 300, "Poor", "#F28A2E", "#10262E", "Limit long outdoor activity. Consider a mask."),
    (301, 400, "Very poor", "#DC4B3E", "#FFFFFF", "Avoid outdoor exercise. Keep windows closed."),
    (401, 500, "Severe", "#8B2C5E", "#FFFFFF", "Stay indoors if you can. Wear an N95 outside."),
]


def aqi_band(v):
    for b in BANDS:
        if v <= b[1]:
            return b
    return BANDS[-1]


def apply_theme(page_title=APP_NAME, icon="🌫️"):
    st.set_page_config(page_title=f"{page_title} | {APP_NAME}", page_icon=icon, layout="wide")
    css = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def ribbon(aqi):
    segs = "".join(f'<span style="flex:{max(hi - lo, 1)};background:{c}"></span>' for lo, hi, _, c, _, _ in BANDS)
    pos = min(aqi, 500) / 5
    labels = "".join(f"<span>{n}</span>" for n in (0, 50, 100, 200, 300, 400, 500))
    return (f'<div class="ribbon">{segs}<div class="marker" style="--pos:{pos}%"></div></div>'
            f'<div class="ribbon-labels">{labels}</div>')


def tile(label, value, unit="", note=""):
    return (f'<div class="tile"><div class="k">{label}</div>'
            f'<div class="v">{value}<small>{unit}</small></div><div class="d">{note}</div></div>')


def style_fig(fig):
    fig.update_layout(font_family="DM Sans", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(l=10, r=10, t=30, b=10), legend=dict(orientation="h", y=1.12))
    fig.update_xaxes(gridcolor="#D5E1E6", showline=False)
    fig.update_yaxes(gridcolor="#D5E1E6", showline=False)
    return fig


def latest(df, city):
    d = df[df["city"] == city].sort_values("date")
    return d.iloc[-1], (d.iloc[-2] if len(d) > 1 else d.iloc[-1])


def demo_data():
    rng = np.random.default_rng(7)
    days = pd.date_range(end=pd.Timestamp.today().normalize(), periods=180)
    doy = days.dayofyear.values
    rows = []
    for city, base in {"Bengaluru": 70, "Delhi": 210, "Mumbai": 110, "Chennai": 85, "Kolkata": 150}.items():
        n = len(days)
        wind = np.clip(rng.normal(9, 3, n), 1, 20)
        season = 1 + 0.35 * np.cos((doy - 20) / 365 * 2 * np.pi)
        pm25 = np.clip(base * 0.5 * season * (10 / wind) ** 0.5 + rng.normal(0, 6, n), 5, 400)
        rows.append(pd.DataFrame({
            "date": days, "city": city,
            "aqi": np.clip(pm25 * 1.7 + rng.normal(0, 8, n), 10, 500).round(),
            "pm25": pm25.round(1), "pm10": (pm25 * 1.8 + rng.normal(0, 8, n)).round(1),
            "no2": (pm25 * 0.35 + rng.normal(0, 3, n)).round(1),
            "temperature": (26 + 5 * np.cos((doy - 120) / 365 * 2 * np.pi) + rng.normal(0, 1.5, n)).round(1),
            "humidity": np.clip(65 + rng.normal(0, 12, n), 20, 98).round(),
            "wind_speed": wind.round(1)}))
    return pd.concat(rows, ignore_index=True)


@st.cache_data(show_spinner=False)
def get_data():
    """Returns (df, is_demo). Uses Person 2's modules when they exist, else demo data.
    Expected columns: date, city, aqi, pm25, pm10, temperature, humidity, wind_speed."""
    try:
        from modules.data_loader import load_data
        df = load_data(load_data())
        df["date"] = pd.to_datetime(df["date"])
        return df, False
    except Exception:
        return demo_data(), True
