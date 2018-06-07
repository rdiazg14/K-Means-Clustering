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

from PreProcess import *
from KMeans import *

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
        self.numOfClusEntry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        #Num of runs
        self.numOfRunsLabel = Label(master, text="Num of runs:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.numOfRunsEntry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

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
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "browse":
            self.total += self.entered_number
        elif method == "Pre-Process":
            self.total -= self.entered_number
        else:  # cluster
            self.total = 0

        self.total_label_text.set(self.total)
        self.pathEntry.delete(0, END)

    def browse(self):
        self.filename = tkFileDialog.askopenfilename()
        self.pathEntry.insert(0,self.filename)
        self.df=pd.read_excel(self.filename)

    def preProc(self):
        dataCleaner = PreProcess(dataframe)
        self.df=dataCleaner.df
        #alert user
        tkMessageBox.showinfo("K Means Clustering", "Preprocessing completed successfully!")
        pass

    def kMeans(self):
        cluster = KMeans(self.df, self.numOfClusEntry.get(), self.numOfRunsEntry.get())
        self.df=dataCleaner.df
        #alert user
        tkMessageBox.showinfo("K Means Clustering", "Preprocessing completed successfully!")
        pass


root = Tk()
my_gui = GUI(root)
root.mainloop()
