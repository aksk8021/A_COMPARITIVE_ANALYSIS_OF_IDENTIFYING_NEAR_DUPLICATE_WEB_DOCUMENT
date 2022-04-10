#!/usr/bin/env python
# coding: utf-8

# In[39]:


filename=input()


# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()


# In[ ]:


import time
start_time = time.time()


# In[ ]:


data=pd.read_excel(filename)
# print(data[['linkk']]) 
df=pd.DataFrame(data)
# dfs=df['linkk']
print(df['links'][0])
num_of_links=df.shape[0]
l_names=[]
l_w_name=[]


# In[ ]:


def project_ndd1(url):
    r = requests.get(url)# r variable has all the HTML code
    htmlContent = r.content# r returns response so if we want the code we write r.content
    #print(htmlContent)
    soup = BeautifulSoup(r.content, 'html.parser')
    s1=""
    for i in soup.find_all('p'):
        a=(i.text)
        s1+=(i.text)
    # print(a) 
    # s1.strip()  
    while "\n" in s1:
        s1=s1.replace("\n"," ")
    while "     " in s1:
        s1=s1.replace("     "," ")
    while "    " in s1:
        s1=s1.replace("    "," ")    
    punc='''!()-[]{};:'"\,<>./?@#$%^&*_~”’“‘|—•'''
    stop_word=["a","the","an","is"]
    for ele in s1:
        if ele in punc:
            s1 = s1.replace(ele, " ")
    no_of_words=list(s1.split())
#     print(len(no_of_words)) 
    s2=""
    for i in no_of_words:
        s2+=i
        s2+=" "
#     print(s2)
    stop_words = stopwords.words('english')
    l=list(s2.split())
    for x in range(len(l)):
        if l[x] in stop_words:
            l[x]=""
    s_inf=""
    for x in l:
        s_inf+=ps.stem(x)
        s_inf+=" "     
    #print(s_inf)   
    di={}
    for x in range(len(l)):
        b=l[x].lower()
        if b=="" or b.isnumeric():
            continue
        a=l.count(b)
        di[b]=a
#     print(di)
    def get_value(tp):
        return di[tp] 
    l=[]
    i=1
    for x in sorted(di,key=get_value, reverse=True):
        ll=[]
        ll.append(i)
        ll.append(x)
        ll.append(di[x])
        l.append(ll)
        i+=1
#     print(l)
    #data=pd.DataFrame(l)
    #df=data.iloc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
#     ll=[]
#     for i in range(15):
#         ll.append(l[i])
    return l[:15]


# In[ ]:


#brute force/manual entering
# l1=[]
# while True:
#     ll=[]
#     s=input()
#     if s=="-1":
#         break
# #     ll.append(project_ndd1(s))
#     #l1.append(ll)
#     l1.append(project_ndd1(s))
# print(l1)   

l1=[]
for i in range(num_of_links):
    url=df['links'][i]
    l_w_name.append(f"w{i+1}")
    l1.append(project_ndd1(url))


# In[ ]:


# print(l1) 
# df=pd.DataFrame(l1)
df.rename(columns={0:'T_IND',1:'WORD',2:'COUNT'},inplace=True)
list_of_dfs=[]
diff_df_t1=[]
diff_df_t2=[]
print(df) 
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if i==j:
            continue
        ll1=[]
        ll2=[]
        ll1_ig=[]
        ll2_ig=[]
        for k in range(len(l1[i])):
            for l in range(len(l1[j])):
                if l1[i][k][1]==l1[j][l][1]:
                    ll1.append(l1[i][k])
                    ll1_ig.append(k)
                    ll2.append(l1[j][l])
                    ll2_ig.append(l)
        df1=pd.DataFrame(ll1)
        df1.rename(columns={0:f'T_IND{i}',1:'WORD',2:'COUNT'},inplace=True)
        df2=pd.DataFrame(ll2)
        df2.rename(columns={0:f'T_IND{j}',1:'WORD',2:'COUNT'},inplace=True)
        frames=[df1,df2]
        result = pd.concat(frames, axis=1, join='inner')
        list_of_dfs.append(result)
        l_diff_t1=[]
        l_diff_t2=[]
        for q in range(len(l1[i])):
            if q not in ll1_ig:
                l_diff_t1.append(l1[i][q])
        for r in range(len(l1[j])):
            if r not in ll2_ig:
                l_diff_t2.append(l1[j][r])  
        df3=pd.DataFrame(l_diff_t1)
        df3.rename(columns={0:'T_IND',1:'WORD',2:'COUNT'},inplace=True)
        df4=pd.DataFrame(l_diff_t2)
        df4.rename(columns={0:'T_IND',1:'WORD',2:'COUNT'},inplace=True)
        diff_df_t1.append(df3)
        diff_df_t2.append(df4) 
        v_1=l_w_name[i]
        v_2=l_w_name[j]
        lll=[v_1,v_2]
        l_names.append(lll)


# In[ ]:


# print(list_of_dfs[0])
# # df_prime=pd.DataFrame(list_of_dfs[0])
print(diff_df_t1)
print(diff_df_t2)


# In[ ]:


import math
df_incl_sdc=[]
for i in range(len(list_of_dfs)):
    local_df=pd.DataFrame(list_of_dfs[i])
    ll_sdc=[]
    for j in range(len(list_of_dfs[i])):
        val1=math.log(local_df.iat[j,2]/local_df.iat[j,5],10)
        val2=abs(1+local_df.iat[j,0]-local_df.iat[j,3])
        l_sdc=val1*val2
        ll_sdc.append(l_sdc)
    ll_sdc_df=pd.DataFrame(ll_sdc)
    df_ele= pd.concat([local_df,ll_sdc_df], axis=1, join='inner')
    df_ele.rename(columns={0:'SDC_VAL'},inplace=True)
    df_incl_sdc.append(df_ele)


# In[ ]:


df_incl_sdt_t1=[]
for i in range(len(diff_df_t1)):
    local_diff=pd.DataFrame(diff_df_t1[i])
    ll_sdt=[]
    alpha= local_diff.shape[0]
    for j in range(alpha):
        if local_diff.iat[j,2]==0:
            continue
        val=math.log(local_diff.iat[j,2],10)*16
        ll_sdt.append(val)
    sdt_df=pd.DataFrame(ll_sdt)
    df_sdt= pd.concat([local_diff,sdt_df], axis=1, join='inner')
    df_sdt.rename(columns={0:'SDT1_VAL'},inplace=True)
    df_incl_sdt_t1.append(df_sdt)


# In[ ]:


# df_incl_sdt_t1


# In[ ]:


df_incl_sdt_t2=[]
for i in range(len(diff_df_t2)):
    local_diff=pd.DataFrame(diff_df_t2[i])
    ll_sdt=[]
    alpha= local_diff.shape[0]
    for j in range(alpha):
#         print(local_diff.iat[j,2])
        val=math.log(abs(local_diff.iat[j,2])+1,10)*16
        ll_sdt.append(val)
    sdt_df=pd.DataFrame(ll_sdt)
    df_sdt= pd.concat([local_diff,sdt_df], axis=1, join='inner')
    df_sdt.rename(columns={0:'SDT2_VAL'},inplace=True)
    df_incl_sdt_t2.append(df_sdt)


# In[ ]:


# df_incl_sdt_t2


# In[ ]:


# df_incl_sdt_t2[9]['SDT2_VAL'].sum()


# In[ ]:


count_of_unique=0
count_of_ndd=0
for i in range(len(df_incl_sdc)):
    df_1=pd.DataFrame(df_incl_sdc[i])
    df_2=pd.DataFrame(df_incl_sdt_t1[i])
    df_3=pd.DataFrame(df_incl_sdt_t2[i])
    if df_1.empty and not df_3.empty and not df_2.empty:
#         print(df_3)
#         print(df_2['SDT1_VAL'])
        ssm=df_2['SDT1_VAL'].sum()+df_3['SDT2_VAL'].sum()
    
    elif df_2.empty and not df_3.empty and not df_1.empty:
#         print(df_3)
        ssm=df_1['SDC_VAL'].sum()+df_3['SDT2_VAL'].sum()
    
    elif df_3.empty and not df_2.empty and not df_1.empty:
#         print(df_3)
        ssm=df_1['SDC_VAL'].sum()+df_2['SDT1_VAL'].sum()
    
    elif df_2.empty and df_3.empty:
        ssm=df_1['SDC_VAL'].sum()
        
    elif df_1.empty and df_2.empty:
        ssm=df_3['SDT2_VAL'].sum()
        
    elif df_1.empty and df_3.empty:
        ssm=df_2['SDT1_VAL'].sum()
        
    else:
#         print(df_3)
        ssm=df_1['SDC_VAL'].sum()+df_2['SDT1_VAL'].sum()+df_3['SDT2_VAL'].sum()
    ssm/=15
    print("AFTER CALCULATION THE SSM IS {} for the datasets {}".format(ssm,l_names[i]))
    if ssm<19.50:
        print("NDD")
        count_of_ndd+=1
    elif ssm>=19.50:
        print("UNIQUE")
        count_of_unique+=1


# In[ ]:


print("the number of unique pairs is: ",count_of_unique)
print("the number of ndd pairs is: ",count_of_ndd)


# In[ ]:


with open("res.txt","a") as f:
    s1=f"""{count_of_unique} """
    s2=f"""{count_of_ndd} """
    s3=f"""{filename} """
    f.write("stemmed ")
    f.write(s3)
    f.write(s1)
    f.write(s2)
    f.write("%s\n" % (time.time() - start_time))


# In[ ]:


print("--- %s seconds ---" % (time.time() - start_time))


# In[ ]:





# In[ ]:




