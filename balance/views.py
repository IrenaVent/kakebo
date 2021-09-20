# las rutas se crean por convenio en views y se consideran las vistas
# la vista solo se encarga de generar el HTML
# los datos los genera el modelo

from balance import app
from flask import render_template, request  # informamos un fichero, request es un objeto de flask
from balance.models import ListaMovimientos

@app.route("/")
def index():
    lm = ListaMovimientos()
    lm.leer()
    return render_template("index.html", items=lm.movimientos)

@app.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    if request.method == "GET":
        return render_template("nuevo_movimiento.html")
    else:
        return None