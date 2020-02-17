import tkinter as tk 
import matplotlib.pyplot as plt
import numpy as np 


class Frm_line_plot():
    def __init__(self):
        
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        self.root.configure(background='black')
        
        self.funtion=tk.StringVar()
        self.min_val=tk.StringVar()
        self.max_val=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Function")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.funtion)
        self.ent1.place(x=200, y=50)
        
        self.lbl2=tk.Label(self.root, text="min_val")
        self.lbl2.place(x=50, y=100)
        
        self.ent2=tk.Entry(self.root, textvariable=self.min_val)
        self.ent2.place(x=200, y=100)
        
        self.lbl3=tk.Label(self.root, text="max_val")
        self.lbl3.place(x=50, y=150)
        
        self.ent3=tk.Entry(self.root, textvariable=self.max_val)
        self.ent3.place(x=200, y=150)
        
        self.btn1=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn1.place(x=300, y=300)
        
    
    def createclicked(self):
        function=self.ent1.get()
        min_val=int(self.ent2.get())
        max_val=int(self.ent3.get())
        
        domain = np.linspace(min_val, max_val)
        y = [eval(function) for x in domain]
        
        plt.plot(domain, y)
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.title('Line-Plot')
        plt.show()
        
        self.root.mainloop()
        
        
    