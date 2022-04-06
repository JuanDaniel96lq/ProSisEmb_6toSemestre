class Car:
    nombre = None
    color = None
    modelo = None
    tamaño = None
    forma = None
    
    def __init__(self, n, c, m, t, f):
        self.nombre = n
        self.color = c
        self.modelo = m
        self.tamaño = t
        self.forma = f
        
    def __str__(self):
        return f'Datos de Vehiculo\nNombre: {self.nombre}\nColor: {self.color}\nModelo: {self.modelo}\nTamaño: {self.tamaño}\nForma: {self.forma}'
    
    
    def mover(self):
        print('Moviendo')
    
    def frenar(self):
        print('Frenando')
        
    def girar_derecha(self):
        print('Girando a la derecha')
    
    def girar_izquierda(self):
        print('Girando a la izquierda')
        
Objeto = Car("F150 Raptor", "Negro", "2020", "3m x 6m", "Camioneta")
print("=======================")
print(Objeto)
print("=======================")
Objeto.mover()
Objeto.frenar()
Objeto.girar_derecha()
Objeto.girar_izquierda()