# import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# import the dataset

dataset = pd.read_csv('data/bank-additional/bank-additional.csv')

print(dataset.head(10))