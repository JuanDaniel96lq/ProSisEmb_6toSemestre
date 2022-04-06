class Writer:
    __name = None
    __email = None
    __gender = None
    __nationality = None
    # Constructor
    def __init__(self, name, email, gender, nationality):
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__nationality = nationality
    # Getters
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_gender(self):
        return self.__gender
    def get_nationality(self):
        return self.__nationality
    # Setters
    def set_name(self, name):
        self.__name = name
    def set_email(self, email):
        self.__email = email
    def set_gender(self, gender):
        self.__gender = gender
    def set_nationality(self, nationality):
        self.__nationality = nationality
    # Métodos
    def write_book(self):
        return self.__name + " está escribiendo un libro."
    def write_a_movie(self):
        return self.__name + " está escribiendo una pelicula."
    def change_nationality(self, nacionalidad):
        self.set_nationality(nacionalidad)
    def change_email(self, correo):
        self.set_email(correo)
        

Instance = Writer("Daniel", "eate.juandaniel.laura.qu@unifranz.edu.bo", "Masculino", "Boliviana")

print("=========================")
print("Nombre: " + Instance.get_name())
print("Correo: " + Instance.get_email())
print("Genero: " + Instance.get_gender())
print("Nacionalidad: " + Instance.get_nationality())

Instance.change_nationality("Peruana")
Instance.change_email("Jdaniel@gmail.com")
print("=========================")
print("Nombre: " + Instance.get_name())
print("Correo: " + Instance.get_email())
print("Genero: " + Instance.get_gender())
print("Nacionalidad: " + Instance.get_nationality())