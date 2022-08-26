import json
with open("first_task.json","r") as f:
    movie=json.load(f)
    def group_by_year():
        d={}
        for i in movie:
            movie_list=[]
            year=i["year"]
            # i+=1
            if year not in d:
                for j in movie:
                    if year==j["year"]:
                        movie_list.append(j)
                    # j+=1
                d[year]=movie_list
            print(d)
        with open("second_task.json","w") as f1:
            json.dump(d,f1,indent=4,sort_keys=True)
    group_by_year()
            
        
