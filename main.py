from weather import get_weather
from forecast import show_forecast
from utils import current_date, current_time
from history import save_history, view_history, clear_history
from menu import show_menu
from datetime import datetime

while True:

    show_menu()

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":

        city = input("\nEnter city name: ").strip()

        if city == "":
            print("⚠ Please enter a city name.")
            continue

        data, status = get_weather(city)

        if status == 200:

            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.fromtimestamp(data["sys"]["sunset"])

            print("\n" + "=" * 45)
            print("📍 City:", data["name"])
            print("🌍 Country:", data["sys"]["country"])
            print("📅 Date:", current_date())
            print("🕒 Time:", current_time())
            print("🌡 Temperature:", data["main"]["temp"], "°C")
            print("🌡 Max Temp:", data["main"]["temp_max"], "°C")
            print("🌡 Min Temp:", data["main"]["temp_min"], "°C")
            print("🤒 Feels Like:", data["main"]["feels_like"], "°C")
            print("💧 Humidity:", data["main"]["humidity"], "%")
            print("🌬 Wind Speed:", data["wind"]["speed"], "m/s")
            print("🔽 Pressure:", data["main"]["pressure"], "hPa")
            print("☁ Clouds:", data["clouds"]["all"], "%")
            print("👁 Visibility:", data["visibility"] / 1000, "km")
            print("☁ Weather:", data["weather"][0]["description"].title())
            print("🌅 Sunrise:", sunrise.strftime("%I:%M %p"))
            print("🌇 Sunset :", sunset.strftime("%I:%M %p"))
            print("=" * 45)

            save_history(
                data["name"],
                data["main"]["temp"],
                data["weather"][0]["description"].title()
            )

        else:
            print("❌", data.get("message", "Unknown error"))

    elif choice == "2":

        city = input("\nEnter city name: ").strip()

        if city == "":
            print("⚠ Please enter a city name.")
            continue

        show_forecast(city)

    elif choice == "3":
        view_history()

    elif choice == "4":
        confirm = input("Are you sure you want to clear history? (y/n): ").lower()

        if confirm == "y":
            clear_history()
        else:
            print("History not cleared.")

    elif choice == "5":
        print("\n👋 Thank you for using Weather Forecast App!")
        break

    else:
        print("❌ Invalid option. Please choose 1-5.")