# -*- coding: utf-8 -*-

#libreira base
import sys
import logging
###############################
from funciones_extra import *
from ip import *
from base_dato import *
from configuracion import *

if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(format='%(levelname)s - %(message)s',filename=".log_aplicacio.log", level=logging.DEBUG)
    resultado=argumentos() #resultado del menu por argumento
    if resultado==2: #revisar si se elige iniciar
        if not archivo_exite(".env"): #revisar si exite archivo env
            print("No se encuentra el archivo de configuración")
            logging.critical("No se encuentra el archivo de configuración")
            sys.exit(1)
        print("Inicio del programa")
        logging.debug("inicio del programa")
        datos=leer_configuracion()
        ip = IP(datos["remitente"],datos["destinatario"],datos["clave"])
        #ip.enviar_email()
        ip.crear_archivo()
        base=conexion_base_datos()
        base.crear_bd()
        base.cargar_datos()
        base.listar_all()
        print("Fin del programa")
    else:
        import os
        os.system('python3 main.py -h')
