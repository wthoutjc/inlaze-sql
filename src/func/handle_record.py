import psycopg2
from psycopg2 import OperationalError, Error

def get_record_count(db_config, table_name):
    """
    Conecta a la base de datos PostgreSQL y obtiene el número total de registros en una tabla específica.

    :param db_config: Diccionario con la configuración de la base de datos (host, dbname, user, password)
    :param table_name: Nombre de la tabla para la que se desea obtener el recuento de registros
    :return: Número total de registros en la tabla
    """
    conn = None
    record_count = 0

    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        record_count = cursor.fetchone()[0]

        cursor.close()
    except OperationalError as e:
        print(f"Error de conexión a la base de datos: {e}")
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        if conn:
            conn.close()

    return record_count
