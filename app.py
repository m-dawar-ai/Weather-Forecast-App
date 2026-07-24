import streamlit as st
from weather import get_weather, get_forecast

# Page configuration
st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌤️",
    layout="centered"
)

# Title
st.title("🌤️ Weather Forecast App")
st.write("Get current weather information and forecast using OpenWeather API")

# City input
city = st.text_input("Enter City Name", "Peshawar")

if st.button("Get Weather"):

    weather_data, weather_status = get_weather(city)

    if weather_status == 200:

        st.success(f"Weather in {city}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Temperature",
                f"{weather_data['main']['temp']} °C"
            )

            st.metric(
                "Feels Like",
                f"{weather_data['main']['feels_like']} °C"
            )

        with col2:
            st.metric(
                "Humidity",
                f"{weather_data['main']['humidity']}%"
            )

            st.metric(
                "Wind Speed",
                f"{weather_data['wind']['speed']} m/s"
            )

        st.subheader("Condition")
        st.write(
            weather_data["weather"][0]["description"].title()
        )


        # Forecast
        st.subheader("📅 Forecast")

        forecast_data, forecast_status = get_forecast(city)

        if forecast_status == 200:

            for item in forecast_data["list"][:5]:
                st.write(
                    f"""
                    **{item['dt_txt']}**
                    - Temperature: {item['main']['temp']} °C
                    - Condition: {item['weather'][0]['description'].title()}
                    """
                )

    else:
    st.error(
        f"Error: {weather_data.get('message', 'Unknown error')}"
    )
