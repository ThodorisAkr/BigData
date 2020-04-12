#!/usr/bin/env python
# coding: utf-8

# In[22]:


#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_pos = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.replace('(', "")
    line = line.replace(')', "")

    # parse the input we got from mapper.py
    word, pos, count = line.split(",",2)

    

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
    if (current_word == word and current_pos == pos):
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word,pos, current_count))
        current_count = count
        current_word = word
        current_pos = pos

# do not forget to output the last word if needed!
if (current_word == word ):
    print('%s\t%s\t%s' % (current_word,current_pos, current_count))





