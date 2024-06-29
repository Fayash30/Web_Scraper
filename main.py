
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import openpyxl.workbook
import requests,openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title="Anime List"
sheet.append(['Rank','Anime Name','Episodes','Ratings'])
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

        for anime in animes:
            
            rank =  anime.find('td',class_="rank ac").span.text.strip()
            title = anime.find('td',class_="title al va-t word-break").h3.text.strip()
            infos = anime.find('div',class_="information di-ib mt4").text.strip().split(')')[0]
            episodes = infos.split('(')[1]
            score = anime.find('td',class_="score ac fs14").span.text.strip()

            sheet.append([rank,title,episodes,score])
        
        next_button = soup.find('a',class_="link-blue-box next")
        has_next = next_button is not None and page_number < 10

        page_number += 1


except Exception as e:
    print(e)

excel.save("Anime.xlsx")