#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import and print the version of pandas
import pandas as pd
import numpy as np
print(pd.__version__)
# pd.show_versions()


# In[9]:


# Consider the following Python dictionary data and Python list labels:

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# (This is just some meaningless data I made up with the theme of animals and trips to a vet.)

# Create a DataFrame df from this dictionary data which has the index labels.

df = pd.DataFrame(data=data, index=labels)
df.info()


# In[11]:


# Return the first 3 rows of the DataFrame df.
df.head(3)


# In[13]:


# Select just the 'animal', 'age' and 'visits' columns from the DataFrame df.
df[['animal', 'age', 'visits']]


# In[16]:


# Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
df[['animal', 'age']].iloc[[3, 4, 8]]


# In[18]:


# Select only the rows where the number of visits is greater than 3.
df[df["visits"]>2]


# In[20]:


# Select the rows where the age is missing, i.e. it is NaN.
df[df.age.isna()]


# In[23]:


# Select the rows where the animal is a cat and the age is less than 3.
df[(df.animal == "cat") & (df.age < 3)]


# In[24]:


# Select the rows the age is between 2 and 4 (inclusive).
df[(df.age <=4) & (df.age >=2)]


# In[25]:


# Change the age in row 'f' to 1.5.
df.loc['f', 'age']= 1.5


# In[27]:





# In[31]:


# Calculate the sum of all visits in df (i.e. find the total number of visits).
df.sum()['visits']


# In[32]:


# Calculate the mean age for each different animal in df.
df.groupby('animal')['age'].agg('mean')


# In[38]:


# Append a new row 'k' to df with new values for each column. Then delete that row to return the original DataFrame.
df.loc['k']= ['beer', 4, 0, 'no']
df.loc['k', 'visits'] = 4


# In[41]:


df.drop(index=['k'], inplace=True)
df


# In[42]:


#Count the number of each type of animal in df
df.groupby('animal')['animal'].agg('count')


# In[45]:


# Sort df first by the values in the 'age' in decending order, 
# then by the value in the 'visits' column in ascending order (so row i should be first, and row d should be last).
df.sort_values(by=['age', 'visits'], ascending=[0, 1])


# In[ ]:





# In[ ]:




