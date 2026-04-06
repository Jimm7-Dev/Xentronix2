from ModelUsuario import ModelUsuario  
from ModelProducto import ModelProducto 
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9dcb3380af008f90b23a5d1616bf319bc298105da20fe'
CORS(app)

usuarios = ModelUsuario()
productos = ModelProducto()


@app.route('/login', methods=['POST'])  
def loginUsuario():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Faltan credenciales"}), 400
    
    resultado = usuarios.verificarUsuario(email, password)
    if resultado:
        return jsonify({"mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios.obtener_usuarios())

@app.route('/usuario/<int:id>', methods=['GET'])
def listar_usuario(id):
    usuario = usuarios.obtener_usuario(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    contrasena = data.get('contrasena')
   

    if not all([nombre, email, contrasena]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    usuarios.insertar_usuario(nombre, email, contrasena )
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201

@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    contrasena = data.get('contrasena')
   

    if not any([nombre, email, contrasena]):
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    usuario_existente = usuarios.obtener_usuario(id)
    if usuario_existente:
        usuarios.actualizar_usuario(id, nombre, email, contrasena)
        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    else:
        return jsonify({"error": "El usuario no existe"}), 404

@app.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if usuarios.obtener_usuario(id):
        usuarios.eliminar_usuario(id)
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    else:
        return jsonify({"error": "El usuario no existe"}), 404


@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(productos.obtener_productos())

@app.route('/producto/<int:id>', methods=['GET'])
def listar_producto(id):
    producto = productos.obtener_producto(id)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/nuevo_producto', methods=['POST'])
def crear_producto():
    data = request.json
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')

    if not all([nombre, descripcion, precio]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    productos.insertar_producto(nombre, descripcion, float(precio))
    return jsonify({"mensaje": "Producto creado exitosamente"}), 201

@app.route('/actualizar_producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')

    if not any([nombre, descripcion, precio]):
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    producto_existente = productos.obtener_producto(id)
    if producto_existente:
        productos.actualizar_producto(id, nombre, descripcion, float(precio))
        return jsonify({"mensaje": "Producto actualizado correctamente"}), 200
    else:
        return jsonify({"error": "El producto no existe"}), 404

@app.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    if productos.obtener_producto(id):
        productos.eliminar_producto(id)
        return jsonify({"mensaje": "Producto eliminado correctamente"}), 200
    else:
        return jsonify({"error": "El producto no existe"}), 404

if __name__ == '__main__':
    app.run(debug=True)


