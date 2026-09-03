#!/usr/bin/env python
# coding: utf-8

# In[14]:


#python program tht accepts integer n and compute the value of n+nn+nnn
n=int(input("Enter the value of n:"))
nn=n*11
nnn=n*111
result=n+nn+nnn
print(n,"+",nn,"+",nnn,"=",result)


# In[19]:


#area of circle
import math
r=float(input("Enter the radius of a circle:"))
area=math.pi*r*r
print(f"{area=:.2f}")


# In[20]:


#biggest of three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
biggest=max(a,b,c)
print("Biggest number is:",biggest)


# In[ ]:




