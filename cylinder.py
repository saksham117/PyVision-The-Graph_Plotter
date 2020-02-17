import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np 
import csv
from tkinter.filedialog import askopenfile 

class cylinder:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Graph plotting")
        self.root.configure(background='black')
        
        self.btn1=tk.Button(self.root, text="Add Values", command=self.opentextfile)
        self.btn1.place(x=50, y=50)
        
        self.btn1=tk.Button(self.root, text="create", command=self.createclicked)
        self.btn1.place(x=200, y=50)
        
        self.msg="To create a Cylinder we need to enter the data in the text file labelled 'cylinder.txt'\nClick on 'Add values' button.\nRight click on 'cylinder.txt' and click on'Open option from the listed options to open it.\n Enter data in the format:\nx-center,y-center,height,radius\nExample:\n2,1,10,6...\nSave the text file and click on the create button to create the cylinder"
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=50, y=200)
        self.root.mainloop()
        
        
    def opentextfile(self):
        
        file = askopenfile(mode='r', filetypes=[('cylinder', '*.txt')])
        
        
    def createclicked(self):
            
        center_x = 0
        center_y = 0
        radius = 0
        height_z = 0

        with open('cylinder.txt','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                center_x=(float(row[0]))
                center_y=(float(row[1]))
                height_z=(float(row[2]))
                radius=(float(row[3]))
                
                
        z = np.linspace(0, height_z, 50)
        theta = np.linspace(0, 2*np.pi, 50)
        theta_grid, z_grid=np.meshgrid(theta, z)
        x_grid = radius*np.cos(theta_grid) + center_x
        y_grid = radius*np.sin(theta_grid) + center_y
    

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5)

        plt.show()
        
       
        