import requests
import pandas as pd

base_url = 'https://gorest.co.in/public/v2/todos'
resp = requests.get(base_url)
data = resp.json()

#print(type(data))

data1 = []
for items in data:
    d = {}
    d['id'] = items['id']
    try:
        d['user_id'] = items['user_id']
    except:
        d['user_id'] = None
    d['title'] = items['title']
    d['due_on'] = items['due_on']
    d['status'] = items['status']
    data1.append(d)
d = pd.DataFrame(data1)
d.to_csv('E:\Internship\detailsfile.csv')