
import pandas as pd


def get_health_recommendation(aqi):

    if pd.isna(aqi):
        return {
            "category": "Unavailable",
            "recommendation": "AQI data is unavailable. Please check again later."
        }

    if aqi < 0:
        return {
            "category": "Invalid",
            "recommendation": "Invalid AQI value."
        }

    if aqi <= 50:
        category = "Good"
        advice = "Air quality is good. Enjoy normal outdoor activities."

    elif aqi <= 100:
        category = "Satisfactory"
        advice = "Minor breathing discomfort may occur in sensitive individuals. Most people can continue normal activities."

    elif aqi <= 200:
        category = "Moderate"
        advice = "People with asthma or other respiratory conditions should limit prolonged outdoor exertion if they experience symptoms."

    elif aqi <= 300:
        category = "Poor"
        advice = "Reduce prolonged outdoor exertion. Sensitive individuals should take extra care and follow medical advice."

    elif aqi <= 400:
        category = "Very Poor"
        advice = "Avoid prolonged or strenuous outdoor activities. Sensitive groups should stay indoors when possible."

    else:
        category = "Severe"
        advice = "Avoid outdoor exertion as much as possible. Follow local health advisories and seek medical guidance if you feel unwell."

    return {
        "category": category,
        "recommendation": advice
    }
