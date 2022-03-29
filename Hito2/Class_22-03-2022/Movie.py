''' Metodos especiales en python '''
class Movie:
    name = None
    duration = None
    release = None
    
    ''' def __init__ (self, name, duration, release):
        self.name = name
        self.duration = duration
        self.release = release
    '''
    def __init__ (self):
        self.name = ""
        self.duration = ""
        self.release = ""
    
    def __str__ (self):
        return f'El nombre de la pelicula es {self.name} y la duración es de {self.duration} fue lanzado el año {self.release}'
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Pelicula eliminada correctamente", self.name)
        
    def get_name(self):
        return self.name
    
    def get_duration(self):
        return self.duration
    
    def get_release(self):
        return self.releas
    
    def set_name(self, text):
        self.name = text
        
    def set_duration(self, text):
        self.duration = text
        
    def set_release(self, integer):
        self.release = integer
    
object1 = Movie()
object1.set_name("Fast And Furious")
object1.set_duration("02:30:52")
object1.set_release(2020)

print(object1)
print(object1.get_name())