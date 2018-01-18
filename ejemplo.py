try:
    import urllib
    import urllib.request
except:
    logging.critical("Error: al importar libreria urllib")
    print('Error: al importar libreria urllib')
    sys.exit(1)
try:
    pag_web='http://icanhazip.com'
    response = urllib.request.urlopen(pag_web)
    IPRaw = response.read()
    IP = IPRaw.strip().decode('utf-8')
    print(IPRaw)
    print(IP)
except:
    logging.critical("Error: En la pag web para ver la ip")
    print('Error: En la pag web para ver la ip(  '+pag_web+' )')
    sys.exit(1)
