from Conexion import *
from Consultadispositivo import *

class Agente(Conexion):
    def insertar(self, hostname, versionSNMP, puertoSNMP, comunidad, usuario):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("select idUsuario from Usuario where usuario='" + usuario + "';")
        result = cursor.fetchone()
        idUsuario = str(result[0])
        cursor.execute("insert into Agente values(null,'" + hostname + "','" + str(versionSNMP) + "'," + str(puertoSNMP) + ",'" + comunidad + "',"+ idUsuario+");")
        con.commit()
        self.cerrar(con)

    def eliminar(self,comunidad,usuario):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("delete from Agente where comunidadSNMP = '" +comunidad +"';")
        con.commit()
        self.cerrar(con)

    def mostrarDispositivos(self, usuario):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("select idUsuario from Usuario where usuario='" + usuario + "';")
        result = cursor.fetchone()
        idUsuario = str(result[0])
        cursor.execute("select count(*) from Agente where idUsuario='"+idUsuario+"';")
        result = cursor.fetchone()
        dispositivosMonitorizados = result[0]

        cursor.execute("select * from Agente where idUsuario='" + idUsuario + "';")
        rows = cursor.fetchall()
        hostname = []
        version = []
        comunidad = []
        estados = []
        interfaces = []
        i=0
        for row in rows:
            hostname.append(row[1])
            version.append(row[2])
            comunidad.append(row[4])
            host = hostname.__getitem__(i)
            v = int(version.__getitem__(i))
            com = comunidad.__getitem__(i)
            respuesta = direccionip(host,com,v)

            if(respuesta!=""):
                estados.append('Up')
            else:
                estados.append('Down')
            respuesta = noInterfacesRed(host,com,v)
            interfaces.append(respuesta)
        resultadoGrup = []
        j=0
        for interface in interfaces:
            resultadoInd=[]
            for i in range(0,int(interface)):
                resultado = int(estatusInterfaces(hostname.__getitem__(j),comunidad.__getitem__(j),version.__getitem__(j),i+1))
                if(resultado==1):
                    resultadoInd.append("Up")
                elif(resultado==2):
                    resultadoInd.append("Down")
                elif(resultado==3):
                    resultadoInd.append("Testing")
            j=j+1
            resultadoGrup.append(resultadoInd)

        return [dispositivosMonitorizados, estados, interfaces, resultadoGrup]

    def mostrarEstados(self,usuario):
        con=self.conectar()
        cursor = con.cursor()
        cursor.execute("select idUsuario from Usuario where usuario='" + usuario + "';")
        result = cursor.fetchone()
        idUsuario = str(result[0])
        cursor.execute("select * from Agente where idUsuario='" + idUsuario + "';")
        rows = cursor.fetchall()
        hostname = []
        ip = []
        nombre = []
        version = []
        comunidad = []
        sistemaop = []
        interfaces = []
        tiempo = []
        ubicacion = []
        contacto = []



        i=0
        for row in rows:
            hostname.append(row[1])
            version.append(int(row[2]))
            comunidad.append(row[4])
            ip.append(direccionip(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            nombre.append(nombreDis(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            sistemaop.append(so(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            interfaces.append(noInterfacesRed(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            tiempo.append(tiempoUltimoReinicio(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            ubicacion.append(ubicacionFisica(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
            contacto.append(infContacto(hostname.__getitem__(i),comunidad.__getitem__(i),version.__getitem__(i)))
        estados = [hostname, ip, nombre, version, comunidad, sistemaop, interfaces, tiempo, ubicacion, contacto]
        return estados
