import mysql.connector
from mysql.connector import Error

class ConexionMySQL:
    def __init__(self):
        try:
            self.mibasededatos = mysql.connector.connect(
                host="localhost",
                port=3306,  
                user="root",
                password="",
                database="tienda_virtual_3"  
            )

            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()

            if self.conexion.is_connected():
                db_info = self.conexion.get_server_info()
                print(" Conectado a MySQL Server versión", db_info)

        except Error as e:
            print(f" Error al conectarse a MySQL: {e}")

    def cerrar_conexion(self):
        if self.mibasededatos.is_connected():
            self.cursor.close()
            self.conexion.close()
            print(" Conexión a MySQL cerrada")


if __name__ == "__main__":
    conexion = ConexionMySQL()
    conexion.cerrar_conexion()
