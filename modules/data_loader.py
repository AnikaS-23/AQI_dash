
from datasets import load_dataset


def load_air_quality_data():
    print("Loading air quality dataset...")

    dataset = load_dataset(
        "ixrbhii/india-aqi-hourly-cams"
    )

    df = dataset["train"].to_pandas()

    print("Dataset loaded successfully!")
    print("Total records:", len(df))

    return df


import os
import pandas as pd


def load_processed_data(use_sample=False):

    if use_sample:
        file_path = "data/processed/airscope_sample.csv"
    else:
        file_path = "data/processed/airscope_cleaned.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    print("Loading processed dataset...")

    df = pd.read_csv(file_path)

    df["time"] = pd.to_datetime(df["time"])

    print("Dataset loaded!")
    print("Shape:", df.shape)

    return df

