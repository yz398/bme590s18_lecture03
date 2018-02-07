
# coding: utf-8

# In[ ]:


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

