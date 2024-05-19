# Weather Forecast Application

## Description
The Weather Forecast application provides users with current weather data for a specified location. Users can input the name of the city, and the application retrieves weather information such as temperature, humidity, wind speed, pressure, and precipitation percentage.

## Features
- Retrieve current weather data based on user-input location.
- Display temperature, humidity, wind speed, pressure, and precipitation percentage.
- Dark-themed user interface for a modern look.

## Requirements
- Python 3.x
- `requests` library
- `tkinter` library

## How to Use
1. Run the script `weather_forecast.py`.
2. Enter the name of the location (city name) in the provided text field.
3. Click the "Search" button to retrieve weather data.
4. The application displays temperature, humidity, wind speed, pressure, and precipitation percentage for the specified location.
5. Exit the application when done.

## Implementation Details
- The application is implemented in Python using the `tkinter` library for the graphical user interface (GUI).
- Weather data is obtained from the OpenWeather API using the `requests` library.
- Users input the location (city name) to retrieve weather information.
- Error handling is implemented to handle invalid inputs and API request failures.
- The application provides feedback to users through labels displaying weather information.

## What I've Learned
- Working with APIs to fetch real-time data.
- Integrating graphical user interfaces using the `tkinter` library.
- Handling user inputs and validating data.
- Displaying dynamic content based on API responses.
- Designing and implementing a dark-themed user interface for improved aesthetics.

## Author
[Omar Wagih]
