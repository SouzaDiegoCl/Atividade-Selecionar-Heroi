from flask import render_template, request


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/universoSelect", methods=["POST", "GET"])
    def universoSelect():
        universo = request.form.get("inputUniversoSelect")
        return render_template("index.html", universoSelecionado=universo)

    @app.route("/heroiSelect", methods=["POST", "GET"])
    def heroiSelect():
        universo = "selecionado"
        heroi = request.form.get("inputHeroiSelect")
        return render_template("index.html", heroiSelecionado=heroi, universoSelecionado = universo)
