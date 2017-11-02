from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


def scrapper(characters):
    wookie_url = "http://starwars.wikia.com/wiki/{}"
    url_characters = [wookie_url.format(
        character['name'].replace(' ', '_')) for character in characters]
    list_characters = list()
    for index, url in enumerate(url_characters, start=0):
        req = requests.get(url)
        try:
            soup = BeautifulSoup(req.text, 'html.parser')
            imgs = soup.find_all('img',
                                 attrs={'class': 'pi-image-thumbnail'})
            list_characters.append(
                dict(
                    name=characters[index]['name'],
                    img_url=imgs[0]['src']
                )
            )
        except:
            list_characters.append(
                dict(
                    name=characters[index]['name'],
                    img_url=""
                )
            )
    return list_characters


def index(request):
    return render(request, 'index.html',
                  {"greeting": "Hola a todos"})


def characters(request, page=1):
    url = "http://swapi.co/api/people/?page={}".format(page)
    r = requests.get(url)
    if r.status_code == 200:
        characters = scrapper(r.json()['results'])
    else:
        characters = list()

    return render(request, 'character.html',
                  {"characters": characters})
