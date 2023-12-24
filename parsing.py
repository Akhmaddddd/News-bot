import requests
from bs4 import BeautifulSoup

def news_pars(category):
    list_news=[]
    url='https://upl.uz/'
    host='https://upl.uz'
    html=requests.get(url+category).text
    soup=BeautifulSoup(html,'html.parser')
    block=soup.find_all('div',class_='short-story')

    for i in block[:3]:
        image=host+i.find('img',class_='lazy-loaded').get('data-src')

        title=i.find('h2',class_='sh-tit').get_text(strip=True)
        description=i.find('div',class_='sh-pan').get_text(strip=True)
        timeof=i.find('div',class_='sh-dat itim').get_text(strip=True)
        link =   i.find('a').get('href')
        list_news.append({
            'image':image,
            'title':title,
            'description':description,
            'timeof':timeof,
            'link':link
        })

    return list_news











