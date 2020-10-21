# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
#Code starts here
data = pd.read_csv(path)
data = data.rename(columns={'Total':'Total_Medals'})
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1],inplace=True)
#print(top_countries.tail())
def top_ten(top_countries,column):
    country_list = []
    largest = top_countries.nlargest(10,column)
    country_list = list(largest['Country_Name'])
    return country_list
top_10_summer = top_ten(top_countries,['Total_Summer'])
top_10_winter = top_ten(top_countries,['Total_Winter'])
top_10 = top_ten(top_countries,['Total_Medals'])
print(top_10_summer)
print(top_10_winter)
print(top_10)
def common_member(a,b,c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)
    if (set_a & set_b & set_c):
        common_list = list(set_a & set_b & set_c)
    return common_list
common = common_member(top_10_summer,top_10_winter,top_10)
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#print(summer_df)
#print(winter_df)
#print(top_df)
summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')
winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')
top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
#print(summer_df)
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = str(summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio].iloc[0])
print(summer_max_ratio)
print(summer_country_gold)
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio].iloc[0]
print(winter_max_ratio)
print(winter_country_gold)
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio].iloc[0]
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
data.drop(data.index[-1],inplace = True)
data_1 = data
#print(data_1.tail())
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total']*1)
#print(data_1['Total_Points'].head())
most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points']==most_points].iloc[0]
print(most_points)
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals')
plt.xticks(rotation=45)


