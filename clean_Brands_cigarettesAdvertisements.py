
# coding: utf-8

# In[17]:

get_ipython().magic('matplotlib inline')
import csv
import collections
import pprint
import sys
import pandas as pd
import matplot


# In[2]:

csv.field_size_limit(sys.maxsize)


# In[51]:

main_file = "all.csv" #load_export


# In[52]:

df = pd.read_csv(main_file, header=0, sep='\t')
#data = data.set_index(pd.DatetimeIndex(data['paper_dc_date']))


# In[54]:

df['paper_dc_title'] = df['paper_dc_title'].apply(lambda x: x.split(':')[0]) #strip cell after :
df['paper_dc_title'] = df['paper_dc_title'].apply(lambda x: x.split('/')[0]) #strip cell after /
df['paper_dc_title'] = df['paper_dc_title'].str.lower().str.replace('ĳ', 'ij') #fix error with ij
df['text_content'] = df['text_content'].str.lower() #lower-case text content


# In[55]:

df = df[df['text_content'].str.contains("bruin") == False] #words related to Camel
df = df[df['text_content'].str.contains("wit") == False]
df = df[df['text_content'].str.contains("zwart") == False]
df = df[df['text_content'].str.contains("kleuren") == False]
df = df[df['text_content'].str.contains("grijs") == False]
df = df[df['text_content'].str.contains("groen") == False]
df = df[df['text_content'].str.contains("beige") == False]
df = df[df['text_content'].str.contains("marine") == False]
df = df[df['text_content'].str.contains("tweed") == False]
df = df[df['text_content'].str.contains("tweed") == False]
df = df[df['text_content'].str.contains("mantel") == False]
df = df[df['text_content'].str.contains("katoen") == False]
df = df[df['text_content'].str.contains("mantels") == False]
df = df[df['text_content'].str.contains("maten") == False]


# In[56]:

df = df[df['text_content'].str.contains("theater") == False] #words related to Roxy
df = df[df['text_content'].str.contains("geleen") == False]


# In[58]:

df.to_csv('Brands_cleanUp.csv', index=False) #export to csv

