class Person:
    __fulllname = None
    __lastname = None
    __document = None
    __type = None
    __age = None
    
    def __init__(self, name, lastname, document, type):
        self.__fullname = name
        self.__lastname = lastname
        self.__document = document
        self.__type = type
    # Getters & Setters
    def get_fullname(self):
        return self.__fullname
    def set_fullname(self, texto):
        self.__fullname = texto
    def get_lastname(self):
        return self.__lastname
    def set_lastname(self, texto):
        self.__lastname = texto
    def get_document(self):
        return self.__document
    def set_document(self, document):
        self.__document = document
    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type
    
    def __str__(self):
        return f'Name: {self.__fullname}\nLastname: {self.__lastname} \nDocument: {self.__document} \nType: {self.__type}'


class Client(Person):
    __category = None
    __code = None
    
    def __init__(self, name, lastname, document, type, category, code):
        super().__init__(name, lastname, document, type)
        self.__category = category
        self.__code = type
        
    def __str__(self):
        return super().__str__() + "\nCategory: " + self.__category + "\nCode: " + self.__code
    
class Employee(Person):
    __typeContrato = None
    __salary = None
    
    def __init__(self, name, lastname, document, type, typeContra, salary):
        super().__init__(name, lastname, document, type)
        self.__typeContrato = typeContra
        self.__salary = salary
        
    def get_type_contrato(self):
        return self.__typeContrato
    def set_type_contrato(self, typeC):
        self.__typeContrato = typeC
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary  
    
    def __str__(self):
        return super().__str__() + "\nType Contra: " + self.__typeContrato + "\nSalary: " + str(self.__salary)
    
    def calcular_sueldo(self):
        return self.get_salary()
        
ObjetoPersona = Person("Daniel", "Laura", "10021571", "LP")
print(ObjetoPersona)
print()
ObjetoCliente = Client("Adriana", "Cusicanqui", "10021573", "TJ", "Premium", "AC-10021571TJ")
print(ObjetoCliente)
print()
ObjetoEmployee = Employee("Luis", "Carpio", "65468766", "OR", "Anual", 2000)
print(ObjetoEmployee)