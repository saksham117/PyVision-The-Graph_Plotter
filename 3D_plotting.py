import tkinter as tk 

class Frm_3D_plotting():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
       
        
        self.btn1=tk.Button(self.root, text="Spheres", command=self.sphereclicked)
        self.btn1.pack()
        
        self.btn2=tk.Button(self.root, text="Cylinder", command=self.cylinderclicked)
        self.btn2.pack()
        
        self.btn3=tk.Button(self.root, text="Cubes", command=self.cubeclicked)
        self.btn3.pack()
        
        self.btn4=tk.Button(self.root, text="3D Plane Surface", command=self.surfaceclicked)
        self.btn4.pack()
        
        self.root.mainloop()
        
    def sphereclicked(self):
        obj=sphere()
    
    def cylinderclicked(self):
        obj=cylinder()
    
    def cubeclikcked(self):
        obj=cube()
    
    def surfaceclicked(self):
        obj=surface()
        
        
        
        
'''class sphere:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        
        self.root.mainloop()
        
        
class cylinder:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        
        self.root.mainloop()
        
        
class cube:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        
        self.root.mainloop()
        
        
class surface:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("500x500")
        
        self.root.mainloop()'''