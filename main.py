
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests,openpyxl

web_url = os.getenv('URL')

# try:
#     response = requests.get(web_url)