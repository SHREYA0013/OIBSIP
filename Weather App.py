<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:04:00 2023

@author: shreya
"""

#we are going to get the weather of a city using OpenWeatherMap API. We need the weather API key which we can get by logging into our account.

import json
import requests # import required modules

Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
City = input("Type the name of the city: ")
API_key = "7b67198854557491df089e4fcd4b3fc1" # Enter your API key here

URL = Base_URL + "q=" + City + "&appid=" + API_key # complete url address

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature_kelvin = main['temp']
    humidity = main['humidity']
    wind = data['wind']
    wind_speed = wind['speed']
    pressure = main['pressure']
    
    #convert the temperature into celsius:
    temperature_celsius= temperature_kelvin-273.15

    print(f"{City:-^30}")
    print(f"Temperature: {temperature_kelvin}")
    print(f"Celsius Temperature: {temperature_celsius:.2f} °C")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_speed}")
    print(f"Pressure: {pressure}")
else:
    print("Can't access.")
    
    
print("\nHave a nice day!")





#Let's modify the code now:
    
    
    
from tkinter import *
import requests
import json
from datetime import datetime #importing necessary modules

#initialize window
root=Tk()
root.geometry("800x800") #this is the default size of the window
root.resizable(0,0) #make the size fixed
root.title("Weather Details App")

City=StringVar()


def Weather_Details():
    API_key="7b67198854557491df089e4fcd4b3fc1"
    City_name= City.get()
    
    Weather_URL = "https://api.openweathermap.org/data/2.5/weather?q=" + City_name + "&appid=" + API_key
    
    response= requests.get(Weather_URL)
    weather_info=response.json()
    
    tfield.delete("1.0","end") #to clear the text field for new output
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod']==200:
        kelvin=273
        
        temp=int(weather_info['main']['temp']-kelvin)
        feels_like_temp=int(weather_info['main']['feels_like']-kelvin)
        pressure=weather_info['main']['pressure']
        humidity=weather_info['main']['humidity']
        wind_speed=weather_info['wind']['speed']*3.6
        cloudy=weather_info['clouds']['all']
        sunrise=weather_info['sys']['sunrise']
        sunset=weather_info['sys']['sunset']
        timezone=weather_info['timezone']
        description=weather_info['weather'][0]['description']
        
        sunrise_time=time_format_for_location(sunrise+timezone)
        sunset_time=time_format_for_location(sunset+timezone)

        Weather = f"\nCurrent Weather of: {City_name}\nTemperature(Celsius): {temp}°\nFeels like(Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed}\nSunrise time: {sunrise_time}\nSunset time: {sunset_time}\nCloud: {cloudy}%\nTime zone:{timezone}\nOverall Information: {description}"
    else:
        Weather = f"\nSorry\tWeather for '{City_name}' not found!\n\tPlease Enter a valid City Name !!"
   
    tfield.insert(INSERT,Weather)
    print("\n\tHave a nice day!") 
#function checks for the local time as compared to the UTC(Universal Time Coordinated) in which the API gives the output to the time format as per our location. Ex. UTC to IST.   
def time_format_for_location(timestamp):
    local_time= datetime.utcfromtimestamp(timestamp)
    return local_time.time()

#Graphical User Interfact
City_head=Label(root,text='Hello!\nEnter the name of the City:',font='Cambria 18 italic').pack(pady=10)
inp_City=Entry(root,textvariable= City, width=20,font='Arial 14 bold').pack()

#Adding buttons as per our choice
Button(root,command=Weather_Details, text="Weather Details",font="Cambria 12 bold",bg='teal',activebackground="pink",padx=5,pady=5).pack(pady=15)

Weather_now=Label(root,text="The current weather details: ",font='Arial 16 bold').pack(pady=10)
tfield=Text(root,width=60,height=15,font='Arial 14 bold')
tfield.pack()

root.mainloop()














=======
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:04:00 2023

@author: shreya
"""

#we are going to get the weather of a city using OpenWeatherMap API. We need the weather API key which we can get by logging into our account.

import json
import requests # import required modules

Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
City = input("Type the name of the city: ")
API_key = "7b67198854557491df089e4fcd4b3fc1" # Enter your API key here

URL = Base_URL + "q=" + City + "&appid=" + API_key # complete url address

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature_kelvin = main['temp']
    humidity = main['humidity']
    wind = data['wind']
    wind_speed = wind['speed']
    pressure = main['pressure']
    
    #convert the temperature into celsius:
    temperature_celsius= temperature_kelvin-273.15

    print(f"{City:-^30}")
    print(f"Temperature: {temperature_kelvin}")
    print(f"Celsius Temperature: {temperature_celsius:.2f} °C")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_speed}")
    print(f"Pressure: {pressure}")
else:
    print("Can't access.")
    
    
print("\nHave a nice day!")





#Let's modify the code now:
    
    
    
from tkinter import *
import requests
import json
from datetime import datetime #importing necessary modules

#initialize window
root=Tk()
root.geometry("800x800") #this is the default size of the window
root.resizable(0,0) #make the size fixed
root.title("Weather Details App")

City=StringVar()


def Weather_Details():
    API_key="7b67198854557491df089e4fcd4b3fc1"
    City_name= City.get()
    
    Weather_URL = "https://api.openweathermap.org/data/2.5/weather?q=" + City_name + "&appid=" + API_key
    
    response= requests.get(Weather_URL)
    weather_info=response.json()
    
    tfield.delete("1.0","end") #to clear the text field for new output
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod']==200:
        kelvin=273
        
        temp=int(weather_info['main']['temp']-kelvin)
        feels_like_temp=int(weather_info['main']['feels_like']-kelvin)
        pressure=weather_info['main']['pressure']
        humidity=weather_info['main']['humidity']
        wind_speed=weather_info['wind']['speed']*3.6
        cloudy=weather_info['clouds']['all']
        sunrise=weather_info['sys']['sunrise']
        sunset=weather_info['sys']['sunset']
        timezone=weather_info['timezone']
        description=weather_info['weather'][0]['description']
        
        sunrise_time=time_format_for_location(sunrise+timezone)
        sunset_time=time_format_for_location(sunset+timezone)

        Weather = f"\nCurrent Weather of: {City_name}\nTemperature(Celsius): {temp}°\nFeels like(Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed}\nSunrise time: {sunrise_time}\nSunset time: {sunset_time}\nCloud: {cloudy}%\nTime zone:{timezone}\nOverall Information: {description}"
    else:
        Weather = f"\nSorry\tWeather for '{City_name}' not found!\n\tPlease Enter a valid City Name !!"
   
    tfield.insert(INSERT,Weather)
    print("\n\tHave a nice day!") 
#function checks for the local time as compared to the UTC(Universal Time Coordinated) in which the API gives the output to the time format as per our location. Ex. UTC to IST.   
def time_format_for_location(timestamp):
    local_time= datetime.utcfromtimestamp(timestamp)
    return local_time.time()

#Graphical User Interfact
City_head=Label(root,text='Hello!\nEnter the name of the City:',font='Cambria 18 italic').pack(pady=10)
inp_City=Entry(root,textvariable= City, width=20,font='Arial 14 bold').pack()

#Adding buttons as per our choice
Button(root,command=Weather_details, text="Weather Details",font="Cambria 12 bold",bg='teal',activebackground="pink",padx=5,pady=5).pack(pady=15)

Weather_now=Label(root,text="The current weather details: ",font='Arial 16 bold').pack(pady=10)
tfield=Text(root,width=60,height=15,font='Arial 14 bold')
tfield.pack()

root.mainloop()














>>>>>>> 112fc8c4dd908cf213b413f494ebe4d96c81586d
