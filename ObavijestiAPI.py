from flask import Blueprint, request
import json
from ObavijestiModel import getObavijesti, parseObavijesti
obavijesti_api = Blueprint('obavijesti_api', __name__)

@obavijesti_api.route('/dohvati')
def dohvatiObavijesti():
  pageNumber = request.args.get('page') or 0
  studij = str(request.args.get('studij'))
  start = 0
  raw_obavijesti = getObavijesti(int(pageNumber), start, studij)
  parsedObavijesti = parseObavijesti(raw_obavijesti)
  print(parsedObavijesti)
  return json.dumps(parsedObavijesti)
