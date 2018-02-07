
# coding: utf-8

# In[6]:


cd d:/2018spring/device python/git/Git/b


# In[7]:


get_ipython().magic('cd d:/2018spring/device python/git/Git/b')


# In[8]:


cd d:/2018spring/device python/git/Git/b


# In[9]:


import glob
x = glob.glob("*.csv")
print(x)


# In[5]:


cd d:/2018spring/device python/git/Git/bme590s18_lecture03


# In[10]:


import glob
x = glob.glob("*.csv")
print(x)
x[0]


# In[10]:


import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')


# In[34]:


import csv
with open('yz398.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# In[46]:


import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
for i in range(len(x)-1):
    with open(x[i],'ab') as f:
        f.write(open(x[i+1],'rb').read())
    x[i+1] = x[i]


# In[25]:





# In[40]:


with open('yz398.csv','ab') as f:
        f.write(open('zk28.csv','rb').read())


# In[43]:


import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
for i in range(len(x)-1):
    with open('x[i]','ab') as f:
        f.write(open('x[i+1]','rb').read())
        x[i+1] = x[i]


# In[49]:


import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
a = len(x)
for i in range(a-1):
    with open(x[i],'ab') as f:
        f.write(open(x[i+1],'rb').read())
    x[i+1] = x[i]


# In[1]:


cfile = open('everyone.csv', 'w')
import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
a = len(x)
for i in range(a):
    with open('everyone.csv','ab') as f:
        f.writerow(open(x[i],'rb').read())


# In[57]:


import csv
with open('', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# In[2]:


cd d:/2018spring/device python/git/Git/bme590s18_lecture03


# In[9]:


cfile = open('everyone.csv', 'w')
import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
a = len(x)
for i in range(a):
    with open('everyone.csv','a+') as f:
        f.write(open(x[i],'rb').read())


# In[1]:



    


# In[5]:


import csv
with open('gja8.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# In[65]:


cfile = open('everyone.csv', 'w')
import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
a = len(x)
for i in range(a):
    with open('everyone.csv','ab') as f:
        f.write(open(x[i],'rb').read())


# In[11]:


cd d:/2018spring/device python/git/Git/bme590s18_lecture03


# In[24]:


cfile = open('everyone.csv', 'w')
import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
a = len(x)
for i in range(a):
    with open('everyone.csv','a+') as f:
        f.writeline(open(x[i],'r+').read())


# In[43]:


import csv
reader = csv.reader(open('yz398.csv','rb'))
for row in reader:
    print(row)


# In[34]:


str ='yz'
print(str)


# In[44]:


import csv
 
def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        #title = reader.fieldnames
        for row in reader:
            #csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        return csv_rows
 
print read_csv('yz398.csv')


# In[47]:


import csv
with open('yz398.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
print(rows)


# In[49]:


import csv
with open('yz398.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]
print(rows)


# In[50]:


with open('yz398.csv') as l1:
    str = l1.read()
print(str)


# In[62]:


import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
a = len(x)
for i in range(a):
    with open(x[i]) as l1:
        rows = l1.read()
    with open('everyone.csv','w') as f:
         f_csv = csv.writer(f)
         f_csv.writer(rows)


# In[74]:


with open('yz398.csv','r') as db01:
    reader = csv.reader(db01)  
    column = [row[0] for row in reader]  
    a =column[1]
print(a)


# In[48]:


cd d:/2018spring/device python/git/Git/bme590s18_lecture03


# In[92]:


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


# In[93]:


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

a = CamelCase('test.csv')

import sys
sys.stdout.write(a) 

                
                


# In[82]:


cfile = open('everyone.csv', 'w')
testcsv=open('test.csv','w')
import glob
x = glob.glob("*.csv")
x.remove('mlp6.csv')
x.remove('everyone.csv')
x.remove('test.csv')
a = len(x)

for i in range(a):
    with open('everyone.csv','ab') as f:
        
        templine=open(x[i],'rb').read()
        dfile = open(x[i],'w')
       # print('----------',templine)
        templine=templine.decode('utf-8-sig')
        templine=templine.strip()
       # print(templine)

        if '\xef\xbb\xbf'  in templine:
            templine=templine.replace('\xef\xbb\xbf','')

        if '#' in templine:
            #print('--------\n',templine)
            templine=templine.split('\n')[1]
            #print(templine,'\n---------')

        if '\n' not in templine:
            print(templine)
            templine+='\n'

        #print('newline:',templine)
        #f.write(open(x[i],'rb').read())
        cfile.write(templine)
        dfile.write(templine)
cfile.close()


# In[83]:


import csv
import json
 
def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = ['lastname','firstname','netid','githubname','teamname']
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        return csv_rows
 
def write_json(data, json_file, format=None):
    with open(json_file, "w") as f:
        if format == "good":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
        else:
            f.write(json.dumps(data))
for i in range(len(x)):          
    a = x[i]
    b = a.replace('.csv','.json')
    write_json(read_csv(a),b, 'good')

