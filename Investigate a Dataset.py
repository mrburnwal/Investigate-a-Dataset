#!/usr/bin/env python
# coding: utf-8

# # Project : IMDB Movies Data Analysis

# In[2]:


#importing necessary and useful libraries.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#we will be using IMDB Movies Data for this process
#printing first 5 rows of the Dataset.

df=pd.read_csv('tmdb-movies.csv')
df.head()


# In[4]:


#listing down all columns name

for i in df.columns:
    print(i)


# In[5]:


#dropping down unnecessary columns for this project

df.drop(['id','imdb_id','budget','revenue','original_title','cast','homepage','director','tagline','keywords','overview','production_companies','release_date','vote_count'],axis=1,inplace=True)
df.head()


# In[6]:


#printing shape of the dataframe after dropping columns 

df.shape


# In[7]:


#information about dataframe (Datatypes and null values)

df.info()


# In[8]:


#sum of total null values from each columns

df.isnull().sum()


# In[9]:


#dropping down all null values and fix it in original dataframe

df.dropna(inplace=True)
df.head()


# # Research Question 1:
# 
# ## Is runtime increasing with year ?
# 
# ## For this sum of runtime has been calculated and then plotted the graph against release year.

# In[10]:


#generating a Bar Plot of sum of runtime against release_year


plt.xlabel('Release_year',fontsize=20)
plt.ylabel('in minutes',fontsize=20)
plt.title('Runtime Over Year',fontsize=30)
df.groupby('release_year')['runtime'].sum().plot(kind='bar',figsize=(30,8))


# # Research Question 2:
# 
# ## Is number of movies released per year is increasing over the year?
# 
# ## For this sum of movies per year has been calculated using value_counts() function and then plotted using Bar Plot.

# In[11]:


#generating a Bar Plot of number of movies released per year against release year

plt.xlabel('release_year',fontsize=20)
plt.ylabel('No. Of Movies',fontsize=20)
plt.title('No. of Movies released Over Year',fontsize=30)
df.release_year.value_counts().sort_index().plot(kind='bar',figsize=(30,8))


# In[12]:


#splitting the genre value that were connected with | in the dataframe and printing value

df_genres = df['genres'].str.split('|', expand=True)
print(df['genres'])
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(df_genres)


# # Research Question 3:
# 
# ## What are popular genres of movies?
# 
# ## for this we plotted the sum of genres in Pie Chart with percentage value after extracting the data from Genres column.

# In[13]:


#printing popular genres in Pie Plot

plt.title('Popular Genre in Pie Plot',fontsize=30)
(df_genres[0].value_counts()+df_genres[1].value_counts()+df_genres[2].value_counts()+df_genres[3].value_counts()+df_genres[4].value_counts()).plot(kind='pie',figsize=(10,10),autopct='%1.1f%%')
plt.show()


# In[14]:


#adding a profit column in dataframe

df['profit']=df['revenue_adj']-df['budget_adj']
df.head()


# # Research Question 4:
# 
# ## Is profit increasing over the years?
# 
# ## for this question's solution, a new column of profit has been created by substracting revenue with budget and then plotted in Line Plot.

# In[15]:


#ploting a Line plot of profit over year against release year

plt.title('Profit Over Year',fontsize=30)
plt.xlabel('Profit in USD',fontsize=20)
plt.ylabel('Release_Year',fontsize=20)
df.groupby('release_year')['profit'].sum().plot(kind='line',figsize=(30,8))


# # Conclusion:
# 
# ## 1. Runtime is continously increasing over the years. 
# ## 2. More number of movies are releasing per year. (Satisfying conclusion 1)
# ## 3. Drama, Comedy, Thriller and Action are most popular genres with 18%, 14.3%, 11% and 9% of share in total sum of genre.
# ## 4. Profit over the years is continously increasing. 
# 
# ### More numbers of movies are releasing per year, increasing more runtime, more profit per year.
# 
# ## P.S. Project is based on data till 2015 and irregularity in plots may be due to missing data.

# # Thank You
