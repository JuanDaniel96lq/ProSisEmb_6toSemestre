class PoweredDevice:
    voltaje = None
    Amperaje = None
    Marca = None
    Modelo = None
    
    def __init__(self, V, A, Marca, Modelo):
        self.voltaje = V
        self.Amperaje = A
        self.Marca = Marca
        self.Modelo = Modelo
        
    def __str__(self):
        return f'Datos\nVoltaje: {self.voltaje}\nAmperaje: {self.Amperaje}\nMarca: {self.Marca}\nModelo: {self.Modelo}'
    
    def on(self):
        print("Prendiendo dispositivo...")
        
    def off(self):
        print("Apagando dispositivo...")
        

class Scanner(PoweredDevice):
    velocidad = None
    
    def __init__(self, V, A, Marca, Modelo, Velocidad):
        PoweredDevice.__init__(self, V, A, Marca, Modelo)
        self.velocidad = Velocidad
    
    def __str__(self):
        return super().__str__() + "\nVelocidad: " + self.velocidad
    
    def escanear(self):
        print("Escaneando...")
        

class Printer(PoweredDevice):
    tinta = None
    capacidad = None
    
    def __init__(self, V, A, Marca, Modelo, Tinta, Capacidad):
        PoweredDevice.__init__(self, V, A, Marca, Modelo)
        self.tinta = Tinta
        self.capacidad = Capacidad
    
    def __str__(self):
        return PoweredDevice.__str__(self) + "\nTinta: " + self.tinta + "\nCapacidad: " + self.capacidad
        
    def imprimir(self):
        print("Imprimiendo...")

class Copier(Scanner, Printer):
    Wifi = None
    
    def __init__(self, V, A, Marca, Modelo, Velocidad, Tinta, Capacidad, Wifi):
        Scanner.__init__(self, V, A, Marca, Modelo, Velocidad)
        Printer.__init__(self, V, A, Marca, Modelo, Tinta, Capacidad)
        self.Wifi = Wifi
    
    def __str__(self):
        return Printer.__str__(self) + "\nVelocidad: " + str(Scanner.velocidad) + "\nWifi: " + self.Wifi
    
    def Conectar(self):
        print("Conectando a red...")
        

Dispositivo = Copier("220V", "1A", "Epson", "L355", "1/10 seg", "Continua", "5Kg", "Si")
print(Dispositivo)
Dispositivo.Conectar()