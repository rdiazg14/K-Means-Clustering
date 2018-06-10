import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
import sklearn
from scipy.stats import mode
from sklearn.cluster import KMeans
#import plotly.plotly as py
from PIL import Image
import plotly.plotly as py


class KMeans:
    df = pd.DataFrame({})
    kMean=pd.DataFrame({})
    scatterPlot=None

    def __init__(self, dataFrame, k, runs):
        self.df=dataFrame
        self.kMean=sklearn.cluster.KMeans(n_clusters=k, n_init=runs).fit(self.df)
        self.df["cluster"]=self.kMean.labels_
        print (self.df)
        self.df.reset_index(level=0,inplace=True)
        self.printScatter()
        self.printMap()

    def printScatter(self):
        #create scatter
        self.scatterPlot=plt.scatter(x=self.df["Social support"], y=self.df["Generosity"], c=self.df["cluster"])
        plt.title("K-Means Clustering")
        plt.xlabel("Social support")
        plt.ylabel("Generosity")
        #save scatter as image
        plt.savefig("scatterPlt.png")
        im = Image.open("scatterPlt.png")
        im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        im.save('scatterPlt.gif')

    def printMap(self):

        pass