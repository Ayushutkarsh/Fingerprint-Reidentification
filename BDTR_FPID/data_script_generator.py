#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
kk={}
a = open("data_file_color.txt", "w")
b = open("data_file_thermal.txt", "w")
counter=1
cc=0
for path, subdirs, files in os.walk(r'/Users/ayush/projects/Visible-Thermal-Person-Re-Identification-master/BDTR/data_trial/test'):
    for filename in files:
        #print(filename)
        cc+=1
        f = os.path.join(path, filename)
        label_file = f.split('/')[-1]
        label_file=label_file.split('.')[0]
        print(label_file)
        k=label_file.split('_')
        print(k)
        label=k[0]+"_"+k[2]
        if label not in kk:
            kk[label]=counter
            counter+=1
        text_label =kk[label]   
        #print(label)
        a.write(str(f) +" "+ str(text_label)+ os.linesep) 
        b.write(str(f) +" "+ str(text_label)+ os.linesep)


# In[7]:


len(kk)
print(cc)


# In[5]:


get_ipython().system('rm /Users/ayush/projects/Visible-Thermal-Person-Re-Identification-master/BDTR/data_trial/test/.DS_Store')


# In[3]:


get_ipython().system('pip install tensorflow==1.11.0')


# In[2]:


import numpy as np
print(np.__version__)


# In[1]:


import tensorflow as tf


# In[2]:


tf.__version__


# In[4]:


get_ipython().system('python -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.14.0-py3-none-any.whl')


# In[3]:



get_ipython().system('pip install numpy --upgrade')


# In[1]:


import numpy as np


# In[ ]:




