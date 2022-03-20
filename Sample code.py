#!/usr/bin/env python
# coding: utf-8

# In[15]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    else:
        text.append(item)
print(number)
print(text)
assert len(number) == 4
assert len(text) == 13


# In[11]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float,str))):
        number.append(item)
    else:
        text.append(item)
print(number)
print(text)


# In[3]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    elif(isinstance(item,str)):
        res= item.replace('.',' ',1).isdigit()
        number.append(res)
    else:
        text.append(item)
print(number)
print(text)


# In[4]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
new_n = [int(g) for g in data]
print(new_n)
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    elif(isinstance(item,str)):
        res= item.replace('.',' ',1).isdigit()
        number.append(res)
    else:
        text.append(item)
print(number)
print(text)


# In[1]:


a='f'
type(a)


# In[2]:


b='5.45'
type(b)


# In[3]:


float(b)


# In[4]:


c='jaa'
type(c)


# In[6]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    elif(isinstance(item,str)):
        res= item.replace('.',' ',1)
        number.append(res)
    else:
        text.append(item)
print(number)
print(text)


# In[5]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    elif(item.isnumeric()):
        number.append(item)
    else:
        text.append(item)
print(number)
print(text)


# In[18]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        number.append(item)
    elif(isinstance(item,str)):
        res= item.replace(' ',' ',1)
        number.append(res)
    else:
        text.append(item)
print(number)
print(text)


# In[14]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float))):
        item=float(item)
        number.append(item)
    elif(item.isnumeric()):
        item=float(item)
        number.append(item)
    else:
        text.append(item)
print(number)
print(text)


# In[1]:


data= ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']
number=[];
text=[];
for item in data:
    if (isinstance(item,(int,float)) or item.isnumeric()):
        item= int(item)
        number.append(item)
    elif '.' in item:
        item=float(item)
        number.append(item)
    else:
        text.append(item)
print(number)
print(text)


# In[ ]:




