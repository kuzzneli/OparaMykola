import tkinter as tk
import requests
from datetime import datetime
from WeatherApp import gg

def get_weather():
    api_key = "1d814739a97d4eb6998101237241006"
    city = city_entry.get()
    url = f"'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        temp = weather_data["main"]["temp"]
        desc = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]

        result_label.config(text=f"Температура: {temp}°C\nОпис: {desc}\nВологість: {humidity}%")
    else:
        result_label.config(text="Місто не знайдено")


# Створення головного вікна
root = tk.Tk()
root.title("Погода на сьогодні")
root.geometry("300x250")

# Створення і розміщення віджетів
title_label = tk.Label(root, text="Введіть назву міста:", font=("Arial", 14))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack()

search_button = tk.Button(root, text="Пошук", command=get_weather, font=("Arial", 12))
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.pack(pady=10)

# Запуск головного циклу
root.mainloop()
