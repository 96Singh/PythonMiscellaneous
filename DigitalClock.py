#!usr/bin/python

import time
import tkinter as tk
from tkinter import *

background_color = input("Please input a colour for background: ")
text_color = input("Please input a colour for clock text: " )

def tick(time1 =''):
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)


root = tk.Tk()
root.title("TIme")
clock_frame = tk.Label(root, font=('arial 100 bold'),bg = background_color, fg=text_color)
clock_frame.pack(fill='both', expand=YES)
root.geometry('600x300')
root.configure(background="green")
tick()
root.mainloop()