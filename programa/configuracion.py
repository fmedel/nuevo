#libreira base
import sys
import logging
###############################

def leer_configuracion(): #leer el archivo env y entrga un dicionario con los datos
    try:
        archivo = open('.env','r')
    except:
        logging.critical("Error en la lectura del archivo de configuración ")
        sys.exit(1)
    contador=1
    for line in archivo:
        if contador==1:
            remitente=line.rstrip('\n') #eliminar el salto de linea
        if contador==2:
            destinatario = line.rstrip('\n')
        if contador==3:
            clave= line.rstrip('\n')
        contador+=1
    dic_datos={"destinatario":destinatario,"remitente":remitente,"clave":clave}
    return dic_datos

def config(): # crea el archivo donde se guardan los datos de configuracion
    try:
        import re
        remitente = ""
        destinatario = ""
        password = ""
        while (not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',remitente.lower()))): #verificar el email remitente
            remitente = input("¿Cual es su email? ")
        while (not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',destinatario.lower()))): #verificar el email destinatario
            destinatario = input("¿Cual es el email donde se enviaran los mensajes ? ")
        while (not(re.match('^[(a-z0-9\_\-\.A-Z)]{2,24}$',password))): #verificar el password email remitente
            password = input("¿Cual es la clave de su email? ")
        archivo = open('.env','w')
        archivo.write(remitente+'\n')
        archivo.write(destinatario+'\n')
        archivo.write(password+'\n')
        archivo.close
        logging.debug("Archivo de configuracion creado")
    except:
        print("Error al crear archivo env ")
        logging.critical("Error al crear archivo env")
        sys.exit(1)
