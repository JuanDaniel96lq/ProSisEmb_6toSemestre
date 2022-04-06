class Animal:
    nombre = None
    patas = None
    peso = None
    comida = None
    
    def __init__(self, nombre, patas, peso, comida):
        self.nombre = nombre
        self.patas = patas
        self.peso = peso
        self.comida = comida
        
    def correr(self):
        return "Soy un(a) " + self.nombre + " tengo " + self.patas + " patas y me gusta correr."
  
  
    
class Herbivoro(Animal):
    planta = None
    
    def __init__(self, nombre, patas, peso, comida, planta):
        Herbivoro.__init__(self, nombre, patas, peso, comida)
        self.planta = planta
    
    def comer(self):
        return "Soy herbivoro por eso como " + self.comida + " y la más favorita es " + self.planta
    
    
    
class Carnivoro(Animal):
    carne = None
    
    def __init__(self, nombre, patas, peso, comida, carne):
        Animal.__init__(self, nombre, patas, peso, comida)
        self.carne = carne
        
    def cazar(self):
        return "Soy un carnivoro por eso como " + self.comida + " y debo cazar a para comer " + self.carne
    


class Omnivoro(Herbivoro, Carnivoro):
    
    def __init__(self, nombre, patas, peso, comida, planta, carne):
        Animal.__init__(self, nombre, patas, peso, comida)
        self.planta = planta
        self.carne = carne
        
    def print(self):
        print("Soy un omnivoro y tambien \n" + self.cazar() + "\n" + self.comer())
        
        

Instancia = Omnivoro("Perro", "4", "25 kg", "Carne y Plantas", "Diente de León", "Carne de Res")
Instancia.print()