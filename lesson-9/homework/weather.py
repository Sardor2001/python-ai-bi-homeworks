import requests


def get_weather_data(city):
    api_key = "6db85f628018a8605b6c2ab282319754"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract relevant information
        city_name = data.get("name")
        country = data["sys"].get("country")
        temperature = data["main"].get("temp")
        humidity = data["main"].get("humidity")
        weather_description = data["weather"][0].get("description")

        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Unexpected data format: Missing key {e}")


if __name__ == "__main__":
    city = "Tashkent"  # Replace with your desired city
    get_weather_data(city)
