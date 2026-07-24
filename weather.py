import requests
import streamlit as st

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    return response.json(), response.status_code


def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    return response.json(), response.status_code
