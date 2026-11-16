
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AeroSense AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
BASE_DIR = Path(__file__).resolve().parent

for folder in ["assets", "assests"]:
    css_file = BASE_DIR / folder / "style.css"
    if css_file.exists():
        st.markdown(
            f"<style>{css_file.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )
        break

# Header
st.markdown("""
<div class="topbar">
    <div>
        <div class="brand">AEROSENSE <span>AI</span></div>
        <div class="brand-sub">AIR QUALITY INTELLIGENCE PLATFORM</div>
    </div>
    <div class="system-status">● SYSTEM ONLINE</div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="eyebrow">ENVIRONMENTAL INTELLIGENCE · BENGALURU</div>
    <h1>See the air.<br><span>Understand the impact.</span></h1>
    <p>
        An intelligent platform to explore air quality, monitor
        environmental conditions and understand weather patterns.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-label">YOUR ENVIRONMENT, AT A GLANCE</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">◉</div>
        <div class="feature-title">Air Quality Monitoring</div>
        <div class="feature-text">
            Explore AQI levels, pollutant concentrations and
            monitoring station data.
        </div>
        <div class="feature-tag">01 · MONITOR</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">☁</div>
        <div class="feature-title">Weather Insights</div>
        <div class="feature-text">
            Understand temperature, humidity, wind and their
            relationship with pollution.
        </div>
        <div class="feature-tag">02 · ANALYSE</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⌁</div>
        <div class="feature-title">AI Predictions</div>
        <div class="feature-text">
            Explore air-quality trends and short-term prediction
            capabilities.
        </div>
        <div class="feature-tag">03 · PREDICT</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

left, right = st.columns([1.5, 1])

with left:
    st.markdown("""
    <div class="welcome-panel">
        <div class="section-label">WELCOME TO AEROSENSE AI</div>
        <h2>Cleaner insights.<br>Smarter decisions.</h2>
        <p>
            Explore environmental data through interactive
            visualisations and meaningful insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="info-panel">
        <div class="section-label">PROJECT STATUS</div>
        <h3>Development preview</h3>
        <p>
            This version uses illustrative sample data.
            Actual team datasets and prediction models will
            be integrated as they become available.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

st.page_link(
    "pages/overview.py",
    label="OPEN AIR QUALITY OVERVIEW →",
    icon="🌍",
    use_container_width=True
)

st.markdown("""
<div class="footer">
    AEROSENSE AI &nbsp; · &nbsp; AIR QUALITY & WEATHER INTELLIGENCE
</div>
""", unsafe_allow_html=True)
