def save(currenttemp, date, text):
    file = open("History.txt", "a")
    file.write(str(currenttemp) + " " + str(date) + " " + str(text) + " " + "\n")


def load(labels):
    file = open("History.txt", "r")
    a = file.readlines()
    if len(a) > 10:
        end = len(a) - 10
    else:
        end = 0
    k = 0
    for i in range(len(a) - 1, end, -1):
        txt1 = a[i]
        txt = txt1.split(" ")
        labels[k][0].config(text=txt[0])
        labels[k][1].config(text=txt[1])
        labels[k][2].config(text=txt[2])
        k += 1


def a():
    print('a')
b = a
b()