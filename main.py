from bs4 import BeautifulSoup
import requests

articleLink = "https://edition.cnn.com/2023/04/23/tech/iphone-thief-recovery-key/index.html"

response = requests.get(articleLink)
coreWebpage = response.text

soup = BeautifulSoup(coreWebpage, "html.parser")


title = soup.find(name='title')
print(title.text)

par = soup.find_all('p')
parText = ""
for e in par:
    parText = parText + e.get_text()

date = soup.find('meta', property='article:modified_time')['content']

byline = soup.find('meta', attrs={'name': 'author'})
byline = byline['content']

print("Date published: ", date)
print("Byline: ", byline)
print("Title: ", title)
print("Article Content: ", parText)
