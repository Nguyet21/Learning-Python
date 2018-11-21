from tkinter import *

tk = Tk()
cas = Canvas(tk, width = 500, height = 600)

cas.pack()

cas.create_polygon(20,20,20,50,70,50)

def dichuyen(event):
    if event.keysym == "Up":
        cas.move(1, 0, -3)

    elif event.keysym == "Down":
        cas.move(1, 0, 3);
    elif event.keysym == "Left":
        cas.move(1, -3, 0)

    else:
        cas.move(1, 3, 0)

cas.bind_all('<KeyPress-Up>', dichuyen)
cas.bind_all('<KeyPress-Down>', dichuyen)
cas.bind_all('<KeyPress-Left>', dichuyen)
cas.bind_all('<KeyPress-Right>', dichuyen)
        
