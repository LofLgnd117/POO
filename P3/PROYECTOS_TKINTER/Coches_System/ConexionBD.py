import mysql.connector

# Variables globales para usar en los modelos
conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # Pon tu contraseña si tienes
        database='bd_coches'
    )
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print(f"Error en la conexión BD: {e}")