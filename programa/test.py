
def funciones_extra_test():
    try:
        print("Testiando el archivo funciones_extra.py")
        try:
            from funciones_extra import archivo_exite , reniciar_log
        except:
            print("\tError en import el archivo funciones_extra.py")
            print("\tSe para el testeo de funciones_extra.py")
            return 0
        try:
            print("\tTestiando la funcion archivo_exite ")
            archivo_exite("test.py")
            print("\t\tTest completo")
        except:
            print("\t\tError en la funcion archivo_exite")
        try:
            print("\tTestiando la funcion reniciar_log")
            reniciar_log()
            print("\t\tTest completo")
        except:
            print("\t\tError en la funcion reniciar_log")
    except:
        print("Error en el archivo_exite.py")

def ip_f():
    print("Testiando el archivo ip.py")
    try:
        try:
            from ip import IP
        except:
            print("\tError en import de archivo ip.py")
            print("\tSe para el testeo de ip.py")
            return 0
        try:
            print("\tTestiando el init de ip")
            ip=IP()
            print("\t\tTest completo")
        except:
            print("\t\tError en init")
            print("\tSe para el testeo de ip.py")
            return 0
        try:
            print("\tTestiando Apikey")
            ip.Apikey()
            print("\t\tTest completo")
        except:
            print("\t\tError en Apikey")
        try:
            print("\tTestiando get_ip")
            ip.get_ip()
            print("\t\tTest completo")
        except:
            print("\t\tError en get_ip")
        try:
            print("\tTestiando crear_archivo")
            ip.crear_archivo()
            print("\t\tTest completo")
        except:
            print("\t\tError en crear_archivo")
        try:
            print("\tTestiando comprobar_ip_publica")
            ip.comprobar_ip_publica()
            print("\t\tTest completo")
        except:
            print("\t\tError en comprobar_ip_publica")
        try:
            print("\tTestiando enviar_email")
            try:
                from configuracion import leer_configuracion
                datos=leer_configuracion()
                ip2 = IP(datos["remitente"],datos["destinatario"],datos["clave"])
            except:
                print("\t\tError en enviar_email")
                return 0
            #print("-------------------------------------------------------")
            #ip2.enviar_email()
            #print("-------------------------------------------------------")
            print("\t\tTest completo")
        except:
            print("\t\tError en enviar_email")
        try:
            print("\tTestiando enviar_Apikey")
            #print("-------------------------------------------------------")
            #ip2.enviar_Apikey(False)
            #print("-------------------------------------------------------")
        except:
            print("\t\tError en enviar_Apikey")
    except:
        print("Error en ip.py")

def configuracion_f():
    try:
        print("Testiando el archivo configuracion.py")
        try:
            from configuracion import leer_configuracion,config
        except:
            print("\tError en import configuracion.py")
            print("\tSe para el testeo de configuracion.py")
            return 0
        try:
            print("\tTestiando leer_configuracion")
            leer_configuracion()
            print("\t\tTest completo")
        except:
            print("\t\tError en leer_configuracion")
        try:
            print("\tTestiando config")
            #print("-------------------------------------------------------")
            #config()
            #print("-------------------------------------------------------")
            print("\t\tTest completo")
        except:
            print("\t\tError en config")

    except:
        print("Error en el archivo configuracion.py")

def base_dato_f():
    try:
        print("Testiando el archivo base_dato.py")
        try:
            from base_dato import conexion_base_datos
        except:
            print("\tError en import configuracion.py")
            print("\tSe para el testeo de configuracion.py")
            return 0
        try:
            print("\tTestiando init")
            base=conexion_base_datos()
            print("\t\tTest completo")
        except:
            print("\t\tError en la init")
        try:
            print("\tTestiando conexion")
            if base.conectar_test() ==1:
                print("\t\tError en la conexion revise los datos")
            else:
                print("\t\tTest completo")
        except:
            print("\t\tError en la conexio")
        try:
            print("\tTestiando el configuración")
            base.configuracion()
            print("\t\tTest completo")
        except:
            print("\tError en import configuración")
    except:
        print("Error en el archivo base_dato.py")

def json_e.py():
    pass
if __name__ == '__main__':
    print("***** inicio del testeo ******")
    print("")
    funciones_extra_test()
    print("")
    configuracion_f() # config descomnetar para testiarla
    print("")
    ip_f() #enviar_email y enviar_Apikey descomnetar para testiarla
    print("")
    base_dato_f()
    print("")
    print("")
    print("***** Fin del testeo ******")
