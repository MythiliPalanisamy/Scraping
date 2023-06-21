from bs4 import BeautifulSoup
import requests

url='https://country-leaders.onrender.com/status'
r=requests.get(url)
soup= BeautifulSoup(r.content, 'html')

if r.status_code==200:
    print(soup.text)
else:
    print(r.status_code, url)


