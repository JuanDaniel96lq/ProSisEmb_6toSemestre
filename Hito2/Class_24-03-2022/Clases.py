class Person:
    __name = None
    __lastname = None
    __age = None
    
    def __init__(self, name, lastname, integer):
        self.__name = name
        self.__lastname = lastname
        self.__age = integer
    
    def get_name(self):
        return self.__name
        
    def set_name(self, texto):
        self.__name = texto
        
    def get_lastname(self):
        return self.__lastname
        
    def set_lastname(self, texto):
        self.__lastname = texto
        
    def get_age(self):
        return self.__age
        
    def set_age(self, integer):
        self.__age = integer
    
    def __str__(self):
        return "Datos: " + self.__name + " " + self.__lastname + " " + str(self.__age)
    
    def update_person(self, name, lastname, age):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        
Persona = Person("XXXXXXXX", "XXXXXXXX", 99)
print(Persona)

n = input('Ingrese su nombre: ')
l = input('Ingrese su apellido: ')
a = input('Ingrese su edad: ')

Persona.update_person(n, l, a)

print(Persona)
