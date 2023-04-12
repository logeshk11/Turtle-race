import requests
from bs4 import BeautifulSoup
apikey = "9b88077c12784b55a7c43099ed27a68a"

website= "https://subslikescript.com/movies"

news_end_point= "https://newsapi.org/v2/top-headlines?"

params= {
    "country": "India",
    "apikey": apikey
}

response = requests.get(website)
response.raise_for_status()
content = response.text
soup= BeautifulSoup(content, 'lxml')
links=[]
box= soup.find('article', class_='main-article')
for link in box.find_all('a', href= True):
    links.append(link['href'])

for i in links:
    print(i)
# title= box.find('h1').get_text()
# transcript= box.find('div', class_='full-script').get_text(strip=True, separator=' ')
# print(transcript)
# with open('titanic.txt', 'w') as file:
#     file.write(transcript)
