
import pandas as pd


def clean_air_quality_data(df):

    print("Cleaning dataset...")

    df = df.copy()

    # 1. Remove extra spaces from text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
        df[col] = df[col].replace("", pd.NA)

    # 2. Convert time column
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # 3. Convert measurement columns to numeric
    numeric_cols = [
        "lat", "lon", "aqi", "pm2_5", "pm10",
        "no2", "so2", "co", "o3", "dust",
        "temperature", "humidity", "wind_speed", "rain"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 4. Identify cities using latitude
    df["city"] = "Unknown"
    df.loc[df["lat"] < 20, "city"] = "Bengaluru"
    df.loc[df["lat"] > 20, "city"] = "Delhi"

    print("Cleaning completed!")
    print("City distribution:")
    print(df["city"].value_counts())

    return df
