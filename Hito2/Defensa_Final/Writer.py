class Writer:
    __name = None
    __email = None
    __gender = None
    __nationality = None
    
    def __init__(self, name, email, gender, nationality):
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__nationality = nationality
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
        
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender
        
    def get_nationality(self):
        return self.__nationality
    
    def set_nationality(self, nationality):
        self.__nationality = nationality
        
    def write_book(self):
        return self.__name + " está escribiendo un libro."
    
    def write_a_movie(self):
        return self.__name + " está escribiendo una película."
    
    def change_nationality(self, new_nacionality):
        self.__nationality = new_nacionality
        
    def change_email(self, new_email):
        self.__email =new_email
        
Instance = Writer("Daniel", "eate.juandaniel.laura.qu@unifranz.edu.bo", "M", "Boliviana")
print("===============================")
print("Nombre: " + Instance.get_name())
print("Email: " + Instance.get_email())
print("Genero: " + Instance.get_gender())
print("Nacionalidad: " + Instance.get_nationality())

Instance.change_nationality("Peruana")
Instance.change_email("JDaniel96lq@gmail.com")
print("===============================")
print("Nombre: " + Instance.get_name())
print("Email: " + Instance.get_email())
print("Genero: " + Instance.get_gender())
print("Nacionalidad: " + Instance.get_nationality())
print("===============================")