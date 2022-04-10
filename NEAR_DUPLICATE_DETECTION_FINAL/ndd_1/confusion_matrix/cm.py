#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[2]:


filename=input()


# In[3]:


l1=[]
with open(f"{filename}","r") as f:
    l1=f.readlines()


# In[4]:


l1


# In[5]:


l2=[]
for i in l1:
    l2.append(i.strip('\n'))
print(l2)


# In[6]:


print(len(l1[0]))


# In[7]:


l3=[]
for i in l2:
    l=list(i.split())
    l3.append(l)
print(l3)


# In[8]:


df=pd.DataFrame(l3)


# In[9]:


df


# In[10]:


df.rename(columns={1:'file_taken',2:'predicted_number_of_unique_pairs',3:'predicted_number_of_ndd_pairs',4:'time_taken'},inplace=True)


# In[11]:


df


# In[12]:


df['total_links']=[100,100,200,200,100,300,300,803]


# In[13]:


df


# In[14]:


df['uniqueness_percentage']=[100,50,100,50,80,100,50,100]


# In[15]:


df


# pd.to_numeric(df['number_of_unique_pairs'])
# pd.to_numeric(df['number_of_ndd_pairs'])

# In[16]:


df['total_pairs_considered']=pd.to_numeric(df['predicted_number_of_unique_pairs'])+pd.to_numeric(df['predicted_number_of_ndd_pairs'])


# In[17]:


df


# In[18]:


print(type(df.iat[1,3]))


# In[19]:


from sklearn.metrics import confusion_matrix


# In[20]:


list_of_conf_matrix=[]
import decimal as dc
for i in range(8):
    l_pred=[]
    l_pred.append(int(df['predicted_number_of_unique_pairs'][i]))
    l_pred.append(int(df['predicted_number_of_ndd_pairs'][i]))
    l_true=[]
    l_true.append(int(df['total_pairs_considered'][i])-int(df['uniqueness_percentage'][i])/100*int(df['total_links'][i]))
    l_true.append(int(df['uniqueness_percentage'][i])/100*int(df['total_links'][i]))
    conf_1=[str(min(l_pred[0],l_true[0])),str(max(0,l_true[0]-l_pred[0]))]
    conf_2=[str(max(0,l_true[1]-l_pred[1])),str(min(l_pred[1],l_true[1]))]
    a=np.array([conf_1,conf_2])
    list_of_conf_matrix.append(a)
    print(f"the confusion matrix for the {df['file_taken'][i]} is:")
    print(a)


# In[21]:


def final_table(cm):
    tp=float(cm[0][0])
    tn=float(cm[1][1])
    fp=float(cm[0][1])
    fn=float(cm[1][0])
#     print(tn)
    tot=tp+tn+fp+fn
    acc=(tp+tn)/(tot)
    err=(fp+fn)/(tot)
    sen=(tp)/(tp+fn)
    spe=(tn)/(tn+fp)
    ppv=(tp)/(tp+fp)
    npv=(tn)/(tn+fn)
    fpr=(fp)/(fp+tn)
    fnr=(fn)/(fn+tp)
    fdr=(fp)/(fp+tp)
    fomr=(fn)/(fn+tn)
    col1=['acc','err','sen','spe','ppv','npv','fpr','fnr','fdr','fomr']
    col2=[acc,err,sen,spe,ppv,npv,fpr,fnr,fdr,fomr]
    data=[]
    di={'acc':acc,'err':err,'sen':sen,'spe':spe,'ppv':ppv,'npv':npv,'fpr':fpr,'fnr':fnr,'fdr':fdr,'fomr':fomr}
    for i in range(len(col1)):
        l=[]
        l.append(col1[i])
        l.append(col2[i])
        data.append(l)
    df_local=pd.DataFrame(data,columns=['factor','ndd01_stemmed'])
#     df_local.rename(columns={0:'factor',1:'ndd01_stemmed'},inplace=True)
    return df_local


# In[22]:


list_of_final_dataframes=[]
for i in range(len(list_of_conf_matrix)):
    list_of_final_dataframes.append(final_table(list_of_conf_matrix[i]))
    print(list_of_final_dataframes[i])


# In[ ]:




