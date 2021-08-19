from flask import Flask, render_template, request, redirect, flash, url_for,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dragon77'
app.config['MYSQL_DB'] = 'proyecto_trimestral'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    Usuario = request.form['usuario']
    Contraseña = request.form['contraseña']
    cur = mysql.connection.cursor()
    B = cur.execute('SELECT * FROM usuarios WHERE codigo = %s and contrasena = %s',(Usuario,Contraseña))
    B = cur.fetchall()
    if B:
        session["username"] = Usuario
        session["contraseña"]= Contraseña
        return render_template("registrar.html")
    return "No pertenece al sistema"

if __name__ == "__main__":
    app.run(debug=True, port=9001)