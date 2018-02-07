
# coding: utf-8

# In[ ]:


def spacecheck(file):
    m = 0
    n = 0
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        column = [row[4] for row in reader]
        for i in range(len(column)):
            s = column[i]
            for index in s:
                if index.isspace():
                    m = m+1
            if m > 0:
                n = n+1
    return n


a = spacecheck('everyone.csv')
print(a)   

