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
        py.sign_in("sarfatyl","AAk5mt9UQlWdoE7aOiZ7")


        scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
               [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

        data = [dict(
            type='choropleth',
            colorscale=scl,
            autocolorscale=False,
            locations=self.df['country'],
            z=self.df['cluster'].astype(float),
            locationmode='Country Name',
            text=self.df['country'],
            marker=dict(
                line=dict(
                    color='rgb(255,255,255)',
                    width=2
                )),
            colorbar=dict(
                title="Cluster")
        )]

        layout = dict(
            title='K-Means Clustering Visualization',
            geo=dict(
                scope='cluster group',
                projection=dict(type='Mercator'),
                showlakes=True,
                lakecolor='rgb(255, 255, 255)'),
        )

        fig = dict(data=data, layout=layout)
        py.iplot(fig, filename='d3-cloropleth-map')
        py.image.save_as(fig, filename="mapPLT.png")
        temp=Image.open("mapPLT.png")
        temp = temp.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        temp.save('map.gif')