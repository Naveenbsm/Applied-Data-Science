# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 02:50:35 2023

@author: navee
"""

import matplotlib.pyplot as plt
import pandas as pd

url = "https://drive.google.com/file/d/17E9N7mbBo87BrV_rPNoJZurt5f_614LE/view"
data = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])
data = data.drop(columns=['Series Name', 'Series Code',
                 'Country Code'])
data = data.dropna()
data = data.rename(columns={'Country Name': 'Country'})
print(data)
print(data.head())

x = data['Country']

y = data['2012 [YR2012]']


# bar graph of year 2012
plt.figure(figsize=(30, 15))
plt.bar(x, y, label= 'Urban population (% of total)')
plt.xlabel('Country')
plt.ylabel('% of population')
plt.title('Urban population (% of total)')
plt.legend()
plt.show()
# pie chart of year 2014
plt.figure(figsize=(8, 5))
plt.pie(data['2002 [YR2002]'], labels=data['Country'])
plt.title('pie chart of Urban population (% of total) for 2002')
plt.show()
# pie chart of year 2020
plt.figure(figsize=(8, 5))
plt.pie(data['2012 [YR2012]'], labels=data['Country'])
plt.title('pie chart of Urban population (% of total) 2012')
plt.show()
# line plot
year = ['2002','2003','2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
#data.drop(['Malaysia'], axis = 0)
plt.figure(figsize=(8, 5))
plt.plot(year, data.iloc[1, 1:12], label='AUS')
plt.plot(year, data.iloc[2, 1:12], label='BGD')
plt.plot(year, data.iloc[4, 1:12], label='CAN')
plt.plot(year, data.iloc[5, 1:12], label='CHN')
plt.plot(year, data.iloc[8, 1:12], label='IND')
plt.plot(year, data.iloc[15, 1:12], label='GBR')
plt.xlabel('Year')
plt.ylabel('% of pop')
plt.title('line plot of Urban population (% of total) 2012 to 2020')
plt.legend()
plt.show()