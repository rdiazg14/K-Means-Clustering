import pandas as pd
import numpy as np
import matplotlib as plt
import sklearn
from scipy.stats import mode
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#import plotly.plotly as py

class KMeans:
    df = pd.DataFrame({})
    kMean=pd.DataFrame({})

    def __init__(self, dataFrame, k, runs):
        self.df=dataFrame
        self.kMean=sklearn.cluster.KMeans(n_clusters=k, n_init=runs).fit(self.df)
        print (self.kMean)