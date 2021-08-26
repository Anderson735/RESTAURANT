from flask import Flask, render_template, request, redirect, flash, url_for,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dragon77'
app.config['MYSQL_DB'] = 'trabajo_arle'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/', methods = ['GET'])
def Index():
    return render_template("restaurante.html")

@app.route('/ingresar', methods=['POST','GET'])
def ingresar():
    if request.method == 'POST':
        Inicio = request.form['fecha']
        Restaurante = request.form['restaurante']
        Des = request.form['Descripcion']
        FechaEvento = request.form['fechae']
        FechaFinal = request.form['fechaf']
        cur = mysql.connection.cursor()
        B = cur.execute('INSERT INTO eventos(fecha_publicacion,Descripcion,id_restaurante,fecha_evento,fecha_final) VALUES("{}","{}","{}","{}","{}")'.format (Inicio, Des, Restaurante, FechaEvento, FechaFinal))
        mysql.connection.commit()
    return render_template("restaurante.html")
    
@app.route('/registrar', methods=['POST','GET'])
def ingre():
    if request.method == 'POST':
        Id = request.form['id']
        Nombre = request.form['nombre']
        Lugar = request.form['lugar']
        Telefono = request.form['telefono']
        Categoria = request.form['categoria']
        cur = mysql.connection.cursor()
        B = cur.execute('INSERT INTO restaurante(id_restaurante,nombre,direccion,telefono,categoria) VALUES("{}","{}","{}","{}","{}")'.format (Id, Nombre, Lugar, Telefono, Categoria))
        mysql.connection.commit()
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=9001)