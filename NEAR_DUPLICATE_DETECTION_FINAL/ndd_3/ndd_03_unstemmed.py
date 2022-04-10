#!/usr/bin/env python
# coding: utf-8

# In[1]:


filename=input()


# In[2]:


import pandas as pd
import numpy as np
import string

data=pd.read_excel(filename)
# print(data[['linkk']]) 
df=pd.DataFrame(data)
# dfs=df['linkk']
print(df['links'][0])
num_of_links=df.shape[0]


# In[3]:


import time
start_time = time.time()


# In[4]:


def print_string(l1):
    s_0=""
    for i in range(len(l1)):
        s_0+=l1[i]
        s_0+=" "
    print(s_0)


# In[5]:


import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()

project_words=[]
url_hash_list=[]
def project_ndd(url):
    r = requests.get(url)		# r variable has all the HTML code
    htmlContent = r.content	# r returns response so if we want the code we write r.content
    soup = BeautifulSoup(r.content, 'html.parser')
    s1=""
    for i in soup.find_all("p"):
        a=(i.text)
        s1+=(i.text)
    l=list(s1.split())
#     print(len(l))    
    punc='''!()-[]{};:'"\,<>./?@#$%^&*_~”’“‘|'''
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
            l[x]=" "
#         l[x]=ps.stem(l[x])
    s_inf=""
    for x in l:
        s_inf+=(x)
        s_inf+=" "
#     print(s_inf)         
    list_of_words=list(s_inf.split())
    list_stemmed=[]
    list_unstemmed=[]
    for i in list_of_words:
        list_stemmed.append(ps.stem(i))
#     print_string(list_stemmed)
    list_of_hash=[]
    for i in list_stemmed:
        HASHVALUE=hash(i)
        list_of_hash.append(HASHVALUE)
    # print(len(list_of_hash)) 
    url_hash_list.append(list((list_of_hash)))
    project_words.append(len(list_of_hash))
#     for i in list_of_hash:
#         print(i,end=" ")


# In[6]:


#brute force method
# s2="-1"
# while True:
#     url=input()
#     if url=="-1":
#         break
#     project_ndd(url)
# print(project_words)
# print(url_hash_list)

#using pandas data frame
for i in range(num_of_links):
    url=df['links'][i]
    project_ndd(url)
# print(project_words)
# print(url_hash_list)


# In[7]:


w_name=[]
for i in range(num_of_links):
    a1="w{}".format(i+1)
    w_name.append(a1)
# print(w_name)    


# In[8]:


total_words=0
for i in range(len(project_words)):
    total_words+=project_words[i]
count_of_unique=0
count_of_ndd=0
count_of_sus=0
def similarity_percentage(hash_list,count_of_unique,count_of_ndd,count_of_sus):
    final_score=[]
    sim_per=[]
    for i in range(len(url_hash_list)):
        ll1=[]
        for j in range(i+1,len(url_hash_list)):
            ll=[]
            if i==j:
                continue
            se=0
            ele=0
            for k in (url_hash_list[i]):
                for l in (url_hash_list[j]):
                    if l==k:
                        ele=1
                        break
                se+=ele
                ele=0
            fi_p=se/(len(url_hash_list[i])+len(url_hash_list[j]))
#             print(se,end=' ')
#             print(len(url_hash_list[i]),end=" ")
#             print(len(url_hash_list[j]))
            fi_p*=200
            ll.append(fi_p)
            ll.append(w_name[j])
            ll.append(w_name[i])
            if fi_p<=60:
                ll.append("unique")
                count_of_unique+=1
            elif fi_p>60 and fi_p<80:
                ll.append("suspicious")
                count_of_sus+=1
            elif fi_p>=80:
                ll.append("ndd")
                count_of_ndd+=1
            ll1.append(ll)   
        final_score.append(ll1)
    print("the number of unique pairs is: ",count_of_unique)
    print("the number of ndd pairs is: ",count_of_ndd)
    print("the number of suspicious pairs is: ",count_of_sus)
    with open("res1.txt","a") as f:
        s1=f"""{count_of_unique} """
        s2=f"""{count_of_ndd} """
        s21=f"""{count_of_sus}\n """
        s3=f"""{filename} """
        f.write("unstemmed ")
        f.write(s3)
        f.write(s1)
        f.write(s2)
        f.write(s21)
        f.write("%s\n" % (time.time() - start_time))
    return final_score


# In[9]:


fi_s=similarity_percentage(url_hash_list,count_of_unique,count_of_ndd,count_of_sus)
# print(set(fi_s)) 
l=[]
# for i in range(len(fi_s)):
#     print(fi_s[i])
#     print()


# In[10]:


# print(project_words)


# In[11]:


import xlwt
from xlwt import Workbook
wb = Workbook()
a=1
b=1
s=0
s1 = wb.add_sheet('s1',cell_overwrite_ok=True)
# for i in range(len(url_hash_list)):
# #     for j in range(len(url_hash_list[i])):
# #         sheet1.write(j,a,url_hash_list[i][j])
    
#     sheet1.write(s,0,b)
#     sheet1.write(s,2,project_words[i])
#     s+=1
#     b+=1
s1.write(1,0,"DOCUMENT_CONSIDERED")
s1.write(1,1,"DOCUMENT_COMPARED_AGAINST")
s1.write(1,2,"SIMILARITY_PERCENTAGE")
s1.write(1,3,"RESULT")
row=2
for i in range(len(fi_s)):
    for j in range(len(fi_s[i])):
        s1.write(row,0,fi_s[i][j][2])
        s1.write(row,1,fi_s[i][j][1])
        s1.write(row,2,fi_s[i][j][0])
        s1.write(row,3,fi_s[i][j][3])
        row+=1
wb.save("result"+filename)


# In[12]:


print("--- %s seconds ---" % (time.time() - start_time))


# In[13]:


# with open("res1.txt","a") as f:
# #     s1=f"""{count_of_unique} """
# #     s2=f"""{count_of_ndd} """
# #     s3=f"""{filename} """
# #     f.write("unstemmed ")
# #     f.write(s3)
# #     f.write(s1)
# #     f.write(s2)
#     f.write("%s\n" % (time.time() - start_time))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




