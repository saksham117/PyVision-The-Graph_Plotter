import tkinter as tk 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


class surface:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Graph plotting")
        self.root.configure(background='black')
        
        self.function=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Enter Function")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.function)
        self.ent1.place(x=200, y=50)
        
        self.btn1=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn1.place(x=150, y=300)
        
        
        self.root.mainloop()
        
    def createclicked(self):
        function=self.ent1.get()
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        xline = np.linspace(0, 15, 50)
        yline = np.linspace(0, 15, 50)
        zline = [eval(function) for x,y in zip(xline, yline)]
        ax.plot3D(xline, yline, zline)
        plt.show()
        
        