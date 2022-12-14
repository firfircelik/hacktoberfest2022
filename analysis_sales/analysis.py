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

****
● 9 items dont bring any profit with lowest Incremental_acquisition_mean (~0.09)
● totally 125 items have lowest profit margin ($3.9) and lowest avg. sold (profit_cat 0-10)

● 2 items bring highest profit with highest Incremental_acquisition_mean (~0.16)
● totally 2 items have highest profit margin ($70.3) and highest avg. sold (profit_cat 60-80)
****

incr_cvr_val = sales_data["Incremental_acquisition"] * 10000
sns.boxplot(x=incr_cvr_val)

out = pd.cut(incr_cvr_val, bins=[0, 5, 10, 20, 40,60, 80, 100], include_lowest=True)
out_norm = out.value_counts(sort=False, normalize=True).mul(100)
ax = out_norm.plot.bar(rot=0, color="b", figsize=(10,6))
plt.ylabel("frequency")
plt.xlabel("cvr_incr_group")
plt.show()

sales_data['incr_cvr_perc'] = sales_data["Incremental_acquisition"] * 10000
sales_data['incr_cvr_cat'] = pd.cut(sales_data['incr_cvr_perc'], [-np.inf, 0, 5, 10, 20, 40, 60, 80],
                                    labels=['-inf_0','0-5','5-10','10-20','20-40','40-60','60-80'])
incr_cvr_groups = sales_data.groupby(
    ['incr_cvr_cat']
).agg({
    'Products':["count"],
    'incr_cvr_perc': ["min","max","mean"]
}
)
incr_cvr_groups.columns = ["".join(x) for x in incr_cvr_groups.columns.ravel()]
incr_cvr_groups.head(10)

incr_sales_val = sales_data["Increase_sale_volume"] * 100
sales_data['incr_sales_perc'] = sales_data['Increase_sale_volume']*100
sales_data['incr_sales_cat'] = pd.cut(sales_data['incr_sales_perc'], [0, 1, 2, 4, 6, 8, 10],labels=['0_1','1_2','2_4','4_6', '6_8', '8_10'])
incr_sales_grouped = sales_data.groupby(
    ['incr_sales_cat']
).agg({
    'incr_sales_perc': ["min","max","mean","count"]
}
)
incr_sales_grouped.columns = ["_".join(x) for x in incr_sales_grouped.columns.ravel()]
incr_sales_grouped.head(10)