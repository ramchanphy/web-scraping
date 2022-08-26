import json
with open("second_task.json","r")as file:
    year=json.load(file)
    def group_by_year():
        y=1950
        dic={}
        for i in range(1950,2022,10):
            b=[]
            for j in year:
                if y<int(j) and int(j)<(y+10):
                    b.append(year[j])
            dic[y]=b
            y+=10
        with open("third_task.json","w") as f:
            json.dump(dic,f,indent=4)
    group_by_year()
            

