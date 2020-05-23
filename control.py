#!/usr/bin/env python
# coding: utf-8

# In[63]:


with open('assignment_code/controller.py') as infile:
    a=eval(infile.read())


# In[64]:


if a in range(1,4):
    with open('assignment_code/new_convolve.py', 'w') as outfile: 
        for j in range(1,a+1): 
            with open('assignment_code/convolve.py') as infile: 
                outfile.write(infile.read()) 
            outfile.write("\n") 
    with open('assignment_code/controller.py','w') as outfile:
        outfile.write(str(a+1))
        
elif a in range(4,7):        
       with open('assignment_code/new_dense.py', 'w') as outfile: 
        for j in range(4,a+1): 
            with open('assignment_code/dense.py') as infile: 
                outfile.write(infile.read()) 
            outfile.write("\n") 
        with open('assignment_code/controller.py','w') as outfile:
            outfile.write(str(a+1))


# In[4]:


filenames = ['assignment_code/import.py', 'assignment_code/input.py','assignment_code/new_convolve.py','assignment_code/flatten.py','assignment_code/new_dense.py','assignment_code/output.py'] 
with open('file3.py', 'w') as outfile: 
    for names in filenames: 
        with open(names) as infile: 
            outfile.write(infile.read()) 
        outfile.write("\n") 


# In[ ]:




