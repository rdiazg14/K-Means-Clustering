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


class KMean:
    df = pd.DataFrame({})
    kMean=pd.DataFrame({})
    scatterPlot=None

    def __init__(self, dataFrame, k, runs):
        self.df=dataFrame
        self.kMean=KMeans(n_clusters=k, n_init=runs).fit(self.df)
        #self.df['cluster']=self.kMean.labels_
        #print (self.df)
        temper=self.kMean.predict(self.df)
        self.df['cluster']=temper
        self.df.reset_index(inplace=True)
        self.printScatter()
        self.createMap()

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

    # save Map as image

    def createMap(self):
        scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
               [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

        data = [dict(
            type='choropleth',
            colorscale=scl,
            autocolorscale=False,
            locations=self.df['country'],
            z=self.df['cluster'].astype(float),
            locationmode='country names',
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
        py.sign_in("sarfatyl","AAk5mt9UQlWdoE7aOiZ7")
        fig = dict(data=data, layout=layout)
        py.iplot(fig, filename='d3-cloropleth-map',auto_open=False)
        py.image.save_as(fig, filename="mapPLT.png")
        temp=Image.open("mapPLT.png")
        temp = temp.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        temp.save('mapPLT.gif')