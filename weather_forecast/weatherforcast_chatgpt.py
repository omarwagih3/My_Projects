import requests
import tkinter as tk
from tkinter import messagebox

# Function to retrieve weather data for the entered location
def get_location_weather():
    # API key
    api_key = "76019c3bbbc0e38984ae20082004674e"  # Replace with your actual API key

    # Get the user-entered location from the text field
    location = location_textfield.get()

    # API request to fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant weather information from the response
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        pressure = weather_data["main"]["pressure"]

        # Update the labels with the retrieved weather data
        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
    else:
        # Display an error message if the request fails
        messagebox.showerror("Error", "Failed to retrieve weather data for the location")

# Create the main window
window = tk.Tk()
window.title("Weather Forecast")

# Create and position the UI elements (buttons, labels, text input field)

# Create and position the UI elements (buttons, labels, text input field)
search_btn = tk.Button(window, text="Search", command=get_location_weather)
search_btn.grid(column=1, row=0, padx=50, pady=17.3, sticky="ne")

location_textfield = tk.Entry(window, width=20)
location_textfield.grid(column=0, row=0, pady=18.45, sticky="ne")

location_label = tk.Label(window, text="Location:",font=(18))
location_label.grid(column=0, row=0, padx=200, pady=13, sticky="ne")

temperature_label = tk.Label(window, text="Temperature:",font=(18))
temperature_label.grid(column=0, row=1, padx=50, pady=20, sticky="w")

humidity_label = tk.Label(window, text="Humidity:",font=(18))
humidity_label.grid(column=0, row=2, padx=60, pady=20, sticky="w")

wind_speed_label = tk.Label(window, text="Wind Speed:",font=(18))
wind_speed_label.grid(column=0, row=3, padx=50, pady=20, sticky="w")

pressure_label = tk.Label(window, text="Pressure:",font=(18))
pressure_label.grid(column=0, row=4, padx=60, pady=20, sticky="w")

# Run the main event loop
window.mainloop()
