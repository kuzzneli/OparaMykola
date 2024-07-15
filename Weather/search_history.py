import json
from tkinter import *
import requests
url = "https://cdn.weatherapi.com/weather/64x64/day/116.png"
query_parameters = {"downloadformat": "png"}
r = requests.get(url, query_parameters)
print(r.url)

def readFromFile(path):
    f = open(path)
    dict = json.load(f)
    return dict


def createBlock(canvas, x, y, city, temp_c, date):
    t = f'{city} \n Temperature: {temp_c} \n {date}'
    canvas.create_text(x, y, text=t)


tk = Tk()
tk.geometry('500x500')
canv = Canvas(width=500, height=500)
canv.pack()
# ph = PhotoImage(file='cdn.weatherapi.com/weather/64x64/day/122.png')
# canv.create_image(ph)

tk.mainloop()
