import json
import urllib.request
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
FPMOZ_INFORMATIKA = 'https://fpmoz.sum.ba/index.php?option=com_content&view=category&id=34&Itemid=122&lang=hr'


@app.route('/')
def index():
  return json.dumps({
    'message': 'hello FPMOZ ¯\_(ツ)_/¯'
  })

@app.route('/dohvatiObavijesti')
def dohvatiObavijesti():
  page = urllib.request.urlopen(FPMOZ_INFORMATIKA)
  soup = BeautifulSoup(page, 'html.parser')

  articles = soup.find_all('article')
  finalizedArray = []
  for article in articles:
      data = {}
      
      data['naslov'] = article.h2.a.text.strip()
      if article.dl.dd.span:
        data['datum'] = article.dl.dd.span.text.strip()
      else:
        data['datum'] = article.dl.dd.text
        
      if article.p.span:
        data['tekst'] = article.p.span.text.strip()
      else:
        data['tekst'] = article.p.text
      finalizedArray.append(data)

  return json.dumps(finalizedArray)