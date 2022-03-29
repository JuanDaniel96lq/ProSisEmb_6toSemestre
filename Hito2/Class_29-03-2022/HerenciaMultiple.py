class Clase_A:
    
    def __init__(self):
        print('Soy la clase A')

    def metodo_clase_a(self):
        print('Soy un metodo de la  clase A')

class Clase_B:
    
    def __init__(self):
        print('Soy la clase B')

    def metodo_clase_a(self):
        print('Soy un metodo de la  clase B')

class Derivada(Clase_B, Clase_A):
    pass

der1 = Derivada()
der1.metodo_clase_a()
der1.metodo_clase_a()
