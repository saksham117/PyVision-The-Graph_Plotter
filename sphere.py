import tkinter as tk 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np 
import csv
from tkinter.filedialog import askopenfile

class sphere:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        self.root.title("Graph plotting")
        self.root.configure(background='black')
        
      
        '''self.xcenter=tk.DoubleVar()
        self.ycenter=tk.DoubleVar()
        self.zcenter=tk.DoubleVar()
        self.radius=tk.DoubleVar()
        
        self.lbl1=tk.Label(self.root, text="x-center")
        self.lbl1.pack()
        
        self.ent1=tk.Entry(self.root, textvariable=self.xcenter)
        self.ent1.pack()
        
        self.lbl2=tk.Label(self.root, text="y-center")
        self.lbl2.pack()
        
        self.ent2=tk.Entry(self.root, textvariable=self.ycenter)
        self.ent2.pack()
        
        self.lbl3=tk.Label(self.root, text="z-center")
        self.lbl3.pack()
        
        self.ent3=tk.Entry(self.root, textvariable=self.zcenter)
        self.ent3.pack()
        
        self.lbl4=tk.Label(self.root, text="radius")
        self.lbl4.pack()
        
        self.ent4=tk.Entry(self.root, textvariable=self.radius)
        self.ent4.pack()'''
        
        self.btn1=tk.Button(self.root, text="Add Values", command=self.opentextfile)
        self.btn1.place(x=50, y=50)
        
        self.btn1=tk.Button(self.root, text="create", command=self.createclicked)
        self.btn1.place(x=200, y=50)
        
        self.msg="To create a Sphere we need to enter the data in the text file labelled 'sphere.txt'\n Click on 'Add values' button.\nRight click on 'cylinder.txt' and click on 'Open' option from the listed options to open it.\nEnter data in format:\nx-center,y-center,z-center,radius\nExample:\n3,1,0,5...\nSave the text file and click on the create button to create the sphere" 
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=50, y=100)
        
        self.root.mainloop()
        
        
    def opentextfile(self):
        
        file = askopenfile(mode='r', filetypes=[('sphere', '*.txt')])
        
        
    def createclicked(self):
            
        center_x=0
        center_y=0
        center_z=0
        r=0

        with open('sphere.txt','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                center_x=(float(row[0]))
                center_y=(float(row[1]))
                center_z=(float(row[2]))
                r=(float(row[3]))
            
        
        
        
        
        
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        phi = np.linspace(0, np.pi, 20)
        theta = np.linspace(0, 2*np.pi, 20)
        phi, theta = np.meshgrid(phi, theta)
        
        
        x = np.sin(phi) * np.cos(theta)*r + center_x
        y = np.sin(phi) * np.sin(theta)*r + center_y
        z = np.cos(phi)*r + center_z
        
        ax.plot_wireframe(x, y, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
        
        