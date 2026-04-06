from conexionbasedata import ConexionMySQL

class ModelProducto:
    def __init__(self):
        self.mibasededatos = ConexionMySQL()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_producto(self, id):
        self.cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        return self.cursor.fetchone()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def insertar_producto(self, nombre, descripcion, precio):
        val = (nombre, descripcion, precio)
        sql = "INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_producto(self, id, nombre, descripcion, precio):
        val = (nombre, descripcion, precio, id)
        sql = "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_producto(self, id):
        sql = "DELETE FROM productos WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()




