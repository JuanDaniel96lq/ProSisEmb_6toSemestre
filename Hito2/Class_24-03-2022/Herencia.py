class Person:
    __fulllname = None
    __lastname = None
    __age = None
    
    def __init__(self, name, lastname, integer):
        self.__fullname = name
        self.__lastname = lastname
        self.__age = integer
    
    def get_fullname(self):
        return self.__fullname
        
    def set_fullname(self, texto):
        self.__fullname = texto
        
    def get_lastname(self):
        return self.__lastname
        
    def set_lastname(self, texto):
        self.__lastname = texto
        
    def get_age(self):
        return self.__age
        
    def set_age(self, integer):
        self.__age = integer
    
    def __str__(self):
        return "Datos: " + self.__fullname + " " + self.__lastname + "\nEdad: " + str(self.__age)
    
    def update_person(self, name, lastname, age):
        Persona.__init__(self, fullname, lastname, age)
        self.__fullname = fullname
        self.__lastname = lastname
        self.__age = age

class Student(Person):
    __course = None
    __email = None
    
    def __init__(self, name, lastname, integer, course, email):
        Person.__init__(self, name, lastname, integer)
        self.__course = course
        self.__email = email
        
    def get_course(self):
        return self.__course
        
    def set_course(self, texto):
        self.__course = texto
    
    def get_email(self):
        return self.__email
        
    def set_email(self, texto):
        self.__email = texto
    
    def __str__(self):
        return  Person.__str__(self) + " Curso: " + self.__course + " Correo: " + self.__email

class Admin(Person):
    __sueldo = None
    
    def __init__(self, name, lastname, integer, sueldo):
        Person.__init__(self, name, lastname, integer)
        self.__sueldo = sueldo
        
    def __str__(self):
        return  Person.__str__(self) + "\nSueldo: " + str(self.__sueldo)
    
    def update_age(self, edad):
        Person.set_age(self, edad)

Objeto = Admin("Daniel", "Laura", 99, 2000)
print(Objeto)
Objeto.update_age(30)
print(Objeto)
