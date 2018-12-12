
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pylot as plt


# In[3]:


from matplotliv import pyplot as plt


# In[4]:


from matplotlib import pyplot as plt


# In[9]:


x = [1,2,3]
y = [1, 4, 9]
z = [10, 5,0]
plt.plot(x, y)
plt.plot(x , z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[10]:


sample_data = pd.read_csv('sample_data.csv')


# In[11]:


sample_data


# In[12]:


type(sample_data)


# In[15]:


sample_data.column_c.iloc[2]


# In[18]:


plt.plot(sample_data.column_a, sample_data.column_b, "o")
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()


# In[19]:


data = pd.read_csv("countries.csv")


# In[20]:


data


# In[21]:


#compare the population growth in the US and China


# In[23]:


us = data[data.country == "United States"]


# In[31]:


china = data[data.country == "China"]


# In[32]:


china


# In[30]:


us


# In[36]:


plt.plot(us.year, us.population /10**6)
plt.plot(china.year, china.population /10**6)
plt.legend(['United States', 'China'])
plt.xlabel("year")
plt.ylabel("population")
plt.show()


# In[37]:


us.population


# In[40]:


us.population / us.population.iloc[0] * 100


# In[41]:


plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel("year")
plt.ylabel("population growth (first year = 100)")
plt.show()

