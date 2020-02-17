import tkinter as tk 
import matplotlib.pyplot as plt
import csv
from tkinter.filedialog import askopenfile



class Frm_scatter_plot():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("800x800")
        self.root.configure(background='black')
        
        self.btn1=tk.Button(self.root, text="Add Points", command=self.opentextfile)
        self.btn1.place(x=50, y=50)
        
        self.btn2=tk.Button(self.root, text="Create", command=self.createclicked)
        self.btn2.place(x=200, y=50)
        
        self.msg="To create a scatter plot we need to enter data in the text file labelled 'scatterplot.txt.\n Click on 'Add points' button.\n Right click on 'scatterplot.txt' and click on 'Open' option from the listed options to open it.\n Enter data in the format:\n X1,Y1\nX2,Y2....\nExample:\n3,11\n50,-65...\n Save the text file and click on create buttton to create the scatter plot"
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=50, y=200)
        #self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        #self.btn3.pack()
        
        
    def opentextfile(self):
        
        file = askopenfile(mode='r', filetypes=[('scatterplot', '*.txt')])
    
    def createclicked(self):
        
        x=[]
        y=[]
        with open('scatterplot.txt','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
                
        fig, ax = plt.subplots()
        plt.scatter(x,y, color='black',s=20, marker="o")
        plt.xlabel('x')
        plt.ylabel('y')
        #plt.title(title)
        ax.set_axisbelow(True)

   
 # Turn on the minor TICKS, which are required for the minor GRID
        ax.minorticks_on()

# Customize the major grid
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    #plt.grid(which ='major',axis ='both',color='r', linestyle='-', linewidth=0.2)
        plt.show()
    
        
        self.root.mainloop()
        
        
        
        
        
