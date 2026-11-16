import pandas as pd


def get_city_statistics(df):
    return df.groupby("city")["aqi"].agg(
        ["count", "mean", "median", "min", "max"]
    ).round(2)


def get_aqi_correlation(df):
    features = [
        "aqi", "pm2_5", "pm10", "no2", "so2", "co",
        "o3", "dust", "temperature", "humidity",
        "wind_speed", "rain"
    ]
    return df[features].corr()["aqi"].sort_values(
        ascending=False
    ).round(3)


def get_feature_importance(model):
    importance = pd.DataFrame({
        "Feature": model.feature_names_in_,
        "Importance": model.feature_importances_
    })
    return importance.sort_values(
        by="Importance", ascending=False
    )


def get_seasonal_aqi(df):
    return df.groupby(
        ["city", "season"], observed=True
    )["aqi"].mean().unstack().round(2)


def get_monthly_aqi(df):
    return df.groupby(
        ["city", "month"]
    )["aqi"].mean().unstack().round(2)


def get_monthly_counts(df):
    return df.groupby(
        ["city", "month"]
    )["aqi"].count().unstack().fillna(0).astype(int)
