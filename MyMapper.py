#!/usr/bin/env python
# coding: utf-8

# In[77]:


import json

with open('dblps.json', 'r') as infile:
    data = infile.read()
    new_data = data.replace('}\n{', '},{')
    json_data = json.loads(f'[{new_data}]')
    
    for data in json_data:
        for name in data['authors']:
            print (name,data['authors'].index(name)+1 , 1)
            


    
    

    
    


# In[ ]:




