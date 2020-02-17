import tkinter as tk 
import matplotlib.pyplot as plt
#from pie_chart2 import pie_chart
import tkinter.font as font

data=[]
sectors=[]

class Frm_piechart():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x300")
        self.root.configure(background='black')
        
        self.heading=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="Heading")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.heading)
        self.ent1.place(x=200, y=50)
        
        
        self.btn1=tk.Button(self.root, text="Add Sector", command=self.addsectorclicked)
        self.btn1.place(x=100, y=100)
        
        self.btn2=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn2.place(x=200, y=100)
        
        '''self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        self.btn3.pack()'''
        
        '''self.photo=tk.PhotoImage(file="piechart.gif")
        self.lbl1=tk.Label(self.root, image=self.photo, background="black")
        self.lbl1.place(x=200, y=150)'''
        
        
        
    def addsectorclicked(self):
        obj=pie_chart()
    
    def createclicked(self):
        heading=self.ent1.get()
        plt.title(heading)
        plt.pie(data, labels=sectors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.show()
        
        self.root.mainloop()
        
    '''def testclicked(self):
        print(data)
        print(sectors)'''
    
    
        
        
        
        




class pie_chart():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        self.root.configure(background='black')
        
        self.myfont=font.Font(family='Arial black', size=10, weight='bold')
        
        self.name=tk.StringVar()
        self.value=tk.DoubleVar()
        
        self.lbl1=tk.Label(self.root, text=" name of sector")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.name)
        self.ent1.place(x=200, y=50)
        
        self.lbl2=tk.Label(self.root, text="value of data")
        self.lbl2.place(x=50, y=100)
        
        self.ent2=tk.Entry(self.root, textvariable=self.value)
        self.ent2.place(x=200, y=100)
        
        self.btn1=tk.Button(self.root, text="Add", command=self.addclicked, width=10)
        self.btn1.place(x=100, y=150)
        self.btn1['font']=self.myfont
        
        self.btn2=tk.Button(self.root, text="OK", command=self.okclicked, width=10)
        self.btn2.place(x=400, y=380)
        
        #self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        #self.btn3.pack()
        
    def addclicked(self):
        sectors.append(self.ent1.get())
        data.append(self.ent2.get())
        
    def okclicked(self):
        self.root.destroy()
        
    #def testclicked(self):
     #   print(data)
      #  print(sectors)
        
        
        self.root.mainloop()
        
        
        
