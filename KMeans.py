import pandas as pd
import numpy as np
import matplotlib as plt
from scipy.stats import mode

class KMeans:
    df = pd.DataFrame({})

    def __init__(self, dataFrame):
        df=dataFrame