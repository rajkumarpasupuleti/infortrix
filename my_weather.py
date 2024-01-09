import requests
import time
import math
import random


class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data"
        self.favorite_cities = []
        self.refresh_interval = 30  # seconds

    def get_weather(self, city):
        url = f"https://api.weatherapi.com/v1/current.json?key=fc534c7dda06456e87275059240201&q={city}&aqi=no"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    def display_weather(self, data):
        if data:
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind=data['current']['wind_kph']
            condition = data['current']['condition']['text']
            print(f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind: {wind}Km/h \nCondition: {condition} \nlocaltime: {data['location']['localtime']}")
        else:
            print("Weather data not available.")

    def add_to_favorites(self, city):
        if city not in self.favorite_cities:
            self.favorite_cities.append(city)
            print(f"{city} added to favorites.")
        else:
            print(f"{city} is already in favorites.")


    def remove_from_favorites(self, city):
        if city in self.favorite_cities:
            self.favorite_cities.remove(city)
            print(f"{city} removed from favorites.")
        else:
            print(f"{city} is not in favorites.")

    def show_favorites(self):
        if self.favorite_cities:
            print("Favorite Cities:")
            for city in self.favorite_cities:
                print(f"- {city}")
            city_1 = input("Enter your favorite city from above list: ")
            weather_data_f=weather_app.get_weather(city_1)
            weather_app.display_weather(weather_data_f)
        else:
            print("No favorite cities yet.")

    def auto_refresh(self):
        while True:
            print("\nAuto Refreshing...")
            for city in self.favorite_cities:
                weather_data = self.get_weather(city)
                print(f"Weather in {city}: ", end="")
                self.display_weather(weather_data)
            refresh_interval = random.randint(15, 30)
            print(f"Next refresh in {refresh_interval} seconds...")
            time.sleep(refresh_interval)

if __name__ == "__main__":
    api_key="fc534c7dda06456e87275059240201"
    weather_app = WeatherApp(api_key)

    while True:
        print("\nWeather Checking Application:")
        print("1. Check Weather by City")
        print("2. Add City to Favorites")
        print("3. Remove City from Favorites")
        print("4. Show Favorite Cities")
        print("5. Auto Refresh Favorites")
        print("0. Exit")

        choice = input("Enter your choice: ")


        if choice == "1":
            city = input("Enter city name: ")
            weather_data = weather_app.get_weather(city)

            if weather_data is not None and 'error' in weather_data:
                print(f"Error: {weather_data['error']['code']} - {weather_data['error']['message']}")
            else:
                weather_app.display_weather(weather_data)


        elif choice == "2":
            city = input("Enter city name: ")
            weather_app.add_to_favorites(city)
        elif choice == "3":
            city = input("Enter city name: ")
            weather_app.remove_from_favorites(city)
        elif choice == "4":
            weather_app.show_favorites()
        elif choice == "5":
            weather_app.auto_refresh()
        elif choice == "0":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
