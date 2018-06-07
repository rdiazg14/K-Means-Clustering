import pandas as pd
import numpy as np
import matplotlib as plt
from scipy.stats import mode

class PreProcess:

    df=pd.DataFrame({})

    def __init__(self,dataFrame):
        self.df = dataFrame
        self.fillNaAndNorm()
        self.groupByCountry()

    #fill na and normalize
    def fillNaAndNorm(self):
        for column in self.df.columns[1:]:
            self.df[column].fillna(self.df[column].mean(), inplace=True)
            #standerization
            avg=self.df[column].mean()
            std=np.std(self.df[column])
            self.df[column]=(self.df[column]-avg)/std

    #group by country
    def groupByCountry(self):
        self.df=self.df.groupby("country").mean()
        del self.df["year"]


dataframe=pd.read_excel("D:\\data.xlsx")
dataCleaner = PreProcess(dataframe)
