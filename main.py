def Ip():
    import urllib
    import urllib.request
    response = urllib.request.urlopen('http://icanhazip.com')
    IPRaw = response.read()
    IP = IPRaw.strip().decode('utf-8')
    return IP

def Apikey(ip,puerto,user,password):
    apikey= user+","+password+","+ ip +","+str(puerto)
    """aqui se hace un deco especial"""
    return apikey
def enviar():
    import smtplib
    from email.MIMEText import MIMEText
    password = ""
    emisor = ""
    receptor = ""
    # Configuracion del mensaje
    mensaje = MIMEText("Este es el contenido del correo enviado desde Python")
    mensaje['From']=emisor
    mensaje['To']=receptor
    mensaje['Subject']="Asunto del correo"

    # Nos conectamos al servidor SMTP de Gmail
    serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
    serverSMTP.ehlo()
    serverSMTP.starttls()
    serverSMTP.ehlo()
    serverSMTP.login(emisor,password)

    # Enviamos el mensaje
    serverSMTP.sendmail(emisor,receptor,mensaje.as_string())

    # Cerramos la conexion
    serverSMTP.close()
print (Apikey(Ip(),52,"felipe","secreto"))
enviar()
