import streamlit as st
import pandas as pd

from modules.predictions import predict_next_hour, load_model


def render_ml_prediction(
    current_aqi,
    timestamp,
    get_aqi_category,
    get_advisory
):

    st.divider()

    st.title("🤖 AI-Based AQI Prediction")

    st.write(
        "Predict the Air Quality Index for the next hour "
        "using our trained Random Forest Machine Learning model."
    )

    st.info(
        "The model uses the current AQI and weather conditions "
        "to estimate the next-hour AQI."
    )

    # --------------------------------------------------
    # CURRENT CONDITIONS
    # --------------------------------------------------

    st.subheader("Current Air Quality")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Current AQI",
            value=f"{float(current_aqi):.2f}"
        )

    with col2:
        st.write("**Latest Reading**")
        st.write(str(timestamp))

    st.divider()

    # --------------------------------------------------
    # WEATHER INPUTS
    # --------------------------------------------------

    st.subheader("Weather Conditions")

    st.write(
        "Enter the current weather conditions to generate "
        "the next-hour prediction."
    )

    col1, col2 = st.columns(2)

    with col1:
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-10.0,
            max_value=60.0,
            value=28.0,
            step=0.5
        )

        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=60.0,
            step=1.0
        )

        wind_speed = st.number_input(
            "Wind Speed",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.5
        )

    with col2:
        rain = st.number_input(
            "Rain",
            min_value=0.0,
            max_value=500.0,
            value=0.0,
            step=0.5
        )

        prediction_time = pd.to_datetime(timestamp)

        hour = prediction_time.hour
        month = prediction_time.month

        st.metric(
            "Current Hour",
            f"{hour}:00"
        )

        st.metric(
            "Current Month",
            month
        )

    st.caption(
        "Hour and month are automatically taken from the latest "
        "available AQI reading."
    )

    st.divider()

    # --------------------------------------------------
    # PREDICTION BUTTON
    # --------------------------------------------------

    if st.button(
        "🔮 Predict Next Hour AQI",
        use_container_width=True
    ):

        try:
            prediction = predict_next_hour(
                aqi=float(current_aqi),
                temperature=float(temperature),
                humidity=float(humidity),
                wind_speed=float(wind_speed),
                rain=float(rain),
                hour=int(hour),
                month=int(month)
            )

            category_result = get_aqi_category(prediction)

            # Supports both tuple and string category functions
            if isinstance(category_result, tuple):
                category = category_result[0]
            else:
                category = category_result

            advisory = get_advisory(prediction)

            st.session_state["ml_prediction"] = prediction
            st.session_state["ml_category"] = category
            st.session_state["ml_advisory"] = advisory

            st.session_state["ml_inputs"] = {
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "rain": rain
            }

        except Exception as e:
            st.error(f"Prediction failed: {e}")

    # --------------------------------------------------
    # DISPLAY PREDICTION RESULT
    # --------------------------------------------------

    if "ml_prediction" in st.session_state:

        prediction = st.session_state["ml_prediction"]
        category = st.session_state["ml_category"]
        advisory = st.session_state["ml_advisory"]

        st.divider()

        st.subheader("📊 Prediction Result")

        st.metric(
            label="Predicted AQI for Next Hour",
            value=f"{prediction:.2f}"
        )

        st.success(f"Predicted AQI Category: {category}")

        st.subheader("Health Advisory")

        st.info(advisory)

        st.caption(
            "This is a machine learning estimate for the next hour, "
            "not a live measured AQI reading."
        )

        # Compare current and predicted AQI
        difference = prediction - float(current_aqi)

        st.subheader("AQI Comparison")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Current AQI",
                f"{float(current_aqi):.2f}"
            )

        with col2:
            st.metric(
                "Predicted AQI",
                f"{prediction:.2f}"
            )

        with col3:
            st.metric(
                "AQI Change",
                f"{difference:+.2f}"
            )

    # --------------------------------------------------
    # MODEL INFORMATION
    # --------------------------------------------------

    st.divider()

    st.subheader("🧠 Machine Learning Model")

    st.write(
        "The prediction is generated using a trained "
        "Random Forest Regressor."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "Random Forest")

    with col2:
        st.metric("Test MAE", "3.13")

    with col3:
        st.metric("R² Score", "0.9976")

    st.write("**Model Performance**")

    st.write(
        "- Mean Absolute Error (MAE): 3.13"
    )

    st.write(
        "- Root Mean Squared Error (RMSE): 5.39"
    )

    st.write(
        "- R² Score: 0.9976"
    )

    st.write(
        "- Model Size: Approximately 3.42 MB"
    )

    st.write("**Input Features Used**")

    st.write(
        "AQI, Temperature, Humidity, Wind Speed, "
        "Rain, Hour and Month."
    )

    st.caption(
        "The model was evaluated using a chronological "
        "80:20 train-test split. Performance metrics are "
        "from the held-out test set."
    )
