
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

load_dotenv()

#Get Url From .env

web_url = os.getenv('URL')

page_number = 1
has_next = True

try:
    while has_next:
        params = {'page':page_number}
        response = requests.get(web_url , params = params)
        soup = BeautifulSoup(response.text , 'html.parser')
        
        #Storing the Html parser to a variable
        animes = soup.find('table',class_ = "top-ranking-table").find_all('tr')
        
        animes.pop(0)

        anime_list = {"anime_rank":[] , "anime_title":[],"episodes":[],"anime_score":[]}
        for anime in animes:
            
            rank =  anime.find('td',class_="rank ac").span.text.strip()
            title = anime.find('td',class_="title al va-t word-break").h3.text.strip()
            infos = anime.find('div',class_="information di-ib mt4").text.strip().split(')')[0]
            episodes = infos.split('(')[1]
            score = anime.find('td',class_="score ac fs14").span.text.strip()

            anime_list["anime_rank"].append(rank)
            anime_list["anime_title"].append(title)
            anime_list['episodes'].append(episodes)
            anime_list["anime_score"].append(score)
            
        
        next_button = soup.find('a',class_="link-blue-box next")
        has_next = next_button is not None and page_number < 10

        page_number += 1


except Exception as e:
    print(e)

df = pd.DataFrame(data=anime_list)

#To see First 5 Records
print(df.head())

#Connecting with sqlite
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

# Create table
qry = '''
CREATE TABLE IF NOT EXISTS animes (
    anime_rank TEXT,
    anime_title TEXT,
    episodes TEXT,
    anime_score TEXT
)
'''
cursor.execute(qry)

for i in range(len(df)):
    cursor.execute("INSERT INTO ANIMES VALUES (?,?,?,?)",df.iloc[i].values)

connection.commit()
connection.close()