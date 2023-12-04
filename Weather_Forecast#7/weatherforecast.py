import requests
import tkinter as tk
from tkinter import messagebox

#getting forecast of location user input
def get_location_weather():
    #api key
    api_key = "76019c3bbbc0e38984ae20082004674e"

    #What will happen when search button is clicked
    def validate_input():
        #getting location from input text field and insuring it is valid
        location = location_textfield.get()
        isValidInput = location.isalpha()
        print(f"isValidInput: {isValidInput}")
        if not isValidInput:
            messagebox.showerror("Error", "Failed to retrieve weather data for the location")
        else:
            #extracting lon and lat from the location as given in city,country name
            url_1 = (f"http://api.openweathermap.org/geo/1.0/direct?q="
                     f"{location}"
                     f"&limit=1"
                    f"&appid={api_key}"
                    )
            res = requests.get(url_1)
            print (f"resss status code::::{res.json()}")              #Testing
            response_1 = res.json()
            lat = response_1[0]["lat"]
            lon = response_1[0]["lon"]
            print(f"lat: {lat} ....... lon: {lon}")    #testing 

            #getting weather data using lon and lat
            url_2 = (f"https://api.openweathermap.org/data/2.5/weather?lat="
                     f"{lat}"
                     f"&lon={lon}"
                     f"&units=metric"   #Units in si
                     f"&appid={api_key}"
                     )
            response_2 = (requests.get(url_2)).json()
            print (response_2)                          #testing
            temp = response_2["main"]["temp"]               #Temperature in celsius
            wind_speed = (response_2["wind"]["speed"])*3.6          #wind speed in Km/h
            pressure = response_2["main"]["pressure"]                    #Pressure in hPa
            humidity = response_2["main"]["humidity"]                            #humidity in %

            #Testing
            print (f"Temperature: {temp} celsius"
                   f"Wind Speed: {wind_speed} Km/h"
                   f"Pressure: {pressure} hPa"
                   f"Humidity: {humidity} %"
                   )

            #Checking from rain field before throwing precipitation to the label
            if "rain" in response_2 and "1h" in response_2["rain"]:
                precipitation = response_2["rain"].get("1h",0)
                avr_max_precipitation_mm = 12.5     #An average of maximum possible precipitation to calculate the percentage
                precipitation_percentage = (precipitation/avr_max_precipitation_mm)*100
                #updating label text
                precipitation_label.config(text = f"Precipitation: {precipitation_percentage}%")
            else:
                precipitation_label.config(text = "Precipitation: 0.0%")

            #throw collected weather data to it's labels
            temperature_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_speed_label.config(text=f"Wind Speed: {wind_speed}Km/s")
            pressure_label.config(text=f"Pressure: {pressure}hPa")

    validate_input()

#Creating & Editing window
window = tk.Tk()
window.title("Beta Weather Forecast__Dark theme .^_^.")
window.configure(bg = "#1b1b1b")

#creating btns , labels , text input field
search_btn = tk.Button(window
                       ,text = "Search",
                       command = get_location_weather
                       ,fg = "#999999" ,bg = "#353535"
                       )
location_textfield = tk.Entry(window
                             ,bg = "#2d2d2d" ,fg = "#f3f6f4"
                             ,font = "regular"
                             ,width = 20
                             )
location_label = tk.Label(window
                          ,text="Location:"
                          ,fg = "#f3f6f4" ,bg = "#1b1b1b",
                          font = ("italic",18)
                          )
temperature_label = tk.Label(window
                             ,text = "Temperature:"
                             ,fg = "#f3f6f4" ,bg = "#1b1b1b",
                             font = ("italic",18)
                             )
humidity_label = tk.Label(window
                          ,text = "Humidity:"
                          ,fg = "#f3f6f4" ,bg = "#1b1b1b",
                          font = ("italic",18)
                          )
wind_speed_label = tk.Label(window
                            ,text = "Wind Speed:",
                            fg = "#f3f6f4" ,bg = "#1b1b1b",
                            font = ("italic",18)
                            )
pressure_label = tk.Label(window
                          ,text = "Pressure:"
                          ,fg = "#f3f6f4" ,bg = "#1b1b1b",
                          font = ("italic",18)
                          )
precipitation_label = tk.Label(window
                               ,text = "Precipitation:"
                               ,fg = "#f3f6f4" ,bg = "#1b1b1b",
                               font = ("italic",18)
                               )



#Positioning
search_btn.grid(column = 1 ,row = 0 ,padx = 50 ,pady = 17.3 ,sticky = "ne")
location_textfield.grid(column = 0 ,row = 0 ,pady = 18.45 ,sticky = "ne")
location_label.grid(column = 0 ,row = 0 ,padx = 200, pady = 13, sticky="ne")
temperature_label.grid(column = 0 ,row = 1 ,padx = 50 ,pady = 20 ,sticky = "w")
humidity_label.grid(column = 0 ,row = 2 ,padx = 60 ,pady = 20 ,sticky = "w")
wind_speed_label.grid(column = 0 ,row = 3 ,padx = 50 ,pady = 20 ,sticky = "w")
pressure_label.grid(column = 0 ,row = 4 ,padx = 60 ,pady = 20 ,sticky = "w")
precipitation_label.grid(column = 0 ,row = 5 ,padx = 50 ,pady = 20 ,sticky = "w")

window.mainloop()
