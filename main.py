# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random


class TrashCity():
    _instance = None
    def __init__(self):
        self.camiones = {}
        self.usuarios = []
        self.rutas = {}
        self.materiales = {}
        self.cantidadv = 0
        self.cantidadpa = 0
        self.cantidadp = 0
        self.cantidadm = 0
        self.cantidado = 0
        self.vidriorutas = 0
        self.vidriodia = {}

    @staticmethod
    def obtenerInstancia():
        if TrashCity._instance is None:
            TrashCity._instance = TrashCity()
        return TrashCity._instance



    def empezarTurno(self, nombreRuta, idCamion):
            for i in self.rutas[nombreRuta]:
                pesoVidrio = random.uniform(0, 40)
                pesoPapel = random.uniform(0, 40)
                pesoPlastico = random.uniform(0, 40)
                pesoMetal = random.uniform(0, 40)
                pesoOrganicos = random.uniform(0, 40)
                self.recoger(pesoVidrio, pesoPapel, pesoPlastico, pesoMetal, pesoOrganicos)
            print("El camión con id ",idCamion," ha iniciado la ruta llamada ", nombreRuta)

    def recoger(self, pesoVidrio, pesoPapel, pesoPlastico, pesoMetal, pesoOrganicos):
        self.cantidadv += float("%.2f" % pesoVidrio)
        self.cantidadpa += float("%.2f" % pesoPapel)
        self.cantidadp += float("%.2f" % pesoPlastico)
        self.cantidadm += float("%.2f" % pesoMetal)
        self.cantidado += float("%.2f" % pesoOrganicos)
        self.materiales.update(
            {"Vidrio": self.cantidadv, "Papel": self.cantidadpa, "Plástico": self.cantidadp, "Metal": self.cantidadm,
             "Organicos": self.cantidado})

    def terminarTurno(self, idCamion):
        self.vidriorutas += self.materiales["Vidrio"]
        self.cantidadv = 0
        self.cantidadpa = 0
        self.cantidadp = 0
        self.cantidadm = 0
        self.cantidado = 0
        self.camiones[idCamion] = False
        print("El camión con id ",idCamion," ha terminado la ruta")

    def finalizarDia(self, dia):
        self.vidriodia[dia] = self.vidriorutas
        self.vidriorutas=0

class personal(TrashCity):
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        TrashCity.usuarios.append(self.id)

class Ruta(TrashCity):
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaRuta = []

    def generarRuta(self, numPuntos):
        i=0
        while(i<=numPuntos):
            altitud = random.randint(100, 10000)
            longitud = random.randint(100, 10000)
            self.listaRuta.append((altitud, longitud))
            i = i+1
        TrashCity.rutas[self.nombre] = self.listaRuta


class Camion(TrashCity):
    def __init__(self, id):
        if (len(TrashCity.usuarios) >= 3):
            self.ruta = []
            self.vidriodia = {}
            self.id = id
            self.cantidadv = 0
            self.cantidadpa = 0
            self.cantidadp = 0
            self.cantidadm = 0
            self.cantidado = 0
            self.materiales = {"Vidrio": self.cantidadv, "Papel": self.cantidadpa, "Plástico": self.cantidadp,
                               "Metal": self.cantidadm, "Organicos": self.cantidado}
            self.vidrioruta = 0
            self.vidriototal = 0
            ##self.enRuta = False
            TrashCity.camiones[self.id] = False
            print(TrashCity.camiones)
        else:
            print("Debe tener al menos tres usuarios")



    def dia(self, id):
        vidriodia = {}
        self.vidriototal = 0
        for i in range(self.numRutas):
            self.empezarTurno()
            self.vidriototal += self.vidrioruta
            self.vidriodia.update({id: self.vidriototal})
            self.cantidadv = 0
            self.cantidadpa = 0
            self.cantidadp = 0
            self.cantidadm = 0
            self.cantidado = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TrashCity = TrashCity()
    personas = 1
    camiones = 1
    rutas= 1
    dia=1

    while True:
        op = int(input("Digite lo que desee realizar:\n1. Agregar Personal \n2. Agregar Camión\n3. Agregar Ruta\n4. Empezar Turno\n5. Finalizar Turno\n6. Finalizar Día\n7. Calcular cantidad de vidrio por día\n8. Salir\n-> "))
        if(op==8):
            print("Gracias por usar nuestros servicios")
            break
        elif(op==1):
            nombreUsuario = input("Digite el nombre del usuario a crear: ")
            idUsuario = int(input("Digite el id del usuario a crear: "))
            persona = personal(nombreUsuario, idUsuario)
            personas = personas + 1
            print(TrashCity.usuarios)
        elif(op==2):
            print(TrashCity.camiones)
            camion = Camion(int(camiones))
            print("El id el camion creado es ", camiones)
            camiones = camiones+1
        elif(op==3):
            nombreRuta = input("Digite el nombre de la ruta a crear: ")
            puntosRuta = int(input("Digite el número de puntos geograficos de la ruta: "))
            ruta = Ruta(nombreRuta)
            ruta.generarRuta(puntosRuta)
        elif(op==4):
            camion = int(input("Digite el id del camion que va a empezar turno: "))
            while(camion not in TrashCity.camiones.keys()):
                print("El id del camión no existe")
                camion = int(input("Digite el id del camion que va a empezar turno: "))
            ruta = input("Digite el nombre de la ruta: ")
            while (ruta not in TrashCity.rutas.keys()):
                print("El id de la ruta no existe")
                ruta = int(input("Digite el nombre de la ruta: "))
            conductor = int(input("Digite el id del conductor: "))
            while (conductor not in TrashCity.usuarios):
                print("El id del usuario no existe")
                conductor = int(input("Digite el id del conductor: "))
            asistente1 = int(input("Digite el id del asistente 1: "))
            while (asistente1 not in TrashCity.usuarios):
                print("El id del usuario no existe")
                asistente1 = int(int(input("Digite el id del asistente 1: ")))
            asistente2 = int(input("Digite el id del asistente 2: "))
            while (asistente2 not in TrashCity.usuarios):
                print("El id del usuario no existe")
                asistente2 = int(input("Digite el id del asistente 2: "))
            TrashCity.empezarTurno(ruta, camion)
        elif(op==5):
            camion = input("Digite el id del camión: ")
            TrashCity.terminarTurno(camion)
            print(TrashCity.materiales)
        elif(op==6):
            TrashCity.finalizarDia(dia)
        elif(op==7):
            dia = input("Escriba el número del dia: ")
            print(TrashCity.vidriodia[dia])





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
