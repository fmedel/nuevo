#libreira base
import sys
import logging
###############################

class IP: #clase que contiene todo lo relacionado con la ip
    def __init__(self,Direccion_Remi="remitente@ejemplo.com",Direccion_Desti="destinatario@ejemplo.com",Contrasenia_Remi="password_remitente"):
        try:
            self.IP_Publica = self.get_ip()
            self.Direccion_Remi = Direccion_Remi
            self.Direccion_Desti = Direccion_Desti
            self.Contrasenia_Remi = Contrasenia_Remi
            self.puerto=8081
            self.Apikey_str=self.Apikey()
        except:
            print("Datos correctamente ingresado de la IP")
            print("Error al cargar los datos de la IP")
            logging.critical("Error: al cargar los datos de la IP")
            sys.exit(1)

    def Apikey(self): #codifica y decodifica  el apikey
        apikey= self.Direccion_Remi+","+self.Contrasenia_Remi+","+ self.IP_Publica +","+str(self.puerto)
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
            Cabecera += 'Subject: ' + Asunto_Mensaje + '\n'
            Cabecera += 'MIME-Version: 1.0 '+'\n'+'Content-type: text/html'+'\n'
            CuerpoMensaje = "Su nueva IP es <b>" +self.IP_Publica+"</b>"+'\n' + '\n'
            EnviarCorreo.sendmail(self.Direccion_Remi, self.Direccion_Desti, Cabecera + CuerpoMensaje)
            EnviarCorreo.close()
            logging.info("Correo enviado a "+self.Direccion_Desti)
            print ("Correo enviado")
        except:
            logging.critical('Error: al enviar el correo a'+self.Direccion_Desti)
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
        try:
            from smtplib import SMTP
            Asunto_Mensaje="La api key "
            EnviarCorreo = SMTP()
            EnviarCorreo.connect("smtp.gmail.com", 587)
            EnviarCorreo.ehlo()
            EnviarCorreo.starttls()
            EnviarCorreo.ehlo()
            EnviarCorreo.login(self.Direccion_Remi, self.Contrasenia_Remi)
            Cabecera = 'To:' + self.Direccion_Desti + '\n'
            Cabecera += 'From: ' + self.Direccion_Remi + '\n'
            Cabecera += 'Subject: ' + Asunto_Mensaje + '\n'
            Cabecera += 'MIME-Version: 1.0 '+'\n'+'Content-type: text/html'+'\n'
            CuerpoMensaje = "La api key es <b>" +self.Apikey_str+"</b>"+'\n' + '\n'
            EnviarCorreo.sendmail(self.Direccion_Remi, self.Direccion_Desti, Cabecera + CuerpoMensaje)
            EnviarCorreo.close()
            logging.info("Correo enviado a "+self.Direccion_Desti)
            print ("Correo enviado")
        except:
            logging.critical('Error: al enviar el correo a'+self.Direccion_Desti)
            print ('Error: al enviar el correo')
            sys.exit(1)

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
