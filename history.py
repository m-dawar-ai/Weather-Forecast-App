from datetime import datetime
import os

def save_history(city, temperature, weather):
    with open("weather_history.txt", "a") as file:
        file.write(
            f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} | "
            f"{city} | {temperature}°C | {weather}\n"
        )

def view_history():
    if os.path.exists("weather_history.txt"):
        with open("weather_history.txt", "r") as file:
            print("\n===== SEARCH HISTORY =====")
            print(file.read())
    else:
        print("No history found.")

def clear_history():
    open("weather_history.txt", "w").close()
    print("✅ Search history cleared.")