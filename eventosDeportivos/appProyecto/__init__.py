from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#Añadiendo esto, no es necesaria la barra del final en la URL
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tsi/eventosDeportivos.db'
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

import appProyecto.controllers
