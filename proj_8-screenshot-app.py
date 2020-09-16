# Screenshot app

from tkinter import *
import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = '{}.png'.format(name)
    time.sleep(1)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()
root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()
button_1 = Button(frame,text="Screenshot!!",command=screenshot)
button_1.pack(side=LEFT)
button_2 = Button(frame, text="Exit",command=quit)
button_2.pack(side=LEFT)
root.mainloop()
