#!/usr/bin/env python
# coding: utf-8

# # Working real project with python
#  The wether data set
#     ,it records,Temperature,Dew point,Humidity,Wind speed,Visibilty,,presuure,and condition.

# # Working real project with python
#  The wether data set
#     ,it records,Temperature,Dew point,Humidity,Wind speed,Visibilty,,presuure,and condition.

# # the data set avilable in csv file.we 
# are going to anlyze;

# In[3]:


import pandas as pd


# In[6]:


df= pd.read_csv("D:\\Marriage\\Weather data.csv")
print(df)


# In[9]:


df.head()


# In[10]:


df.shape


# In[11]:


df.index


# In[12]:


df.columns


# In[13]:


df.dtypes


# In[17]:


df['Weather'].unique()


# In[18]:


df.nunique()


# In[19]:


df.count()


# In[23]:


df['Weather'].value_counts()


# In[25]:


df.info()


# # Find all the UNique "wind speed" values in data.

# In[26]:


df.head(2)


# In[28]:


df.nunique()


# In[31]:


df['Wind Speed_km/h'].nunique()


# In[32]:


df['Wind Speed_km/h'].unique()  #answers()


# # Q2..Find the number of times when the 'weather is excatly clear'..

# In[33]:


df. head(2)


# In[ ]:


# value _counts()


# In[35]:


df.Weather.value_counts()


# In[ ]:


#filetering


# In[42]:


df[df.Weather== 'Clear']


# In[ ]:


#GROUPBY()


# In[44]:


df.groupby ('Weather').get_group('Clear')


# # Q3 find the number of times when the wind speed was exactly 4km/h''.

# In[45]:


df.head(2)


# In[46]:


df[df['Wind Speed_km/h']==4]                ##exctat match df 2times


# # Q4--find out all the nun values in data.

# In[52]:


df.isnull().sum()


# # Q5 --- Rename the
# column name "weather"of data frame to "wether condition"

# In[60]:


df.rename(columns={'Weather':'Weather Condition'})    #column name temporary purpose 


# In[59]:


df.rename(columns={'Weather':'Weather Condition'},inplace=True)  ### incase not change permanetly using inplace=True


# In[61]:


df.head(2)


# # Q6  What is the min visibility ?

# In[62]:


df.head(2)


# In[64]:


df.Visibility_km.mean()


# # Q7..what is the std of pressure in this data?

# In[65]:


df.Press_kPa.std()


# # Q8... what is the variance of Relative Humidity in this data?

# In[66]:


df['Rel Hum_%'].var()


# # Q9....Find all the instance when 'snow was recorded'.

# In[ ]:


## value_counts()


# In[67]:


df['Weather Condition'].value_counts()


# In[ ]:


## filtering


# In[73]:


df[df['Weather Condition']=='Snow']


# In[ ]:


##str.contains


# In[75]:


df[df['Weather Condition'].str.contains('Snow')]


# # 10######### find all instance when 'wind speed' is above 24 and 'visibility' is 25

# In[79]:


df[(df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)]


# # what is minimum and max value of each column against each Weather Condition?

# In[86]:


df.head(2)


# In[90]:


df.groupby ('Weather Condition'). max()


# # Q13#### show all the records where weather  condition is fog?

# In[ ]:





# In[94]:


df[df['Weather Condition']=='Fog']


# # Q14_-Find all insetence when 'Weather is clear 'or 'visibility'is above =40

# In[99]:


df[(df['Weather Condition']=='Clear')| (df['Visibility_km']>40)]


# In[ ]:




