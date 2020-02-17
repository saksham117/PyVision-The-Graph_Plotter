import tkinter as tk
import matplotlib.pyplot as plt
import csv
from tkinter.filedialog import askopenfile
plt.style.use('ggplot')



class Frm_barchart():
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("800x800")
        self.root.configure(background='black')

        self.xtitle=tk.StringVar()
        self.ytitle=tk.StringVar()
        self.heading=tk.StringVar()

        self.btn1=tk.Button(self.root, text="Enter Data", command=self.opentextfile)
        self.btn1.place(x=100, y=350)

        self.btn2=tk.Button(self.root, text="Create Bar Chart", command=self.createclicked)
        self.btn2.place(x=300, y=350)
        
        '''self.lbl6=tk.Label(self.root, text=\n"To create a bar chart we need to enter the data in the text file labelled 'barchart.txt'.
                           click on 'Enter Data' button, Right click on 'barchart.txt' and click on 'Open' option to open it. 
                           Enter the data in the format:
                           VALUE 1, LABEL 1
                           VALUE 2, LABEL 2....
                           Example:
                           30,India
                           50,USA
                           Save the text file and click on create button to create the bar chart"\n, height=30)
        self.lbl6.place(x=100, y=450)'''
        
        self.msg="To create a bar chart we need to enter the data in the text file labelled 'barchart.txt'\n.Click on 'Enter Data' button, Right click on 'barchart.txt' and click on 'Open' option to open it.\n Enter the data in the format:\nVALUE 1, LABEL 1.\nVALUE 2, LABEL 2....\nExample:\n30,India.\n50,USA.\nSave the text file and click on create button to create the bar chart"
        self.a=tk.Message(self.root, text=self.msg)
        self.a.place(x=100, y=450)
        #self.btn3=tk.Button(self.root, text="test", command=self.testclicked)
        #self.btn3.pack()

        self.lbl3=tk.Label(self.root, text="x-Title")
        self.lbl3.place(x=50, y=50)

        self.ent3=tk.Entry(self.root, textvariable=self.xtitle)
        self.ent3.place(x=200, y=50)

        self.lbl4=tk.Label(self.root, text="y-Title")
        self.lbl4.place(x=50, y=100)

        self.ent4=tk.Entry(self.root, textvariable=self.ytitle)
        self.ent4.place(x=200, y=100)

        self.lbl5=tk.Label(self.root, text="Heading")
        self.lbl5.place(x=50, y=150)

        self.ent5=tk.Entry(self.root, textvariable=self.heading)
        self.ent5.place(x=200, y=150)
        
        '''self.photo=tk.PhotoImage(file ="bar_chart.gif")
        self.lbl6=tk.Label(self.root, image=self.photo)
        self.lbl6.pack()'''
    
    def opentextfile(self):
        
        file = askopenfile(mode='r', filetypes=[('bar_chart', '*.txt')])

    def createclicked(self):
        bars = []
        data = []
        xtitle=""
        ytitle=""
        heading=""
        
        xtitle=self.ent3.get()
        ytitle=self.ent4.get()
        heading=self.ent5.get()

        with open('bar_chart.txt','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                data.append(int(row[0]))
                bars.append(row[1])
        bars_pos = [i for i, _ in enumerate(bars)]
        plt.bar(bars_pos, data)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.title(heading)
        plt.xticks(bars_pos, bars)
        plt.show()
        
        self.root.mainloop()

       


    '''def testclicked(self):
        print(bars)
        print(data)'''

        




