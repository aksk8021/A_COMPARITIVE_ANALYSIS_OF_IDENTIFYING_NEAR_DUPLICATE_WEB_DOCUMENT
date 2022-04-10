#!/usr/bin/env python
# coding: utf-8

# In[4]:


filename=input()


# In[5]:


import requests
from bs4 import BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np


# In[6]:


data=pd.read_excel(filename)
# print(data[['linkk']]) 
df=pd.DataFrame(data)
# dfs=df['linkk']
print(df['links'][0])
num_of_links=df.shape[0]
l_names=[]
l_w_name=[]


# In[40]:


def validating_idiots(url):
    r = requests.get(url)# r variable has all the HTML code
    htmlContent = r.content# r returns response so if we want the code we write r.content
    #print(htmlContent)
    soup = BeautifulSoup(r.content, 'html.parser')
    s1=""
    for i in soup.find_all('p'):
        a=(i.text)
        s1+=(i.text)
    l1=list(s1.split())
    return l1[:400]


# In[41]:


l2=[]
for i in range(num_of_links):
    url=df['links'][i]
    l_w_name.append(f"w{i+1}")
    l2.append(validating_idiots(url))


# In[42]:


print(len(l2[0]))
print(len(l2[1]))


# In[43]:


with open("res.txt","a") as f:
    
    for i in range(len(l2)):
        for j in range(len(l2)):
            if i==j:
                continue
            alpha=False
            if l2[i]==l2[j]:
                alpha=True
            if alpha:
                s1=f"""{df['links'][i]}\n"""
                s2=f"""{df['links'][j]}\n\n"""
#                 print(l2[i])
#                 print(l2[j])
#                 print(l_w_name[i],end=" ")
#                 print(l_w_name[j],end=" ")
#                 print(df['links'][i])
#                 print(df['links'][j])
                print()
                f.write(s1)
                f.write(s2)


# In[26]:


# for i in range(len(l2)):
#     print(l2[i])
#     print()


# In[ ]:





# In[ ]:




