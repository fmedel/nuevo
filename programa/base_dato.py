#libreira base
import sys
import logging
import psycopg2
###############################
class conexion_base_datos: #conexion con la bases de datos PostgreSQL
    def __init__(self,host = "localhost",user = "docker",dbname = "docker",password = "docker",port = "8082"):
        self.host = host
        self.user = user
        self.dbname = dbname
        self.password = password
        self.port = port
    def crear_bd(self):
        try:
            conn_string = "host={0} user={1} dbname={2} password={3} port={4}".format(self.host, self.user, self.dbname, self.password, self.port)
            conn = psycopg2.connect(conn_string)
            logging.debug("conexion establecida")
            cursor = conn.cursor()
            try:
                cursor.execute("DROP TABLE IF EXISTS inventory;")
                logging.info("la tabla correctamente eliminda (if existed)")
            except:
                print("Error en la elimiminacion de la tabla")
            try:
                cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);") # aqui es donde se pone la tablas
                logging.info("la tabla correctamente creada ")
            except:
                print("Error en la cración de la tabla")
            conn.commit()
            cursor.close()
            conn.close()
            logging.debug("conexion terminada")
        except:
            print("Error en la conexion")
            logging.critical("Error en la conexion")

    def cargar_datos(self):
        try:
            conn_string = "host={0} user={1} dbname={2} password={3} port={4}".format(self.host, self.user, self.dbname, self.password, self.port)
            conn = psycopg2.connect(conn_string)
            logging.debug("conexion establecida")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
            cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
            cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
            conn.commit()
            cursor.close()
            conn.close()
            logging.debug("conexion terminada")
        except:
            print("Error en la conexion")
            logging.critical("Error en la conexion")

    def listar_all(self):
        try:
            conn_string = "host={0} user={1} dbname={2} password={3} port={4}".format(self.host, self.user, self.dbname, self.password, self.port)
            conn = psycopg2.connect(conn_string)
            logging.debug("conexion establecida")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory")
            cats=cursor.fetchall()
            for dato in cats:
                print(dato[2])
            cursor.close()
            conn.close()
            logging.debug("conexion terminada")
        except:
            print("Error en la conexion")
            logging.critical("Error en la conexion")
