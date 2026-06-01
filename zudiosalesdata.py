import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=pd.read_csv("C:\\Users\\Surya\\OneDrive\\Download\\Zudio_sales_data.csv")


data["Order Date"]=pd.to_datetime(data['Order Date'],format='mixed')
data['Day'] = data['Order Date'].dt.day
data['Month'] = data['Order Date'].dt.month
data['Year'] = data['Order Date'].dt.year

days_count = data.groupby(['Year','Month'])['Day'].nunique().reset_index()
print(days_count)

days_count['Is_Full_Month'] = days_count['Day'] >= 28
data1= data.merge(days_count[['Year','Month','Is_Full_Month']],
              on=['Year','Month'], how='left')


data['Security Features'] = data['Security Features'].fillna("Not Available")
print(data.isnull().sum())



data["Order Date"]=pd.to_datetime(data['Order Date'],format='mixed')
data['Revenue'] = data['Price'] * data['Quantity']
data['Month'] = data['Order Date'].dt.month
data['Year'] = data['Order Date'].dt.year
data['Day'] = data['Order Date'].dt.day_name()
data["profit_ratio"] = data["Sales Profit"]/data["Revenue"]

plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
monthly_revenue = data.groupby('Month')['Revenue'].sum()

plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.title("MONTHLY ORDER COUNT-SORTED BY VALUE")
plt.xlabel("Month",color='purple')
plt.ylabel("Number of Orders",color='purple')
plt.xticks(rotation=45,color='brown')
plt.yticks(color='brown')
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(2,2,2)
sns.histplot(data['Revenue'], bins=30,color='b',linestyle='--',edgecolor='black',kde=True)
plt.grid(True,linestyle=':')
plt.title("SALES DISTRIBUTION")
plt.xlabel('Total Sales',color='purple')
plt.ylabel('Frequency',color='purple')
plt.xticks(color='brown')
plt.yticks(color='brown')
plt.grid(True, linestyle='--', alpha=0.5)



plt.subplot(2,2,3)
corr = data[['Price', 'Quantity', 'Sales Profit','Revenue']].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title('CORRELATION HEATMAP')
plt.xticks(color='brown')
plt.yticks(color='brown')

plt.subplot(2,2,4)
sns.boxplot(x="Category", y="Revenue", data=data)
plt.title('CATEGORY BY REVENUE (OUTLIERS)')
plt.xlabel('Category',color='purple')
plt.ylabel('Revenue',color='purple')
plt.xticks(color='brown')
plt.yticks(color='brown')

plt.tight_layout()
plt.suptitle('RETAIL SALES ANALYSIS',fontweight='bold')
plt.show()

data.to_csv("zudio_sales_data_cleaned.csv", index=False)
import os
print(os.getcwd())