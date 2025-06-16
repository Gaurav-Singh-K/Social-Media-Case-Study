#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[2]:


# your code here


# In[116]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


# In[117]:


categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']


# In[118]:


likes = np.random.randint(0, 10000, size= 1000)


# In[119]:


dates = pd.date_range('2025--01-01', periods= 1000)


# In[120]:


category = [random.choice(categories) for i in range(1000)]


# In[121]:


data = dict({'Date':dates,
              'Category': category,
             'No. of likes' : likes
            })


# In[122]:


df = pd.DataFrame(data)


# In[123]:


df.head()


# In[124]:


df.info()


# In[125]:


df.describe()


# In[126]:


df['Category'].value_counts()


# In[127]:


df.dropna()


# In[128]:


df.info()


# In[129]:


sns.barplot(x = 'Category', y = 'No. of likes', data = df)
plt.xticks(rotation=45)  
plt.title("Average Likes per Category")


# In[130]:


print(sns.__version__)


# In[131]:


sns.boxplot('Category', 'No. of likes', data = df)


# In[132]:


df['No. of likes'].mean()


# In[133]:


df.groupby('Category')['No. of likes'].mean()


# In[139]:


max_likes_row = df[df['No. of likes'] == df['No. of likes'].max()]


print(max_likes_row[['Category', 'Date', 'No. of likes']])


# In[140]:


df.groupby('Category')['No. of likes'].max()


# In[141]:


# As per my case study I understand that the most viral or liked post comes through the category fashion.
# Maximum mean of likes is 5314.2 comes through the category family and minimum mean values is 4547 comes from the category music.
# Mean of all category is around equal. So Every type of post is valuable for the reference of the data.


# In[ ]:




