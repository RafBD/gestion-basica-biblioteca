import pymysql

def connect_db():

    try:
        # Parametros de conexion a la base de datos
        db_host = 'localhost'
        db_user = 'root'
        db_password = ''
        db_name = 'gestion_biblioteca'

        # Establecer conexion con la base de datos
        connection = pymysql.connect(
            host=db_host, 
            user=db_user, 
            password=db_password, 
            db=db_name
        )
        return connection
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def close_connection(connection):
    try:
        connection.close()
    except Exception as e:
        print(f"Error al cerrar la conexion con la base de datos: {e}")