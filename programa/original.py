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

def reniciar_log(): # reniciar  el archivo log para ahorar espacio
    try:
        archivo = open('.log_aplicacio.log','w')
        archivo.close
    except:
        print("Error al reniciar el log")
        sys.exit(1)

class IP: #clase que contiene todo lo relacionado con la ip
    def __init__(self,Direccion_Remi="remitente@ejemplo.com",Direccion_Desti="destinatario@ejemplo.com",Contrasenia_Remi="password_remitente"):
        try:
            self.IP_Publica = self.get_ip()
            self.Direccion_Remi = Direccion_Remi
            self.Direccion_Desti = Direccion_Desti
            self.Contrasenia_Remi = Contrasenia_Remi
            self.puerto=8081
            print("Datos correctamente ingresado de la IP")
        except:
            print("Error al cargar los datos de la IP")
            logging.critical("Error: al cargar los datos de la IP")
            sys.exit(1)

    def get_ip(self): # entrega la ip publica
        try:
            logging.debug("Optener la ip publica")
            import urllib
            import urllib.request
            response = urllib.request.urlopen('http://icanhazip.com')
            IPRaw = response.read()
            IP = IPRaw.strip().decode('utf-8')
            logging.info("La ip publica es "+IP)
            return IP
        except:
            logging.critical("Error: al recojer la ip")
            print('Error: al recojer la ip')
            sys.exit(1)

    def enviar_email(self): # envia email cuando la ip cambia
        try:
            from smtplib import SMTP
            Asunto_Mensaje="Cambio de IP publica "
            EnviarCorreo = SMTP()
            EnviarCorreo.connect("smtp.gmail.com", 587)
            EnviarCorreo.ehlo()
            EnviarCorreo.starttls()
            EnviarCorreo.ehlo()
            EnviarCorreo.login(self.Direccion_Remi, self.Contrasenia_Remi)
            Cabecera = 'To:' + self.Direccion_Desti + '\n'
            Cabecera += 'From: ' + self.Direccion_Remi + '\n'
            Cabecera += 'Subject: ' + Asunto_Mensaje + '\n'+'\n'
            CuerpoMensaje = "Su nueva IP es <b>" +self.IP_Publica+"</b>"+'\n' + '\n'
            EnviarCorreo.sendmail(self.Direccion_Remi, self.Direccion_Desti, Cabecera + CuerpoMensaje)
            EnviarCorreo.close()
            logging.info("Correo enviado a "+self.Direccion_Desti)
            print ("Correo enviado")
        except:
            logging.critical('Error: al enviar el correo a'+Direccion_Desti)
            print ('Error: al enviar el correo')
            sys.exit(1)

    def crear_archivo(self): # crea el archivo donde se guarda la ip publica
        try:
            archivo = open('.ip','w')
            archivo.write(self.IP_Publica+ '\n')
            archivo.close
            logging.debug('Creacion correctamente del archivo ip')
        except:
            logging.critical('Error al crear archivo ip')
            print("Error al crear archivo ip ")
            sys.exit(1)

    def enviar_Apikey(self,Destinatario):
        if Destinatario==False:
            Destinatario= self.Direccion_Desti
        ##try:
            from smtplib import SMTP
            Asunto_Mensaje="Key de la api"
            EnviarCorreo = SMTP()
            EnviarCorreo.connect("smtp.gmail.com", 587)
            EnviarCorreo.ehlo()
            EnviarCorreo.starttls()
            EnviarCorreo.ehlo()
            EnviarCorreo.login(self.Direccion_Remi, self.Contrasenia_Remi)
            Cabecera = 'To:' + Destinatario + '\n'
            Cabecera += 'From: ' + self.Direccion_Remi + '\n'
            Cabecera += 'Subject: ' + Asunto_Mensaje + '\n'+'\n'
            CuerpoMensaje = "La key de la api es: <b>" + Apikey(self.IP_Publica,self.puerto,self.Direccion_Remi,self.Contrasenia_Remi)+"</b>"+'\n' + '\n'
            EnviarCorreo.sendmail(self.Direccion_Remi,Destinatario, Cabecera + CuerpoMensaje)
            EnviarCorreo.close()
            logging.debug("Correo enviado a "+self.Direccion_Desti+' keyAPi')
            print ("Correo enviado keyAPi")
        ##except:
            ##logging.critical('Error: al enviar el correo a'+self.Direccion_Desti +' keyAPi')
            ##print ('Error: al enviar el correo keyAPi')
            ##sys.exit(1)

    def comprobar_ip_publica(self): # comprueba la ip publicas y informa cuando cambia
        try:
            archivo = open('.ip','r')
            ip = archivo.read()
            archivo.close
            if ip!=(self.IP_Publica+'\n'):
                self.crear_archivo()
                self.enviar_email()
                logging.info('Cambio de la ip publica a '+self.IP_Publica)
        except:
            logging.critical('Error al leer el archivo ip')
            print("Error al leer el archivo ip ")
            sys.exit(1)

def Apikey(ip,puerto,user,password): #codifica y decodifica  el apikey
    apikey= user+","+password+","+ ip +","+str(puerto)
    apikey_codificada=""
    dicionario={'!' : '0ap',' ' : '1bq','#' : '2cr','$' : '3ds','%' : '4et','&' : '5fu','\'' : '6gv','(' : '7hL',')' : '8iM','*' : '9jN','+' : 'akO',',' : 'blP','-' : 'cmQ','.' : 'dnR','/' : 'eoS',':' : 'fpT',';' : 'gqU','<' : 'hrV','=' : 'isW','>' : 'jtX','?' : 'kuY','@' : 'lvZ','[' : 'mwa',']' : 'nxb','^' : 'oyc','_' : 'pzd','`' : 'qAe','{' : 'rBf','}' : 'sCg','|' : 'tDh','0' : 'uEi','1' : 'vFj','2' : 'wGk','3' : 'xHl','4' : 'yIm','5' : 'zJn','6' : 'AKo','7' : 'BLw','8' : 'CMx','9' : 'DNy','a' : 'EOz','b' : 'FP1','c' : 'GQ2','d' : 'HR3','e' : 'IS4','f' : 'JT5','g' : 'KU6','h' : 'LV7','i' : 'MW8','j' : 'NX9','k' : 'OYA','l' : 'PZB','m' : 'Q0C','n' : 'R1D','o' : 'S2E','p' : 'T3F','q' : 'U4G','r' : 'V5H','s' : 'W6I','t' : 'X7J','u' : 'Y8K','v' : 'Z9','w' : '','x' : '','y' : '','z' : '','A' : 'Z9','B' : 'Y8K','C' : 'X7J','D' : 'W6I','E' : 'V5H','F' : 'U4G','G' : 'T3F','H' : 'S2E','I' : 'R1D','J' : 'Q0C','K' : 'PZB','L' : 'OYA','M' : 'NX9','N' : 'MW8','O' : 'LV7','P' : 'KU6','Q' : 'JT5','R' : 'IS4','S' : 'HR3','T' : 'GQ2','U' : 'FP1','V' : 'EOz','W' : 'DNy','X' : 'CMx','Y' : 'BLw','Z' : 'AKo','' : 'zJn','' : 'yIm'}
    for value in apikey:
        try:
            apikey_codificada+=dicionario[value]
        except:
            apikey_codificada+=value
    logging.debug("codificación complate a de la apikey")
    logging.info("la apikey es "+apikey_codificada)
    return apikey_codificada

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
    args = parser.parse_args()
    # Aquí procesamos lo que se tiene que hacer con cada argumento
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

def conexion_base_datos(): #conexion con la bases de datos PostgreSQL
    pass


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
        logging.debug(" inicio del programa")
        datos=leer_configuracion()
        ip = IP(datos["remitente"],datos["destinatario"],datos["clave"])
        #ip.enviar_email()
        ip.crear_archivo()
    else:
        import os
        os.system('python3 main.py -h')
