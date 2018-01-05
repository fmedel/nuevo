# pip3 install simplejson
#####################################
#libreira base
import sys
import logging
import simplejson as json
from base_dato import *
#####################################
class plantas():
    def __init__(self,arg):
        self.nivel_agua = arg["nivel del agua"]
        self.temperatura_h = arg["temperatura_h"]
        self.humedad_h = arg["humedad_h"]
        self.planta=arg["planta"]
    def nivel_agua_f(self,nivel_minimo): #entrega false si el nivel de agua llega a un % dado
        try:
            if (self.nivel_agua) > nivel_minimo:
                return True
            else:
                return False
        except:
            print("Error en el nivel agua")
            logging.critical("Error en el nivel agua")
            sys.exit(1)
    def temperatura_h_f(self,temperatura_maxima): #entrega false si el temperatura_maxima llega a un % dado
        try:
            if (self.temperatura_h) <temperatura_maxima:
                return True
            else:
                return False
        except:
            print("Error en la temperatura ambiente")
            logging.critical("Error en la temperatura ambiente")
            sys.exit(1)
    def humedad_h_f(self,humedad_maxima): #entrega false si el humedad_maxima llega a un % dado
        try:
            if (self.humedad_h) <humedad_maxima:
                return True
            else:
                return False
        except:
            print("Error en el humedad ambiente")
            logging.critical("Error en el humedad ambiente")
            sys.exit(1)
    def ver_datos_por_planta(self): #entrega los datos de las plantas ingresada
        try:
            contador_planta=0
            while contador_planta <len(self.planta):
                print(self.planta_id(contador_planta))
                contador_planta+=1
        except:
            print("Error enver datos por planta")
            logging.critical("Error en ver datos por planta")
            sys.exit(1)
    def dicionario_comun(self): #entrea un dicionario con los datos en comun en las plantas
        try:
            dicionario={"nivel del agua":self.nivel_agua,"temperatura ambiente":self.temperatura_h,"humedad ambiente":self.humedad_h}
            return dicionario
        except:
            print("Error en el dicionario de datos comun")
            logging.critical("Error en el dicionario de datos comun")
            sys.exit(1)
    def planta_id(self,id_p) : #entrega los datos de la planta dado su id
        try:
            planta = {"id":self.planta[id_p]["id"],"humedad_tierra":self.planta[id_p]["humedad_tierra"],"regar":self.planta[id_p]["regar"],"id_planta":self.planta[id_p]["id_planta"]}
            return planta
        except:
            print("Error en planta id")
            logging.critical("Error en planta id")
            sys.exit(1)
    def set_plantas(self,arg): #setiar todos los valores de la plantas t
        try:
            self.set_nivel_agua(arg["nivel del agua"])
            self.set_temperatura_h(arg["temperatura_h"])
            self.set_humedad_h(arg["humedad_h"])
            self.set_planta(arg["planta"])
        except:
            print("Error en set pantas")
            logging.critical("Error en set pantas")
            sys.exit(1)
    def set_nivel_agua(self,nivel):#setiar el valor de nivel agua
        try:
            self.nivel_agua = nivel
        except:
            print("Error en set nivel agu|a")
            logging.critical("Error en set nivel agua")
            sys.exit(1)
    def set_temperatura_h(self,temp):#setiar el valor de temperatura ambiente
        try:
            self.temperatura_h = temp
        except:
            print("Error en set temperatura")
            logging.critical("Error en set temperatura")
            sys.exit(1)
    def set_humedad_h(self,hum):#setiar el valor de humedad ambiente
        try:
            self.humedad_h = hum
        except:
            print("Error en set humerdad ambiente")
            logging.critical("Error en set humerdad ambiente")
            sys.exit(1)
    def set_planta(self,plan):#setiar el valor de plantas
        try:
            self.planta = plan
        except:
            print("Error en set planta")
            logging.critical("Error en set planta")
            sys.exit(1)

if __name__ == '__main__':
    users = {
            "nivel del agua":50,
            "temperatura_h":223,
            "humedad_h":222,
            "planta":[
                        {"id":1,"humedad_tierra":3234,"regar":True,"id_planta":45},
                        {"id":2,"humedad_tierra":323,"regar":True,"id_planta":21},
                        {"id":3,"humedad_tierra":323,"regar":False,"id_planta":2}
                    ]
            }

    data = json.dumps(users, sort_keys=True, indent=1 * ' ')
    d = json.loads(data)
    planta=plantas(d)
    planta.nivel_agua_f(41)
    planta.ver_datos_por_planta()
    base=conexion_base_datos()
    base.crear_bd()
    base.cargar_datos()
    base.listar_all("inventario")
    base.configuracion()
