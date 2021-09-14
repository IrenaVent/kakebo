# las rutas se crean por convenio en views y se consideran las vistas

from balance import app

@app.route("/")
def index():
    return "Flask funcionando"