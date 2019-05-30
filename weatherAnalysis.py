#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cityData = pd.read_csv ('cityData.csv')
globalData = pd.read_csv ('globalData.csv')
cityData['city_temp'] = cityData['avg_temp'].rolling(7).mean ()
globalData['global_temp'] = globalData['avg_temp'].rolling(7).mean ()

ax = plt.gca ()
cityPlot = cityData.plot (kind='line',x='year',y='city_temp',color='red',label=str (cityData['city'][1]), ax=ax)
globalPlot = globalData.plot (kind='line',x='year',y='global_temp', color='blue',label='Global', ax=ax)
plt.suptitle ('Average Yearly Temperature Comparison')
plt.ylabel ('Temperature (Celcius)')
plt.xlabel ('Year')
plt.savefig ('TempComp.png')