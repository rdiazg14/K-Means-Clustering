'''try:
    # for Python2
    from Tkinter import Tk, Label, Button, Entry, IntVar, END, W, E   ## notice capitalized T in Tkinter
    from Tkinter.filedialog import askopenfilename
    from Tkinter import tkMessageBox
except ImportError:
    # for Python3
    from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E   ## notice lowercase 't' in tkinter here
    from tkinter.filedialog import askopenfilename
   from tkinter import tkMessageBox'''


import tkFileDialog
import tkMessageBox
from Tkinter import *
import pandas as pd
import numpy as np
import matplotlib as plt
from scipy.stats import mode
from Tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import matplotlib.pyplot as plt
from PreProcess import *
from KMeans import *
#from pre import model
import os

class GUI:

    df=pd.DataFrame({})

    def __init__(self, master):
        self.master = master
        master.title("K-Means Clustering")

        #Data path
        self.pathLabel = Label(master, text="Data path:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.pathEntry = Entry(master, validate="key") ##path for data
        self.browse_button = Button(master, text="Browse", command=lambda: self.browse())

        #Num of clusters k
        self.numOfClusLabel = Label(master, text="Num of clusters k:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.numOfClusEntry = Entry(master, validate="key")

        #Num of runs
        self.numOfRunsLabel = Label(master, text="Num of runs:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.numOfRunsEntry = Entry(master, validate="key")

        #pre process
        self.prePro_button = Button(master, text="Pre-Process", command=lambda: self.preProc())

        #cluster
        self.cluster_button = Button(master, text="Cluster", command=lambda: self.kMeans())

        # LAYOUT
        self.pathLabel.grid(row=1, column=0)
        self.pathEntry.grid(row=1, column=1, sticky=W+E)
        self.browse_button.grid(row=1,column=2)

        self.numOfClusLabel.grid(row=2, column=0)
        self.numOfClusEntry.grid(row=2, column=1)

        self.numOfRunsLabel.grid(row=3, column=0)
        self.numOfRunsEntry.grid(row=3, column=1)

        self.prePro_button.grid(row=4, column=1)

        self.cluster_button.grid(row=5, column=1)

    def validate(self, new_text):
        '''if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False'''

    def browse(self):
        self.filename = tkFileDialog.askopenfilename()
        self.pathEntry.insert(0,self.filename)
        self.df=pd.read_excel(self.filename)

    def preProc(self):
        dataCleaner = PreProcess(self.df)
        self.df=dataCleaner.df
        #alert user
        tkMessageBox.showinfo("K Means Clustering", "Preprocessing completed successfully!")
        pass

    def kMeans(self):
        cluster = KMeans(self.df, int(self.numOfClusEntry.get()), int(self.numOfRunsEntry.get()))
        self.df=cluster.df
        #set scatter plot
        path=r'./scatterPlt.gif'
        scatterPlt=PhotoImage(file=path)
        self.scatterLbl=Label(image=scatterPlt)
        self.scatterLbl.image=scatterPlt
        self.scatterLbl.grid(row=6, column=2)
        #set map plot
        path=r'./mapPLT.gif'
        mapPlt=PhotoImage(file=path)
        self.mapLbl=Label(image=mapPlt)
        self.mapLbl.image=mapPlt
        self.mapLbl.grid(row=6, column=1)
        #alert user
        tkMessageBox.showinfo("K Means Clustering", "Clustering completed successfully!")


root = Tk()
my_gui = GUI(root)

def on_closing():
    if tkMessageBox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
        os._exit(0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
