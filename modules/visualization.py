import plotly.express as px


def make_aqi_chart(df, station_name="Bengaluru"):
    """Create a colorful AQI trend chart."""
    chart = px.line(
        df.sort_values("time"),
        x="time",
        y="aqi",
        title=f"🌈 AQI Trend — {station_name}",
        labels={"time": "Date and time", "aqi": "AQI"},
        color_discrete_sequence=["#7c3aed"],
    )
    chart.update_traces(line=dict(width=3))
    chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_color="#312e81",
        hovermode="x unified",
    )
    return chart


def make_weather_chart(df, column, station_name="Bengaluru"):
    """Create a colorful chart for one weather measurement."""
    colors = {
        "temperature": "#f97316",
        "humidity": "#06b6d4",
        "wind_speed": "#22c55e",
        "rain": "#3b82f6",
    }
    labels = {
        "temperature": "Temperature (°C)",
        "humidity": "Humidity (%)",
        "wind_speed": "Wind speed (km/h)",
        "rain": "Rain (mm)",
    }

    chart = px.line(
        df.sort_values("time"),
        x="time",
        y=column,
        title=f"🌤️ {labels.get(column, column.title())} — {station_name}",
        labels={
            "time": "Date and time",
            column: labels.get(column, column.title()),
        },
        color_discrete_sequence=[colors.get(column, "#8b5cf6")],
    )
    chart.update_traces(line=dict(width=3))
    chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_color="#312e81",
        hovermode="x unified",
    )
    return chart