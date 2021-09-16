from flask import Flask # aquí se crea aplicación flask

FICHERO = "data/movimientos.csv"

app = Flask(__name__)

# tiene que estar situado depués de hacer la app
from balance import views 