import tkinter as tk 
import matplotlib.pyplot as plt
import numpy as np 

#function=""

class Frm_logplot():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x300")
        self.root.configure(background='black')
        
        self.function=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Function")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.function)
        self.ent1.place(x=200, y=50)
        
        self.btn1=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn1.place(x=250, y=250)
        
    
    def createclicked(self):
        fun=self.ent1.get()
        i=0
        sin = "np.sin("
        cos = "np.cos("
        tan = "np.tan("
        log = "np.log("
        temp=""
        while i < len(fun):
            if fun[i]=='s':
                temp+=sin
                i+=3
            elif fun[i]=='c':
                temp+=cos
                i+=3
            elif fun[i]=='t':
                temp+=tan
                i+=3
            elif fun[i]=='l':
                temp+=log
                i+=3
            else:
                temp+=fun[i]
            i+=1

        domain = np.linspace(-1*10,10)
        y = [eval(temp) for x in domain]
        plt.plot(domain, y)
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.title('Log-Plot')
        plt.show()
      
        self.root.mainloop()
        
        