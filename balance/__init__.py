# aquí se crea aplicación flask

from flask import Flask

app = Flask(__name__)

# tiene que ser depueés de hacer la app
from balance import views 