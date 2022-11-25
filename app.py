import os
from flask import Flask, render_template
from cs50 import SQL


app = Flask(__name__)

db = SQL("sqlite:///database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def Menu():
    return render_template("menu.html")

@app.route("/solicitado")
def solocitado():
    return render_template("solicitado.html")

@app.route("/orden_menu")
def orden_menu():
    return render_template("orden_menu.html")

@app.route("/usuario")
def usuario():
    return render_template("usuario.html")
@app.route("/rol")
def rol():
    return render_template("rol.html")

@app.route("/clientes")
def cliente():
    return render_template("clientes.html")

@app.route("/empleado")
def empleado():
    return render_template("empleado.html")

@app.route("/persona")
def persona():
    return render_template("persona.html")

@app.route("/problema")
def problema():
    return render_template("problema.html")