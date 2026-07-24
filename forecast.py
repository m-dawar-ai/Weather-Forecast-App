from weather import get_forecast

def show_forecast(city):

    data, status = get_forecast(city)

    if status != 200:
        print("❌", data.get("message", "Unknown error"))
        return

    print("\n========== 5-DAY WEATHER FORECAST ==========\n")

    count = 0

    for item in data["list"]:

        # Show one forecast every 24 hours (8 x 3-hour intervals)
        if count % 8 == 0:

            print("📅", item["dt_txt"])
            print("🌡 Temp:", item["main"]["temp"], "°C")
            print("☁ Weather:", item["weather"][0]["description"].title())
            print("💧 Humidity:", item["main"]["humidity"], "%")
            print("🌬 Wind:", item["wind"]["speed"], "m/s")
            print("-" * 40)

        count += 1