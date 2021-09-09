from flask import Flask, render_template, request, redirect, flash, url_for,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'trabajo_arle'
mysql = MySQL(app)



@app.route('/', methods = ['GET'])
def Index():
    return render_template("restaurante.html")

@app.route('/ingresar', methods=['POST','GET'])
def ingresar(): 
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
    
@app.route('/registrar', methods=['POST','GET'])
def ingre():
    if request.method == 'POST':
        Id = request.form['id']
        Inicio = request.form['fecha']
        Restaurante = request.form['restaurante']
        Des = request.form['Descripcion']
        FechaEvento = request.form['fechae']
        FechaFinal = request.form['fechaf']
        cur = mysql.connection.cursor()
        B = cur.execute('INSERT INTO eventos(id_evento,fecha_publicacion,Descripcion,idrestaurante,fecha_evento,fecha_final) VALUES("{}","{}","{}","{}","{}","{}")'.format (Id, Inicio, Des, Restaurante, FechaEvento, FechaFinal))
        mysql.connection.commit()
    return render_template("restaurante.html")

@app.route('/mostrar')
def Mostrar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT e.id_evento, r.nombre, e.Descripcion, e.fecha_evento, e.fecha_final FROM restaurante AS r INNER JOIN eventos AS e ON r.id_restaurante = e.idrestaurante ORDER BY e.id_evento')
    Evento = cur.fetchall()
    return render_template("evento.html", Eventos = Evento)

@app.route('/editar/<id_evento>')
def Editar(id_evento):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM eventos WHERE id_evento = {}".format(id_evento))
    data = cur.fetchall()
    return render_template('editarevento.html', evento = data[0])


@app.route('/actualizar/<id_evento>', methods=['POST'])
def Actualizar(id_evento):
    if request.method == 'POST':
        restaurante = request.form['restaurante']
        Descripcion = request.form['Descripcion']
        fechaf = request.form['fechaf']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE eventos 
                    SET idrestaurante = %s,
                    Descripcion = %s,
                    fecha_final = %s
                WHERE id_evento = %s
        """,(restaurante,Descripcion,fechaf,id_evento))
        mysql.connection.commit()
    return redirect(url_for('Mostrar'))

@app.route('/eliminar/<string:id_evento>')
def delete_contact(id_evento):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM eventos WHERE id_evento = {0}".format(id_evento))
    mysql.connection.commit()
    return redirect(url_for('Mostrar'))


if __name__ == "__main__":
    app.run(debug=True, port=9001)