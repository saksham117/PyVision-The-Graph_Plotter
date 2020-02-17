import tkinter as tk 
import matplotlib.pyplot as plt 
import numpy as np
import csv
from tkinter.filedialog import askopenfile


#bin_range=[]


class Frm_histogram():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("800x800")
        self.root.configure(background='black')
        
        
        #self.gap=tk.DoubleVar()
        #self.maxval=tk.DoubleVar()
        
        self.xtitle=tk.StringVar()
        self.heading=tk.StringVar()
        
        self.lbl1=tk.Label(self.root, text="X-title")
        self.lbl1.place(x=50, y=50)
        
        self.ent1=tk.Entry(self.root, textvariable=self.xtitle)
        self.ent1.place(x=200, y=50)
        
        self.lbl2=tk.Label(self.root, text="Heading")
        self.lbl2.place(x=50, y=100)
        
        self.ent2=tk.Entry(self.root, textvariable=self.heading)
        self.ent2.place(x=200, y=100)
        
        self.btn1=tk.Button(self.root, text="Add values", command=self.opentextfile)
        self.btn1.place(x=50, y=200)
        
        self.btn2=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn2.place(x=200, y=200)
        
        self.msg="To create a Histogram we need to enter the data in the text file labelled 'histogram.txt'.\n Click on 'Add values' button.\n Right click on 'histogram.txt' and click on 'Open' option from the listed options to open it.\n Enter data in the format:\n X1,X2,X3,....\n Example:\n3,11,65,84....\n Save the text file and click on create button to create the histogram."
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=50, y=300)
        
        #self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        #self.btn3.pack()
        
        '''
        self.lbl1=tk.Label(self.root, text="Enter Gap")
        self.lbl1.pack()
        
        #self.ent1=tk.Entry(self.root, textvariable=self.gap)
        #self.ent1.pack()
        
        self.lbl2=tk.Label(self.root, text="Max Value")
        self.lbl2.pack()
        
        self.ent2=tk.Entry(self.root, textvariable=self.maxval)
        self.ent2.pack()'''
        
    def opentextfile(self):
        
        file = askopenfile(mode='r', filetypes=[('histogram', '*.txt')])
        
    
    def createclicked(self):
        
         xtitle=self.ent1.get()
         heading=self.ent2.get()
        
         values=[]
         
         values.append(np.loadtxt('histogram.txt', delimiter=',', unpack=True))
         
         plt.hist(values, bins='auto',alpha=0.7, rwidth=1)
         plt.xlabel(xtitle)
         plt.ylabel('Frequency')
         plt.title(heading)
         plt.show()

        
         self.root.mainloop()
        
        
        
