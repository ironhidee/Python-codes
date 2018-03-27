import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://economictimes.indiatimes.com/jindal-steel-power-ltd/stocks/companyid-4355.cms")
page.content
soup = BeautifulSoup(page.content, 'html.parser')
soup.title
soup.title.string
p =soup.find('div', attrs = {'class':'value'})
print(p)
print(p.text)