import os
from flask import Flask, render_template, request, redirect
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

@app.route("/orden_menu", methods=["GET", "POST"])
def orden_menu():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        menu = request.form.get("id_menu")
        empleado = request.form.get("id_empleado")
        cliente = request.form.get("id_cliente")
        cantidad = request.form.get("Cant_pedida")
        print(menu, empleado, cliente, cantidad)
        return render_template("orden_menu.html")
    else:
        return render_template("orden_menu.html")

@app.route("/usuario", methods=["GET", "POST"])
def usuario():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        registro = request.form.get("id_emp")
        usuario = request.form.get("username")
        contraseña = request.form.get("pass")
        #db.execute("INSERT INTO empleado (id_pers) values(:registro)", registro=registro )
        db.execute("INSERT INTO usuario(id_emp,username, pass) values(?,?,?)",registro,usuario,contraseña)
        return redirect("/usuario")

    else:
        vista = db.execute("SELECT * FROM usuario")
        print(vista)
        usuario = db.execute("SELECT *FROM empleado")
        return render_template("usuario.html",usuario=usuario, vista=vista)

@app.route("/usuario_eliminar/<id>", methods=["GET", "POST"])
def usuario_eliminar(id):
    print("hola", id)
    db.execute("DELETE FROM usuario WHERE id = :id",id=id)
    return redirect("/usuario")


@app.route("/rol", methods=["GET", "POST"])
def rol():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        registro = request.form.get("id_user")
        tipo = request.form.get("Tipo_rol")
        estado = request.form.get("Estado")
        db.execute("INSERT INTO rol_usuario(id_user,Tipo_rol, Estado) values(?,?,?)",registro,tipo,estado)
        return redirect("/rol")

    else:
        vista = db.execute("SELECT * FROM rol_usuario")
        print(vista)
        rolu = db.execute("SELECT *FROM usuario")
        return render_template("rol.html",rolu=rolu, vista=vista)


@app.route("/rol_eliminar/<id>", methods=["GET", "POST"])
def rol_eliminar(id):
    print("hola", id)
    db.execute("DELETE FROM rol_usuario WHERE id = :id",id=id)
    return redirect("/rol")

@app.route("/clientes", methods=["GET", "POST"])
def cliente():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        registro = request.form.get("id_pers")
        db.execute("INSERT INTO clientes (id_pers) values(:registro)", registro=registro )
        return redirect("/clientes")
    else:
        vista = db.execute("SELECT *FROM persona INNER JOIN clientes ON clientes.id_pers=persona.id")
        print(vista)
        clientes = db.execute("SELECT *FROM persona")
        return render_template("clientes.html", clientes=clientes, vista=vista)

@app.route("/clientes_eliminar/<id>", methods=["GET", "POST"])
def clientes_eliminar(id):
    print("hola", id)
    db.execute("DELETE FROM clientes WHERE id = :id",id=id)
    return redirect("/clientes")

@app.route("/empleado", methods=["GET", "POST"])
def empleado():
    if request.method == "POST":
        # Estos son los datos para poder registrarse
        registro = request.form.get("id_pers")
        db.execute("INSERT INTO empleado (id_pers) values(:registro)", registro=registro )
        return redirect("/empleado")
    else:
        vista = db.execute("SELECT *FROM persona INNER JOIN empleado ON empleado.id_pers=persona.id")
        print(vista)
        empleado = db.execute("SELECT *FROM persona")
        return render_template("empleado.html", empleado=empleado, vista=vista)

@app.route("/empleado_eliminar/<id>", methods=["GET", "POST"])
def empleado_eliminar(id):
    print("hola", id)
    db.execute("DELETE FROM empleado WHERE id = :id",id=id)
    return redirect("/empleado")

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

        db.execute("INSERT INTO persona(Nombre_pers, Ape_pers, Dic_pers, Tel_pers, Cor_pers) values(?,?,?,?,?)",nombre,apellido,direccion,telefono,correo)
        return redirect("/persona")
    else:
        vista = db.execute("SELECT * FROM persona")
        print(vista)
        return render_template("persona.html",vista=vista)

@app.route("/persona_eliminar/<id>", methods=["GET", "POST"])
def persona_eliminar(id):
    print("hola", id)
    db.execute("DELETE FROM persona WHERE id = :id",id=id)
    return redirect("/persona")

@app.route("/problema")
def problema():
    return render_template("problema.html")