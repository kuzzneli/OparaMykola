from tkinter import*
import json

def move(ver_hor, rlud):
    global coordinates, c1
    canva.delete(c1)
    if rlud == '+':
        coordinates[ver_hor] += 10
    else:
        coordinates[ver_hor] -= 10
    c1 = canva.create_oval(coordinates['x'], coordinates['y'], coordinates['x'] + size, coordinates['y'] + size,
                           fill="red")

def save():
    global coordinates, c1
    file = open("Save2.txt", "w")
    json_str = json.dumps(coordinates)
    file.write(json_str)
def load():
    global coordinates, c1
    file=open("Save2.txt", "r")
    coordinates = json.load(file)
    print(coordinates['x'],coordinates['y'])
    canva.delete(c1)
    c1=canva.create_oval(coordinates['x'], coordinates['y'], coordinates['x'] + size, coordinates['y'] + size,fill="red")


vikno=Tk()
vikno.geometry("600x600")
b1=Button(text="↑",command=lambda : move('y', '-'))
b1.place(x=50, y=20)
b2=Button(text="↓", command=lambda : move('y', '+'))
b2.place(x=50, y=60)
b3=Button(text="←",command=lambda : move('x', '-'))
b3.place(x=20, y=40)
b4=Button(text="→",command=lambda : move('x', '+'))
b4.place(x=75, y=40)
b5=Button(text="зберегти",command=save)
b5.place(x=115, y=25)
b6=Button(text="завантажити",command=load)
b6.place(x=115, y=55)
canva=Canvas(width=600,height=600)
canva.place(x=0,y=100)
coordinates = {
    'x' : 100,
    'y' : 100
}

size = 20
c1=canva.create_oval(coordinates['x'],coordinates['y'],coordinates['x']+size,coordinates['y']+size,fill="red")
vikno.mainloop()