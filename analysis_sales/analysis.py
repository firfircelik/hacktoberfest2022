import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
%matplotlib inline


sales_data = pd.read_csv("/vendor_data.csv")
perc =[.20, .40, .60, .80]
include =['object', 'float', 'int']
desc = sales_data.describe(percentiles = perc, include = include)
desc