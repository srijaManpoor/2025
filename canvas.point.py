from tkinter import *
from tkinter import Tk
bin.geometry('700x300')
def draw_point(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
Canvas.create_oval(x1,y1,x2,y2,fill='black',width=30)
Canvas.Canvas(bin,width=700,height=350,background='green')
Canvas.grid(row=0,column=0)
Canvas.bind('<Button-1>',draw_point)
click_num=0
bin.mainloop()
