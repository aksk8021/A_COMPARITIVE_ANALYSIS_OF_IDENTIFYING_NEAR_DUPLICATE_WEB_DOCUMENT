#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[19]:


filename=input()


# In[20]:


l1=[]
with open(f"{filename}","r") as f:
    l1=f.readlines()


# In[21]:


l1


# In[22]:


l2=[]
for i in l1:
    l2.append(i.strip('\n'))
print(l2)


# In[23]:


print(len(l1[0]))


# In[24]:


l3=[]
for i in l2:
    l=list(i.split())
    l3.append(l)
print(l3)


# In[25]:


df=pd.DataFrame(l3)


# In[26]:


df


# In[27]:


df.rename(columns={1:'file_taken',2:'predicted_number_of_unique_pairs',3:'predicted_number_of_ndd_pairs',4:'suspicious', 5:'time_taken'},inplace=True)


# In[28]:


df


# In[29]:


df['total_links']=[100,100,100,200,200,300,300]


# In[ ]:


df['uniqueness_percentage']=[100,50,80,100,50,50,100]


# In[ ]:


df['total_pairs_considered']=pd.to_numeric(df['predicted_number_of_unique_pairs'])+pd.to_numeric(df['predicted_number_of_ndd_pairs'])+pd.to_numeric(df['suspicious'])


# In[ ]:


list_of_conf_matrix=[]
import decimal as dc
for i in range(7):
    l_pred=[]
    l_pred.append(int(df['predicted_number_of_unique_pairs'][i])+int(df['suspicious'][i]))
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


# In[ ]:


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


# In[ ]:


list_of_final_dataframes=[]
for i in range(len(list_of_conf_matrix)):
    list_of_final_dataframes.append(final_table(list_of_conf_matrix[i]))
    print(list_of_final_dataframes[i])


# In[ ]:




