from estadoDispositivo import *
from easysnmp import Session

def obtenerSesion(hostname,community, version, tipo, elementoLista):
    session = Session(hostname=hostname, community=community, version=version)
    if(tipo=="walk"):
        description = str(session.walk(elementoLista))
    elif(tipo=="get"):
        description = str(session.get(elementoLista))
    else:
        description = 'Error'
    
    return description

def obtenerSubcadena(cadena):
    inicio = cadena.index("")
    sub = description[inicio+2:]
    fin = sub.index("'")
    return sub[:fin]

def nombreHost(hostname_var):
    return hostname_var

def direccionip(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"walk",lista_oid[0]))

def nombreDis(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[1]))

def version(versionsnmp):
    return versionsnmp

def so(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[2]))

def noInterfacesRed(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[3]))

def tiempoUltimoReinicio(hostname,community,version):
    subcadena = obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[4]))
    milisegundos= int(sub[:fin])
    num= milisegundos/100
    hor = (int(num / 3600))
    minu = int((num - (hor * 3600)) / 60)
    seg = num - ((hor * 3600) + (minu * 60))
    tiempo=str(hor) + "h " + str(minu) + "m " + str(seg) + "s"
    return tiempo

def ubicacionFisica(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[5]))

def infContacto(hostname,community,version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",lista_oid[6]))

def estatusInterfaces(hostname, community, version, num):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get('1.3.6.1.2.1.2.2.1.8.' + str(num)))
    return obtenerSubcadena(description)

def ifInDiscards(hostname,community, version):
    return obtenerSubcadena(obtenerSesion(hostname,community,version,"get",'1.3.6.1.2.1.2.2.1.13.1'))
