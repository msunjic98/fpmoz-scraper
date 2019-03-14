from flask import Flask, request
from ObavijestiAPI import obavijesti_api

app = Flask(__name__)
app.debug = True

app.register_blueprint(obavijesti_api, url_prefix='/obavijesti')

if __name__ == "__main__":
  app.run()

