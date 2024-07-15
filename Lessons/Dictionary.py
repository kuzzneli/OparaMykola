from tkinter import *
tk = Tk()
tk.geometry("500x500")
canvas = Canvas(width=500, height=400)
canvas.place(x=0, y=100)
def func(x):
    print(x)
    return x


def move_left():
    global x, y
    canvas.delete(c1)
    x += 10
    canvas.create_oval(x, y, x + size, y + size)


move_r_1 = Button(text='Right', command = lambda : func('right'))
move_l_1 = Button(text='Left', command = lambda : func('left'))
move_u_1 = Button(text='Up', command = lambda : func('up'))
move_d_1 = Button(text='Down', command = lambda : func('down'))


move_r_1.place(x=25, y=25)
move_l_1.place(x=75, y=25)
move_u_1.place(x=50, y=0)
move_d_1.place(x=50, y=50)
x = 200
y = 150
size = 50
c1 = canvas.create_oval(x,y,x+size,y+size)

tk.mainloop()