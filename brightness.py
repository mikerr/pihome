#!/usr/bin/python
# adjust screen brightness with slider
#
# requires - apt-get install xsetbacklight

from Tkinter import *
from subprocess import *

app=Tk()

slider=Scale(app,orient=HORIZONTAL)
slider.set(50)
slider.pack()

def pressed():
    value = slider.get()
    call("xbacklight -set " + str(value),shell=TRUE)
    
button=Button(app,text="Set brightness",command=pressed)
button.pack()

mainloop()
