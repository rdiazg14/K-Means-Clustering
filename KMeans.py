import pandas as pd
import numpy as np
import matplotlib as plt
import sklearn
from scipy.stats import mode

class KMeans:
    df = pd.DataFrame({})
    kMean=pd.dataFrame()

    def __init__(self, dataFrame, k, runs):
        self.df=dataFrame
        self.kMean=sklearn.cluster.KMeans(n_clusters=k, n_init=runs).fit(self.df)