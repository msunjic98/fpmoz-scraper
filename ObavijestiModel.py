from sources import SOURCES
import urllib.request
from bs4 import BeautifulSoup
def getObavijesti(pageNumber, start, studij):
  if pageNumber not in [0, 1]:
    start = (pageNumber - 1) * 6
  page = urllib.request.urlopen('{}&limitstart={}'.format(SOURCES['fpmoz'][studij], pageNumber))
  return page

def parseObavijesti(raw):
  parsed = BeautifulSoup(raw, 'html.parser')
  articles = parsed.find_all('article')

  results = []
  for article in articles:
    data = {}

    data['naslov'] = article.h2.a.text.strip()
    data['link'] = 'https://fpmoz.sum.ba{}'.format(article.h2.a['href'])
    if article.dl.dd.span:
      data['datum'] = article.dl.dd.span.text.strip()
    else:
      data['datum'] = article.dl.dd.text

    if article.p.span:
      data['tekst'] = article.p.span.text.strip()
    else:
      data['tekst'] = article.p.text

    if data['tekst'] == 'Obavijesti':
      data['tekst'] = 'Kliknite na naslov da bi otvorili obavijest (#jebiga #ne_znaju_objavit_kako_treba).'

    results.append(data)

  return results

