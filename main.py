# import libraries
from bs4 import BeautifulSoup
import requests

def scrapeNcix():
    # start with ncix
    ncix = "https://www.ncix.com/"

    ncixRsp = requests.get(ncix, timeout=5)
    soup = BeautifulSoup(ncixRsp.content, 'html.parser')
    print(soup)

scrapeNcix()

