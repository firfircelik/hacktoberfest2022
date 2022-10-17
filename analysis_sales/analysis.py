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

out = pd.cut(sales_data['Avg_Price_per_unit'], bins=[0, 10, 20, 40,60, 80, 100, 120], include_lowest=True)
out_norm = out.value_counts(sort=False, normalize=True).mul(100)
ax = out_norm.plot.bar(rot=0, color="b", figsize=(15,6))
plt.ylabel("frequency")
plt.xlabel("unit_price")
plt.show()
