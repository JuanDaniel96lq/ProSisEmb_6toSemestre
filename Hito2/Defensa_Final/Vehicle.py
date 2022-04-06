class Vehicle:
    color = None
    wheels = None
    
    def __init__(self, Color, Wheels):
        self.color = Color
        self.wheels = Wheels
        
    def __str__(self):
        return f'Color: {self.color}\nRuedas: {self.wheels}'
        
    def travel(self):
        print("Viajando...")

       
class Bicycle(Vehicle):
    saddles = None
    chain_drive = None
    
    def __init__(self, Color, Wheels, Saddles, Chain_drive):
        Vehicle.__init__(self, Color, Wheels)
        self.saddles = Saddles
        self.chain_drive = Chain_drive
    
    def __str__(self):
        return Vehicle.__str__(self) + "\nSillin:" + self.saddles + "\nTransmisión de Cadena: " + self.chain_drive
        
    def Start(self):
        print("Arrancando...")
    
    def Accelerate(self):
        print("Acelerando...")
        

class Car(Vehicle):
    seats = None
    engine = None
    
    def __init__(self, Color, Wheels, Seats, Engine):
        Vehicle.__init__(self, Color, Wheels)
        self.seats = Seats
        self.engine = Engine
    
    def __str__(self):
        return Vehicle.__str__(self) + "\nAsientos: " + self.seats + "\nMotor: " + self.engine
    
    def Start(self):
        print("Arrancando...")
    
    def Accelerate(self):
        print("Acelerando...")
        

v1 = Vehicle("Rojo", "18")
v2 = Bicycle("Negro", "2", "De cuero", "Simple")
v3 = Bicycle("Blanco", "4", "De cuero", "v6")
print("============================")
print(v1)
v1.travel()
print("============================")
print(v2)
v2.travel()
v2.Start()
v2.Accelerate()
print("============================")
print(v3)
v3.travel()
v3.Start()
v3.Accelerate()
print("============================")