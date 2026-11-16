import streamlit as st
import pandas as pd

from modules.predictions import predict_next_hour, load_model


def render_ml_prediction(current_aqi, timestamp, get_aqi_category,
                         get_advisory):

    st.divider()

    st.markdown(
        """
        <div style="margin-bottom:15px;">
            <div style="color:#9ACBA3;font-size:11px;
                        font-weight:700;letter-spacing:2px;">
                ML / RANDOM FOREST MODEL
            </div>
            <h2 style="color:#EDF5EF;">
                Next-Hour AQI Prediction
            </h2>
            <p style="color:#91A397;font-size:13px;">
                Machine learning prediction using current AQI
                and weather conditions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Enter the weather conditions to estimate AQI "
        "for the next hour using our trained Random Forest model."
    )

    # WEATHER INPUTS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-20.0,
            max_value=60.0,
            value=28.0,
            step=0.5
        )

    with col2:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=60.0,
            step=1.0
        )

    with col3:
        wind_speed = st.number_input(
            "Wind speed",
            min_value=0.0,
            value=5.0,
            step=0.5
        )

    with col4:
        rain = st.number_input(
            "Rain",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

    st.caption(
        "Weather values should use the same units and "
        "measurement conventions as the training dataset."
    )

    # PREDICTION

    if st.button(
        "Predict Next-Hour AQI",
        key="random_forest_predict",
        use_container_width=True
    ):

        try:

            with st.spinner("Running Random Forest prediction..."):

                prediction = predict_next_hour(
                    aqi=float(current_aqi),
                    temperature=float(temperature),
                    humidity=float(humidity),
                    wind_speed=float(wind_speed),
                    rain=float(rain),
                    hour=int(timestamp.hour),
                    month=int(timestamp.month)
                )

            category, css_class = get_aqi_category(prediction)

            st.session_state["ml_prediction"] = prediction
            st.session_state["ml_category"] = category
            st.session_state["ml_css_class"] = css_class

        except Exception as error:

            st.error(
                f"Prediction failed: {error}"
            )

    # DISPLAY RESULT

    if "ml_prediction" in st.session_state:

        prediction = st.session_state["ml_prediction"]
        category = st.session_state["ml_category"]
        css_class = st.session_state["ml_css_class"]

        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-caption">
                    RANDOM FOREST NEXT-HOUR PREDICTION
                </div>

                <div style="font-size:46px;
                            font-weight:800;
                            color:#8CCF9B;
                            font-family:Manrope;">
                    {prediction:.2f}
                </div>

                <span class="status-pill {css_class}">
                    {category}
                </span>

                <p style="color:#C0CEC3;
                          font-size:14px;
                          line-height:1.8;
                          margin-top:18px;">
                    {get_advisory(prediction)}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # MODEL PERFORMANCE

    st.divider()

    st.markdown(
        """
        <div class="section-label">
            MODEL PERFORMANCE / EVALUATION
        </div>
        """,
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)

    m1.metric("MAE", "3.13")
    m2.metric("RMSE", "5.39")
    m3.metric("R² Score", "0.9976")

    st.caption(
        "Test-set evaluation: 128,198 observations. "
        "Persistence baseline MAE: 6.16. "
        "Lower MAE and RMSE indicate better prediction accuracy."
    )

    # FEATURE IMPORTANCE

    with st.expander("Explore model feature importance"):

        try:

            model = load_model()

            importance = pd.DataFrame({
                "Feature": model.feature_names_in_,
                "Importance": model.feature_importances_
            })

            importance = importance.sort_values(
                "Importance",
                ascending=False
            )

            st.bar_chart(
                importance.set_index("Feature"),
                horizontal=True
            )

            st.dataframe(
                importance.round(4),
                use_container_width=True,
                hide_index=True
            )

            st.caption(
                "Feature importance indicates how the model uses "
                "input variables for prediction. It does not establish "
                "causation."
            )

        except Exception as error:

            st.error(
                f"Feature importance unavailable: {error}"
            )

    # METHODOLOGY

    with st.expander("About the Random Forest model"):

        st.markdown(
            """
            **Algorithm:** Random Forest Regressor

            **Prediction target:** AQI one hour ahead.

            **Input features:**
            - Current AQI
            - Temperature
            - Humidity
            - Wind speed
            - Rainfall
            - Hour
            - Month

            **Training methodology:**
            - Chronological 80:20 train-test split.
            - Time ordering preserved within each monitoring station.
            - Next-hour target generated using consecutive hourly readings.

            **Important:** The Random Forest produces a next-hour
            estimate. It does not generate the separate 24-hour
            statistical baseline forecast displayed above.
            """
        )
