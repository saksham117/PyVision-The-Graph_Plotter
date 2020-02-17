import tkinter as tk
from line_plot import Frm_line_plot
from histogram import Frm_histogram
from bar_chart import Frm_barchart
from pie_chart import Frm_piechart
#from table import Frm_table
from scatter_plot import Frm_scatter_plot
from log_plot import Frm_logplot
from trigonometric_plot import Frm_trigonometric_plot
from sphere import sphere 
import tkinter.font as font
from cylinder import cylinder
from surface import surface


class Gateway:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Graph plotting")
        
        self.myfont=font.Font(family='Arial black', size=10, weight='bold')
       
       
        self.btn1=tk.Button(self.root,text='Line plot', command=self.line_plot, width=190  , height=30)
        self.btn1.place(x=50, y=100)
        self.btn1['font']=self.myfont
       
        self.photo=tk.PhotoImage(file='line_plot.gif')
        self.photoimage=self.photo.subsample(4,2)
        self.btn1.config(image=self.photoimage, compound=tk.LEFT)
       
        self.btn3=tk.Button(self.root, text= "Histogram", command=self.histogram, width=190, heigh=30)
        self.btn3.place(x=50, y=150)
        self.btn3['font']=self.myfont
       
        self.photo3=tk.PhotoImage(file='histogram.gif')
        self.photoimage3=self.photo3.subsample(4,2)
        self.btn3.config(image=self.photoimage3, compound=tk.LEFT)
       
       
        self.btn5=tk.Button(self.root, text="Bar Charts", command=self.bar_chart, width=190, height=30)
        self.btn5.place(x=50, y=200)
        self.btn5['font']=self.myfont
       
        self.photo5=tk.PhotoImage(file='bar_chart.gif')
        self.photoimage5=self.photo5.subsample(4,2)
        self.btn5.config(image=self.photoimage5, compound=tk.LEFT)
       
        self.btn6=tk.Button(self.root, text="Pie Charts", command=self.pie_chart, width=190, height=30)
        self.btn6.place(x=50, y=250)
        self.btn6['font']=self.myfont
       
        self.photo6=tk.PhotoImage(file='pie_chart.gif')
        self.photoimage6=self.photo6.subsample(4,2)
        self.btn6.config(image=self.photoimage6, compound=tk.LEFT)
       
        self.btn8=tk.Button(self.root, text="Scatter Plots", command=self.scatter_plot, width=190, height=30)
        self.btn8.place(x=50, y=300)
        self.btn8['font']=self.myfont
       
        self.photo8=tk.PhotoImage(file='scatter_plot.gif')
        self.photoimage8=self.photo8.subsample(4,2)
        self.btn8.config(image=self.photoimage8, compound=tk.LEFT)
       
        self.btn9=tk.Button(self.root, text="Log Plots", command=self.log_plot, width=190, height=30)
        self.btn9.place(x=50, y=350)
        self.btn9['font']=self.myfont
       
        self.photo9=tk.PhotoImage(file='log_plot.gif')
        self.photoimage9=self.photo9.subsample(4,2)
        self.btn9.config(image=self.photoimage9, compound=tk.LEFT)
       
        self.btn11=tk.Button(self.root, text="Trigonometric plot", command=self.trigonometric_plot, width=190, height=30)
        self.btn11.place(x=50, y=400)
        self.btn11['font']=self.myfont
       
        self.photo11=tk.PhotoImage(file='trigonometric_plot.gif')
        self.photoimage11=self.photo11.subsample(4,2)
        self.btn11.config(image=self.photoimage11, compound=tk.LEFT)
        
        self.btn12=tk.Button(self.root, text="Sphere", command=self.sphere, width=190, height=30)
        self.btn12.place(x=50, y=450)
        self.btn12['font']=self.myfont
       
        self.photo12=tk.PhotoImage(file='3D_plot.gif')
        self.photoimage12=self.photo12.subsample(4,2)
        self.btn12.config(image=self.photoimage12, compound=tk.LEFT)
        
        self.btn13=tk.Button(self.root, text="Cylinder", command=self.cylinder, width=190, height=30)
        self.btn13.place(x=50, y=500)
        self.btn13['font']=self.myfont
       
        self.photo13=tk.PhotoImage(file='3D_plot.gif')
        self.photoimage13=self.photo13.subsample(4,2)
        self.btn13.config(image=self.photoimage13, compound=tk.LEFT)
        
        self.btn14=tk.Button(self.root, text="3D Line", command=self.surface, width=190, height=30)
        self.btn14.place(x=50, y=550)
        self.btn14['font']=self.myfont
       
        self.photo14=tk.PhotoImage(file='3D_plot.gif')
        self.photoimage14=self.photo14.subsample(4,2)
        self.btn14.config(image=self.photoimage14, compound=tk.LEFT)
        
        self.msg="PyVision\nYour data visualization companion!!\nPyVision is a unique graph plotter which provides you the option to plot the basic line plots to the complex 3-D plots. This tool can even be used for statistical analysis of the data with the help of bar charts, histograms and pie charts. It has the functionality of even solving the complex trigonometric and logarithmic mixed plots. You name it and we plot it!!"
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=450, y=50)
        self.root.mainloop()
       
       
    def line_plot(self):
        obj=Frm_line_plot()
       
    def multiple_subplot(self):
        obj=Frm_multiple_subplot()
       
    def histogram(self):
        obj=Frm_histogram()
       
    def threeD_plotting(self):
        obj=Frm_3D_plotting()
       
    def bar_chart(self):
        obj=Frm_barchart()
       
    def pie_chart(self):
        obj=Frm_piechart()
       
    #def table(self):
     #   obj=Frm_table()
       
    def scatter_plot(self):
        obj=Frm_scatter_plot()
       
    def log_plot(self):
        obj=Frm_logplot()
       
    def polar_plot(self):
        obj=Frm_polar_plot()
       
    def trigonometric_plot(self):
        obj=Frm_trigonometric_plot()
        
    def sphere(self):
        obj=sphere()
        
    def cylinder(self):
        obj=cylinder()
        
    def surface(self):
        obj=surface()
       
   
       
obj=Gateway()