import joblib
import pandas as pd
from pathlib import Path
from functools import lru_cache

# Model stored inside modules folder
MODEL_PATH = (
    Path(__file__).resolve().parent
    / "aqi_random_forest_small.pkl"
)

FEATURES = [
    "aqi",
    "temperature",
    "humidity",
    "wind_speed",
    "rain",
    "hour",
    "month"
]


@lru_cache(maxsize=1)
def load_model():
    return joblib.load(MODEL_PATH)


def predict_next_hour(aqi, temperature, humidity,
                      wind_speed, rain, hour, month):

    input_data = pd.DataFrame([{
        "aqi": aqi,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "rain": rain,
        "hour": hour,
        "month": month
    }], columns=FEATURES)

    prediction = load_model().predict(input_data)[0]

    return round(float(prediction), 2)
