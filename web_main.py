

from bs4 import BeautifulSoup
import requests

def news_post():
    response = requests.get('https://www.fitnessblender.com/')
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    data = {}
    data_arr = []

    for i in soup.findAll('div', {'class': 'title-card-group'}):
        p = str(i)
        data = {
            'title': i.h2.text,
            'text': p[p.find('"title":') + 9:p.find('subtitle') - 3],
            'image': 'https://d18zdz9g6n5za7.cloudfront.net/plan/640/640-' + p[p.find('"image":') + 9:p.find(
                'image_icon') - 3],
            'time': p[p.find('"minutes_avg"') + 14:p.find('"minutes_min"') - 1] + ' Min/Day ' + p[p.find(
                '"weeks"') + 8:p.find('"brand"') - 1] + ' Weeks'

        }
        data_arr.append(data)
    return data_arr





