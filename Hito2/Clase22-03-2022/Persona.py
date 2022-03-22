class Persona:
    __name = None
    __lastname = None
    __age = None
    
    def __init__ (self, name, lastname, age):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        
    def __str__ (self):
        return f'Nombre Completo {self.__name} {self.__lastname} tengo {self.__age} años.'
    
    def __metodo_privado(self):
        return self.__age()-2021
        
instancia = Persona("Juan Daniel", "Laura Quispe", 20)

#print(instancia.__metodo_privado())

print(instancia.__age)