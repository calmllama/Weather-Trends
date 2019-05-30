#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt


# In[75]:


cityData = pd.read_csv ('cityData.csv')
globalData = pd.read_csv ('globalData.csv')
cityData = cityData.drop (['city', 'country'], axis=1)
cityData['city_temp'] = cityData['avg_temp'].rolling(7).mean ()
globalData['global_temp'] = globalData['avg_temp'].rolling(7).mean ()


# In[76]:


ax = plt.gca ()
cityData.plot (kind='line',x='year',y='city_temp',color='red', ax=ax)
globalData.plot (kind='line',x='year',y='global_temp',color='blue', ax=ax)
plt.show ()


# In[ ]:





# In[ ]:




