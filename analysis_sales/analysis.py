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

sns.set_theme(style="whitegrid")
#ax = sns.violinplot(x=sales_data["unit_price"])
sns.boxplot(x=sales_data["Avg_Price_per_unit"])

sales_data['price_frqn_cat'] = pd.cut(sales_data.Avg_Price_per_unit, [-np.inf, 10, 20, 40, 60, 80, 100, 120, np.inf],labels=['-inf_10','10-20','20-40','40-60','60-80','80-100','100-120','120-inf'])
grouped = sales_data.groupby(
    ['price_frqn_cat']
).agg({
    'Avg_Price_per_unit': ["min","max","mean"],
    'Average_units_sold': ["mean","sum"],
    'Incremental_acquisition': ["mean"],
    'Increase_sale_volume': ["mean"],
    'Products':["count"]
}
)
grouped.columns = ["_".join(x) for x in grouped.columns.ravel()]
grouped.head(10)

*****
price range (40 - 60)
● contains highest# of product (61)
● highest# of avg units sold_mean (1.6)
● good avgrage price-elasticity ( 14.2 % Incremental_acquisition, 5.67 % Increase_sale_volume)
*****

sns.displot(sales_data, x="Average_units_sold", hue="price_frqn_cat", kind="kde")

out = pd.cut(sales_data['Average_units_sold'], bins=[-np.inf, 0, 0.5, 1.0, 2.0, 3.0, 4.0, np.inf], include_lowest=True)
out_norm = out.value_counts(sort=False, normalize=True).mul(100)
ax = out_norm.plot.bar(rot=0, color="b", figsize=(15,6))
#ax.set_xticklabels([c[1:-1].replace(","," to") for c in out.cat.categories])
plt.ylabel("frequency")
plt.xlabel("Average_units_sold")
plt.show()

*****
PROFIT
*****
sales_data['profit']=sales_data['Average_units_sold']*(sales_data['Avg_Price_per_unit']-sales_data['Cost_per_unit'])
out = pd.cut(sales_data['profit'], bins=[-np.inf, 0, 5, 10, 20, 40,60, 80, 100], include_lowest=True)
out_norm = out.value_counts(sort=False, normalize=True).mul(100)
ax = out_norm.plot.bar(rot=0, color="b", figsize=(10,6))
plt.ylabel("frequency")
plt.xlabel("profit")
plt.show()

sales_data['profit_cat'] = pd.cut(sales_data.profit, [-np.inf, 0, 10, 20, 40, 60, 80, 100],labels=['-inf_0','0-10','10-20','20-40','40-60','60-80','80-100'])
price_grouped = sales_data.groupby(
    ['profit_cat']
).agg({
    'Avg_Price_per_unit': ["mean"],
    'Average_units_sold': ["mean","sum"],
    'Incremental_acquisition': ["mean"],
    'Increase_sale_volume': ["mean"],
    'profit': ["mean","sum"],
    'Products':["count"]
}
)
price_grouped.columns = ["_".join(x) for x in price_grouped.columns.ravel()]
price_grouped.head(10)