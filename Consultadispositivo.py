from estadoDispositivo import *
from easysnmp import Session

#El host lo recibe xdxd



def nombreHost(hostname_var):

    return hostname_var

def ifInDiscards(hostname, comunity, version):
    session = Session(hostname=hostname, community=comunity, version=version)
    description = str(session.get('1.3.6.1.2.1.2.2.1.13.1'))
    print(description)

def direccionip(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.walk(lista_oid[0]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]


def nombreDis(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[1]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]


def version(versionsnmp):
    return versionsnmp


def so(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[2]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index(" ")
    return sub[:fin]


def noInterfacesRed(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[3]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]

def tiempoUltimoReinicio(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[4]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    milisegundos= int(sub[:fin])
    num= milisegundos/100
    hor = (int(num / 3600))
    minu = int((num - (hor * 3600)) / 60)
    seg = num - ((hor * 3600) + (minu * 60))
    tiempo=str(hor) + "h " + str(minu) + "m " + str(seg) + "s"
    return tiempo


def ubicacionFisica(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[5]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]


def infContacto(hostname, community, version):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get(lista_oid[6]))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]

def estatusInterfaces(hostname, community, version, num):
    session = Session(hostname=hostname, community=community, version=version)
    description = str(session.get('1.3.6.1.2.1.2.2.1.8.' + str(num)))
    inicio = description.index("=")
    sub = description[inicio + 2:]
    fin = sub.index("'")
    return sub[:fin]