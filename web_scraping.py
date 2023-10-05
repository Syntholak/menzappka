import requests 
from bs4 import BeautifulSoup

url = "http://www.kam.vutbr.cz/?p=menu&provoz=10"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

table_element = "test"

i = 1

all_food_items = []

# TODO test this
while table_element is not None:
    table_element = soup.find(id="r" + str(i))
    print(table_element)
    all_food_items.append(table_element)
    i = i + 1

# TODO test HTML parsing

# html_content = '''<tr class="wn0" id="r1">
#     <td class="levy">H</td>
#     <td class="gram">120<span class="lomit">/</span>72</td>
#     <td class="levyjid jjjaz1jjj fs1" onclick="slo(1)">Kuřecí katův šleh
#         <small style="font-size: 70%;"> 1,3,7,9,13</small>
#     </td>
#     <td class="levyjid jjjaz2jjj">Spicy chicken strips stewed with onion, bell pepper and tomato sauce
#         <small style="font-size: 70%;"> 1,3,7,9,13</small>
#     </td>
#     <td class="pravy slcen1">67,- </td>
#     <td class="pravy slcen2">34,- </td>
#     <td class="pravy slcen3">103,- </td>
# </tr>'''

# soup = BeautifulSoup(html_content, 'html.parser')
# row = soup.find("tr", class_="wn0")

# data = {
#     'Label': row.find('td', class_='levy').text,
#     'Gram': row.find('td', class_='gram').text,
#     'Dish Name (Native)': row.find('td', class_='jjjaz1jjj').text.split('<small')[0].strip(),
#     'Allergens (Native)': row.find('td', class_='jjjaz1jjj').small.text.strip(),
#     'Dish Name (English)': row.find('td', class_='jjjaz2jjj').text.split('<small')[0].strip(),
#     'Allergens (English)': row.find('td', class_='jjjaz2jjj').small.text.strip(),
#     'Price 1': row.find('td', class_='slcen1').text.strip(),
#     'Price 2': row.find('td', class_='slcen2').text.strip(),
#     'Price 3': row.find('td', class_='slcen3').text.strip()
# }

# print(data)