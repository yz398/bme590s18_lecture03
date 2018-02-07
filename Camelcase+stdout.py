
# coding: utf-8

# In[ ]:


def CamelCase(file):
    m=0
    n=0
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        column = [row[4] for row in reader]
        for i in range(len(column)):
            s = column[i]
            if s.isupper():
                m = 0
            elif s.islower():
                m = 0
            elif s.istitle():
                m = 0
            else:
                m = 1
            if m >0:
                n = n+1
            
    return n

a = CamelCase('everyone.csv')

import sys
print('number of CamelCase:',a,file=sys.stdout)  

