# las rutas se crean por convenio en views y se consideran las vistas
# la vista solo se encarga de generar el HTML
# los datos los genera el modelo

from balance import app
from flask import render_template, request, redirect, url_for  # informamos un fichero, request es un objeto de flask
from balance.models import ListaMovimientos, Movimiento, ValidationError

@app.route("/")
def index():
    lm = ListaMovimientos()
    lm.leer()
    return render_template("index.html", items=lm.movimientos)

@app.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    if request.method == "GET":
        return render_template("nuevo_movimiento.html", errores=[], form={"fecha":"", "concepto": "", "cantidad":""})
    else:
        datos = request.form
        movimiento = Movimiento(datos)
        if len(movimiento.errores) > 0:
            return render_template("nuevo_movimiento.html", errores=movimiento.errores, form=datos)

        # TODO validar datos

        lm = ListaMovimientos() #instanciamos LM para actuar sobre ella posteriormente
        lm.leer() 
        lm.anyadir(datos)
        lm.escribir()
        return redirect(url_for("index")) # no indicamos la ruta, esta en el futuro puede cambiar sino redireccionamos con nombre página