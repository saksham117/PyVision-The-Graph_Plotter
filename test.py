'''import tkinter as tk
from tkinter.filedialog import askopenfile


class Gateway:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Graph plotting")
        self.root.configure(background='black')
        
        self.btn1=tk.Button(self.root, text="file", command=self.opentextfile)
        self.btn1.pack()
        
        self.root.mainloop()  
        
        
    def opentextfile(self):
        f=open("text.txt")
        t.insert(1.0, f.read())
        file = askopenfile(mode='r', filetypes=[('text', '*.txt')])
        
              
obj=Gateway()

from tkinter import PhotoImage, Tk, Entry
from tkinter.ttk import Label

from tkinter import *
root = Tk()
photo = PhotoImage(file="bar_chart.gif")
w = Label(root, image=photo)
w.pack()
ent = Entry(root)
ent.pack()
ent.focus_set()
root.mainloop()'''