import requests
from bs4 import BeautifulSoup

url = "https://www.rugbypass.com/united-rugby-championship/fixtures-results/"
res = requests.get(url)
htmlData = res.content
soup = BeautifulSoup(htmlData, "html.parser")
layer1 = soup.find_all('div','games-list-item')
# print(soup.prettify())
# print(layer1)
layer2 = soup.find_all('div', 'games')
# print(layer2)
layer3 = soup.find_all('div', 'game scores')
# print(layer3)
layer4 = soup.find_all('div', 'venue')
print(layer4[0].text)