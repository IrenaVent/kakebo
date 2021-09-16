# las rutas se crean por convenio en views y se consideran las vistas

from balance import app
from flask import render_template #informamos un fichero
from balance.models import ListaMovimientos


@app.route("/")
def index():
    lm = ListaMovimientos()
    lm.leer()
    return render_template("index.html", items = lm.movimientos)