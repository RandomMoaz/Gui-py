import tkinter as tk
import requests


def search_weather():
    location = location_input.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    temperature_label.config(text=weather_data["main"]["temp"])
    humidity_label.config(text=weather_data["main"]["humidity"])
    wind_speed_label.config(text=weather_data["wind"]["speed"])
    pressure_label.config(text=weather_data["main"]["pressure"])
    precipitation_label.config(text=weather_data["weather"][0]["description"])


# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create the GUI elements
location_label = tk.Label(window, text="Location:")
location_label.pack()

location_input = tk.Entry(window, width=40)
location_input.pack()

search_button = tk.Button(window, text="Search", command=search_weather, width=40)
search_button.pack()

temperature_label = tk.Label(window, text="Temperature")
temperature_label.pack()

humidity_label = tk.Label(window, text="Humidity")
humidity_label.pack()

wind_speed_label = tk.Label(window, text="Wind Speed")
wind_speed_label.pack()

pressure_label = tk.Label(window, text="Pressure")
pressure_label.pack()

precipitation_label = tk.Label(window, text="Precipitation")
precipitation_label.pack()

# Start the main loop
window.mainloop()
