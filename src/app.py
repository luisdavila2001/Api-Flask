from flask import Flask,jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask (__name__)

conexion = MySQL(app)

@app.route('/Usuarios')
def listar_usuario():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM Usuario'
        cursor.execute(sql)
        datos = cursor.fetchall()
        users = []
        for fila in datos:
            usuario = {'id': fila[0], 'Nombre': fila[1], 'Apellido': fila[2],  'NumeroCel': fila[3],   'DNI': fila[4],'Contraseña': fila[5], 'Saldo': fila[6], 'Codigo': fila[7], 'create_at': fila[8], 'update_at':fila[9]}
            users.append(usuario)
        return jsonify({'user':users})
        
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/Producto')
def listar_producto():
    try:
        cursor = conexion.connection.cursor()  # Corregido aquí
        sql = 'SELECT * FROM Producto'
        cursor.execute(sql)
        datos = cursor.fetchall()
        produ = []
        for fila in datos:
            producto = {'id': fila[0], 'idTipo': fila[1], 'idEmpresa': fila[2], 'Titulo': fila[3], 'Precio': fila[4], 'Detalle': fila[5], 'Validez': fila[6], 'Stock': fila[7], 'create_at': fila[8], 'update_at': fila[9]}
            produ.append(producto)
        return jsonify({'producto': produ})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/Empresa')
def listar_Empresa():
    try:
        cursor = conexion.connection.cursor()
        sql = 'select * from Empresa'
        cursor.execute(sql)
        datos = cursor.fetchall()
        empresa =[]
        for fila in datos:
            empre = {'id':fila[0],'RazonSocial':fila[1],'Codigo':fila[2],'idSector':fila[3]}
            empresa.append(empre)
        return jsonify({'empresas':empresa})
    
    except Exception as ex:
        return jsonify({'mensaje': "Error"})
            

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)