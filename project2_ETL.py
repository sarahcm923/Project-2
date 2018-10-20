
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import os
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()


# In[2]:


review_file = "google-play-store-apps/googleplaystore_user_reviews.csv"
review_df = pd.read_csv(review_file)
review_df.head()


# In[3]:


app_file = "google-play-store-apps/googleplaystore.csv"
app_df = pd.read_csv(app_file)
app_df.head()


# In[4]:


merge_df = pd.merge(app_df, review_df, on="App")
merge_df.head()


# In[5]:


drop_columns = ["Size",'Content Rating','Genres','Last Updated', 'Sentiment_Polarity','Sentiment_Subjectivity']
clean_df = merge_df.drop(drop_columns, axis=1)
clean_df.head()


# In[6]:


clean_df = clean_df.dropna()
clean_df.count()


# In[7]:


import mysql.connector

database= mysql.connector.connect(
  host="localhost",
  user ="root",
  passwd ="Hazel2me$$"
)

mycursor = database.cursor()

mycursor.execute("CREATE DATABASE google2")



# In[8]:


engine = create_engine("mysql://root:Hazel2me$$@localhost:3306/google2")


# In[9]:


conn = engine.connect()


# In[10]:
print("--------------------")

final_db = clean_df.to_sql("test", conn, if_exists="replace")

print("--------------------")

# In[ ]:


data = engine.execute("SELECT * FROM test LIMIT 5")

