import os
from flask import Flask, render_template, request
from cs50 import SQL


app = Flask(__name__)

db = SQL("sqlite:///comedor.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/dia")
def dia():
    return render_template("dia.html")

@app.route("/orden_dia")
def orden_dia():
    return render_template("orden_dia.html")

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

@app.route("/persona", methods=["GET", "POST"])
def persona():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        nombre = request.form.get("Nombre_pers")
        apellido = request.form.get("Ape_pers")
        direccion = request.form.get("Dic_pers")
        telefono = request.form.get("Tel_pers")
        correo = request.form.get("Cor_pers")
        print(nombre, apellido, direccion, telefono, correo)
    else:
        return render_template("persona.html")

@app.route("/problema")
def problema():
    return render_template("problema.html")