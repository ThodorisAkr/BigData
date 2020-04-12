#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    newLine = json.loads(line)
    
    for key,value in newLine.items():
        if(key =='authors'):
            for name in value:
                print(name,value.index(name)+1 , 1)
    






