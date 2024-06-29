
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests,openpyxl



load_dotenv()

#Get Url From .env

web_url = os.getenv('URL')

try:
    response = requests.get(web_url)
    soup = BeautifulSoup(response.text , 'html.parser')
    
    #Storing the Html parser to a variable
    animes = soup.find('table',class_ = "top-ranking-table").find_all('tr')
    
    animes.pop(0)
    print(len(animes))

    for anime in animes:
       # print(movie)
        rank =  anime.find('td',class_="rank ac").span.text.strip()
        title = anime.find('td',class_="title al va-t word-break").h3.text.strip()
        infos = anime.find('div',class_="information di-ib mt4").text.strip().split(')')[0]
        episodes = infos.split('(')[1]
        score = anime.find('td',class_="score ac fs14").span.text.strip()

        print(rank,title,episodes,score)
        
        

except Exception as e:
    print(e)