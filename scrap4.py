import requests
import json
from bs4 import BeautifulSoup
with open("first_task.json","r") as f:
    a=json.load(f)
    i=0
    u=[]
    while i<len(a):
        print(i+1,":",a[i]["name"])
        u.append(a[i]["url"])
        i=i+1
    user=int(input("Please enter the serial number:-"))-1
    x=u[user]
    b=requests.get(x)
    soup=BeautifulSoup(b.text,"html.parser")
    c=soup.find('script',type='application/ld+json').text
    a=json.loads(c)
    with open("task4_detail.json","w") as f:
        json.dump(a,f,indent=2)
    with open("task4_detail.json","r") as k:
        r=json.load(k)      
    d={}
    for j in r:
        d['movie']=r['name']
        d['director']=[r['director'][0]['name']]
        d['image']=r['image']
        d['description']=r['description']
        d["language"]=r['review']['inLanguage']
        d['genre']=r['genre']
        d['Runtime']=r['duration']
        d['country']='india'
    with open("forth_task.json","w") as f:
        json.dump(d,f,indent=4)
    print(r)
                                                                                       
    