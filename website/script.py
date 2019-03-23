import requests
from bs4 import BeautifulSoup as bs
def date(a):
    a=a
    url = "https://en.wikipedia.org/wiki/"
    year = a
    url += year + "_in_India"
    html = requests.get(url)
    soup = bs(html.content,'lxml')
    container = soup.find('div', {'class':'mw-content-ltr'})
    alList = container.findAll('ul')[7]
    data = alList.select('li')
    x=[]
    for d in data:
        x.append(d.text.strip())
    return x
