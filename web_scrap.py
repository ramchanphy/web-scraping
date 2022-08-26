from bs4 import BeautifulSoup
import requests
import json
try:
    source=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")  #to Store HTML code


    soup=BeautifulSoup(source.text,'html.parser')  #.text is used to extract HTML code/'HTML.parser' is a default parser with python installation
    movies=soup.find('tbody',class_='lister-list').find_all('tr')
    details_list=[]
    for movie in movies:
        details={"movie":"","rank":"","rating":"","year":"","link":""}#to iterate through each tr tag to get information abt each td tag   #this movies have details of 250 tr tags having detail for each movie  # we use movie to fetch one movie at a time
        name=movie.find('td',class_="titleColumn").a.text  #to extract the exact movie name from tr tag and then by entering into the td tag
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]  #(split is used to get the value before'.',it will return a list with one at zero index)  #text attribute return whatever text is written in that td tag i.e the serial no. and release year too    #.get_text(strip=True),strip will remove all new line or spaces,etc
        year=movie.find('td',class_="titleColumn").span.text.strip("()")
        rating=movie.find('td',class_="ratingColumn imdbRating").strong.text
        
        url=movie.find('td',class_="titleColumn").a["href"]# href is a data or link that user can access by touching or clicking on
        movie_url="https://www.imdb.com"+url
        details["movie"]=name
        details["rank"]=rank
        details["rating"]=rating
        details["year"]=year
        details["link"]=movie_url
        details_list.append(details)
        print(rank,name,year,rating)

    with open("movies.json","w") as f:
        json.dump(details_list,f,indent=4)
except Exception as e:
    print(e)
    