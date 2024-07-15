import requests
import time
from datetime import datetime

current_time = datetime.now()
print(current_time.time())
from tkinter import *
import json
r = requests.get('http://api.weatherapi.com/v1/current.json?key=1d814739a97d4eb6998101237241006&q=Sydney&aqi=yes')
data = r.json()
can = Canvas()
ph = PhotoImage(file='./assets/paris.png')
can.create_image(image=ph)
can.create_text()
print(data)
print(time.localtime(time.time()))

def gg():
    print(a)