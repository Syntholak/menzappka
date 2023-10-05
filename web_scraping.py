import requests 
from bs4 import BeautifulSoup

url = "http://www.kam.vutbr.cz/?p=menu&provoz=10"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

table_element = soup.find(id="r1")
print(table_element)