import tkinter as tk 



class pie_chart():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        self.root.configure(background='black')
        
        self.data=[]
        self.sectors=[]
        
        self.name=tk.StringVar()
        self.value=tk.StringVar()
        
        self.ent1=tk.Entry(self.root, textvariable=self.name)
        self.ent1.pack()
        
        self.ent2=tk.Entry(self.root, textvariable=self.value)
        self.ent2.pack()
        
        self.btn1=tk.Button(self.root, text="Add", command=self.addclicked)
        self.btn1.pack()
        
        self.btn2=tk.Button(self.root, text="OK", command=self.okclicked)
        self.btn2.pack()
        
        #self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        #self.btn3.pack()
        
    def addclicked(self):
        self.data.append(self.ent1.get())
        self.sectors.append(self.ent2.get())
        
    def okclicked(self):
        self.root.destroy()
        
    #def testclicked(self):
     #   print(data)
      #  print(sectors)
        
        
        self.root.mainloop()
        
        
        
