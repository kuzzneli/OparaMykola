import requests
from tkinter import *
from datetime import datetime
from j import *


def search():
    global text, e1, winddirection, windspeed, currenttemp, feelslike, icon, date
    text = e1.get()
    b = "http://api.weatherapi.com/v1/current.json?key=2b38f3ba988b4a22a0255325240107&q=" + text
    response = requests.get(b)
    n = response.json()
    print(n)
    winddirection = n["current"]["wind_dir"]
    windspeed = n["current"]["wind_kph"]
    currenttemp = n["current"]["temp_c"]
    feelslike = n["current"]["feelslike_c"]
    icon = n["current"]["condition"]["icon"]
    text1 = n["current"]["condition"]["text"]
    time1 = datetime.now()
    date = time1.date()
    l1["text"] = text
    l2["text"] = str(currenttemp) + "°С, Відчувається як " + str(feelslike) + "°С"
    l3["text"] = "Швидкість вітру " + str(windspeed) + " км/год"
    l4["text"] = date
    l5["text"] = "Напрямок вітру: " + str(winddirection)
    l6["text"] = text1
    save(currenttemp, date, text)
    load(labels)


vikno = Tk()
vikno.geometry("600x700")

e1 = Entry(width=25)
e1.place(x=225, y=50)
b1 = Button(text="Пошук 🔍", command=search)
b1.place(x=450, y=45)
l1 = Label(text="Місто")
l1.place(x=225, y=100)
l4 = Label(text="Час")
l4.place(x=225, y=125)
l2 = Label(text="Температура, відчувається як")
l2.place(x=225, y=150)
l3 = Label(text="Швидкість вітру")
l3.place(x=225, y=175)
l5 = Label(text="Напрямок вітру")
l5.place(x=225, y=200)
l6 = Label(text="Стан")
l6.place(x=225, y=225)
# ---------------------1
labels = []
blocks_y = 100
for i in range(10):
    labels.append((Label(text=""), Label(text=""), Label(text="")))
    labels[i][0].place(x=50, y=blocks_y)
    labels[i][1].place(x=50, y=blocks_y + 15)
    labels[i][2].place(x=50, y=blocks_y + 30)
    blocks_y += 50
load(labels)
# canva=Canvas(width=600, height=600)
# canva.pack(side="bottom")

# ключ - 2b38f3ba988b4a22a0255325240107
vikno.mainloop()
