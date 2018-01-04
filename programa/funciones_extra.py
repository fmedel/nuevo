#libreira base
import sys
import logging
from configuracion import *
from ip import *
###############################

def archivo_exite(archivo): #verificar si exite el archivo
    try:
        import os.path as path
        if path.exists(archivo):
            return True
        else:
            return False
    except:
        logging.critical("Error en la busqueda del archivo "+archivo )
        sys.exit(1)

def reniciar_log(): # reniciar  el archivo log para ahorar espacio
    try:
        archivo = open('.log_aplicacio.log','w')
        archivo.close
    except:
        print("Error al reniciar el log")
        sys.exit(1)

def argumentos(): #aqui es donde estan los parametros
    import argparse
    parser = argparse.ArgumentParser()
    # argumentos opcional
    parser.add_argument("-i","--iniciar", help="Ejecutar el programa", action="store_true")
    parser.add_argument("-c", "--config", help="Entrar en la configuración", action="store_true")
    parser.add_argument("-r", "--reniciar", help="Reniciar el log", action="store_true")
    parser.add_argument("-l", "--log", help="Ver el log", action="store_true")
    parser.add_argument("-ip", "--ip", help="Comprobar la ip publica cada 10 minuto", action="store_true")
    parser.add_argument("-e", "--email", help="Enviar email con la direción publica", action="store_true")
    parser.add_argument("-d", "--dest", help="Email del destinatario")
    parser.add_argument("-ak", "--apikey", help="Enviar email con la apikey", action="store_true")
    parser.add_argument("-v", "--ver", help="ver datos [ip | api key]",choices=['ip', 'api'])
    args = parser.parse_args()
    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.ver:
        if not archivo_exite(".env"): #revisar si exite archivo env
            print("No se encuentra el archivo de configuración (enviar emial ip publica)")
            logging.critical("No se encuentra el archivo de configuración (enviar emial ip publica)")
            sys.exit(1)
        datos=leer_configuracion()
        ip = IP(datos["remitente"],datos["destinatario"],datos["clave"])
        if  args.ver=='api':
            print(ip.Apikey_str)
            sys.exit(1)
        else:
            print(ip.IP_Publica)
            sys.exit(1)
    if args.iniciar:
        return 2
    if args.reniciar:
        reniciar_log()
        sys.exit(1)
    if args.log:
        import os
        logging.info("Entro en modo monitor del log")
        os.system('tail -f .log_aplicacio.log ')
        logging.info("Se salio de modo monitor del log")
        sys.exit(1)
    if args.config:
        config()
        logging.info("Salio de la creación de archivo configuración")
        sys.exit(1)
    if args.email:
        if not archivo_exite(".env"): #revisar si exite archivo env
            print("No se encuentra el archivo de configuración (enviar emial ip publica)")
            logging.critical("No se encuentra el archivo de configuración (enviar emial ip publica)")
            sys.exit(1)
        datos=leer_configuracion()
        if args.dest:
            import re
            if(not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',args.dest.lower()))):
                print("No es una direción de email valida para enviar email")
                logging.critical("No es una direción de email valida para enviar email")
                sys.exit(1)
            else:
                datos["destinatario"] =args.dest
        ip = IP(datos["remitente"],datos["destinatario"],datos["clave"])
        logging.info("Se entro en enviar email IP publica")
        ip.enviar_email()
        logging.info("Se salio en enviar email IP publica")
        sys.exit(1)
    if args.apikey:
        if not archivo_exite(".env"): #revisar si exite archivo env
            print("No se encuentra el archivo de configuración (enviar emial ip publica)")
            logging.critical("No se encuentra el archivo de configuración (enviar emial ip publica)")
            sys.exit(1)
        datos=leer_configuracion()
        if args.dest:
            import re
            if(not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',args.dest.lower()))):
                print("No es una direción de email valida para enviar email")
                logging.critical("No es una direción de email valida para enviar email")
                sys.exit(1)
            else:
                datos["destinatario"] =args.dest
        logging.info("Se entro en enviar email Api key")
        ip = IP(datos["remitente"],datos["destinatario"],datos["clave"])
        ip.enviar_Apikey(False)
        logging.info("Se salio en enviar email Api key")
        sys.exit(1)
    if args.ip:
        print("Cada una hora se comprobar la ip publica")
        logging.info("Entro en modo de comprobar ip publica")
        import time
        ip = IP()
        try:
            while True:
                ip.comprobar_ip_publica()
                print("temporal")
                time.sleep(3600)
        except:
            logging.info("Se salio de modo comprobación de ip")
            sys.exit(1)
