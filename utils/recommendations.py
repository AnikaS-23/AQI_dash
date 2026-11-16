
def get_health_recommendation(aqi):
    if aqi is None:
        return {
            "category": "Unavailable",
            "message": "AQI data is currently unavailable.",
            "advice": ["Please check again later."]
        }

    if aqi <= 50:
        return {
            "category": "Good",
            "message": "Air quality is satisfactory.",
            "advice": [
                "Enjoy your usual outdoor activities.",
                "Continue following local air-quality updates."
            ]
        }

    elif aqi <= 100:
        return {
            "category": "Moderate",
            "message": "Air quality is acceptable for most people.",
            "advice": [
                "Unusually sensitive individuals should monitor symptoms.",
                "Take breaks if outdoor air causes discomfort."
            ]
        }

    elif aqi <= 150:
        return {
            "category": "Unhealthy for Sensitive Groups",
            "message": "Sensitive groups may experience health effects.",
            "advice": [
                "Children and people with respiratory conditions should consider reducing prolonged outdoor exertion.",
                "Monitor local air-quality updates."
            ]
        }

    elif aqi <= 200:
        return {
            "category": "Unhealthy",
            "message": "Some people may experience health effects.",
            "advice": [
                "Consider reducing prolonged outdoor exertion.",
                "Sensitive groups should take extra precautions."
            ]
        }

    elif aqi <= 300:
        return {
            "category": "Very Unhealthy",
            "message": "Health alert: increased risk of health effects.",
            "advice": [
                "Avoid prolonged outdoor exertion.",
                "Keep indoor spaces as clean-air as possible."
            ]
        }

    else:
        return {
            "category": "Hazardous",
            "message": "Health warning: everyone may experience health effects.",
            "advice": [
                "Avoid outdoor exertion.",
                "Follow local public-health guidance."
            ]
        }
