class Jugador:
    __nombreCompleto = None
    __apellidos = None
    __ci = None
    __edad = None

    def __init__(self, nombres, apellidos, ci, edad):
        self.__nombreCompleto = nombres
        self.__apellidos = apellidos
        self.__ci = ci
        self.__edad = edad

    def get_nombreCompleto(self):
        return self.__nombreCompleto

    def set_nombreCompleto(self, text):
        self.__nombreCompleto = text

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, text):
        self.__apellidos = text

    def get_ci(self):
        return self.__ci

    def set_ci(self, text):
        self.__ci = text

    def get_edad(self):
        return self.__edad

    def set_edad(self, num):
        self.__edad = num

    def imprimir(self):
        print(self.__nombreCompleto, '\t', self.__apellidos, '\t', self.__ci, '\t', self.__edad)


class Equipo:
    __nombreEquipo = None
    __categoria = None
    __jugadores = []

    def __init__(self, nombreEquipo, categoria, jugadores):
        self.__nombreEquipo = nombreEquipo
        self.__categoria = categoria
        self.__jugadores = jugadores

    def get_nombreEquipo(self):
        return self.__nombreEquipo

    def set_nombreEquipo(self, text):
        self.__nombreEquipo = text

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, text):
        self.__categoria = text

    def get_jugadores(self):
        return self.__jugadores

    def set_jugadores(self, num):
        self.__jugadores = num

    def imprimir(self):
        print(self.__nombreEquipo, ' ', self.__categoria)

        i = 0
        while i< len(self.__jugadores):
            self.__jugadores[i].imprimir()
            i += 1

class Campeonato:
    __nombreCampeonato = None
    __equipos = []

    def __init__(self, nombreCampeonato, equipos):
        self.__nombreCampeonato = nombreCampeonato
        self.__equipos = equipos

    def get_nombreCampeonato(self):
        return self.__nombreCampeonato

    def set_nombreCamponato(self, text):
        self.__nombreCampeonato = text

    def get_equipos(self):
        return self.__equipos

    def set_equipos(self, num):
        self.__equipos = num

    def imprimir(self):
        print(self.__nombreCampeonato, ' ')

        i = 0
        while i< len(self.__equipos):
            self.__equipos[i].imprimir()
            i += 1


jugador0 = Jugador("Daniel", "Laura", "10021571 CB", "18")
jugador1 = Jugador("Adri", "Laura", "13356255 LP", "21")
jugador2 = Jugador("Luis", "Lima", "10081571 LP", "25")
jugador3 = Jugador("Samuel", "Ruiz", "13376255 LP", "35")
jugador4 = Jugador("Amanda", "Rojas", "10021671 OR", "20")

jugadores = [None for _ in range(5)]
jugadores[0] = jugador0
jugadores[1] = jugador1
jugadores[2] = jugador2
jugadores[3] = jugador3
jugadores[4] = jugador4

equipo1 = Equipo("FALAQUI", "Mixto", jugadores)

equipos = [None for _ in range(1)]
equipos[0] = equipo1

campeonato = Campeonato("Unifranz", equipos)

campeonato.imprimir()