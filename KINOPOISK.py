import requests, os, time
from bs4 import BeautifulSoup as bs

def search_news(page_html : str):
	pass

def getinf(url : str):
	sections = {"Интервью", "Сериалы", "Трейлеры", "Сборы", "Индустрия", 
				"Прочее"} # "Прочее" не описано

	url = "https://www.kinopoisk.ru/media/news/"
	r = requests.get(url)

	soup = bs(r.content, "html.parser")
	soup = soup.prettify()

	with open('tmp_text.txt', 'w', encoding = "utf-8") as f:
		f.write(str(soup))

getinf("")