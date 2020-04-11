#!/usr/bin/env python
# coding: utf-8

# In[22]:


#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in open('untitled.txt',encoding = 'utf-8'):
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, pos, count = line.split("'",3)

    

    # convert count (currently a string) to int
    try:
        count = int(count)
        pos = int(pos)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word,pos, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s\t%s' % (current_word,pos, current_count))


# In[ ]:





# In[ ]:




