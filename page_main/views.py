import requests
import bs4
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from urllib.request import urlopen
from django.shortcuts import render
from accounts.models import CustomUser

from django.views import View


@login_required
def page_main(request):
    blocks_links = []
    texts = []
    soup = bs4.BeautifulSoup(
        urlopen("http://korrespondent.net"), "html.parser")
    all_divs = soup.findAll("div", {"class": "time-articles"})
    mydivs = soup.findAll(
        "div", {"class": "article__title"})  # time-articles
    # находим ссылки к статье
    for link in soup.findAll('a', href=True):
        a = link['href']
        blocks_links.append(a)
    # находим название статьи
    for text in mydivs:
        a = text.find(text=True)
        texts.append(a)
    # обьединяем название статьи и ссылку
    name_with_link = list(zip(texts, blocks_links))
    return render(request, 'page_main/page_main.html', {"name_with_link": name_with_link})


