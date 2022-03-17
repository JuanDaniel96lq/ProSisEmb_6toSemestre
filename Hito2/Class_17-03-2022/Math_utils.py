class Math_utils:
    name_app = ""
    version = ""
    year = ""
    
    def __init__(self, name, v, y):
        self.name_app = name
        self.version = v
        self.year = y
    
    def get_name_app(self):
        return self.name_app
    
    def get_version(self):
        return self.version
    
    def get_year(self):
        return self.year
    
    def set_name_app(self, text):
        self.name_app = text
    
    def set_version(self, num):
        self.version = num
        
    def set_year(self, num):
        self.year = num
        
    def print_app(self):
        print(self.name_app, "-", self.version, "-", self.year)
        
    def generate_serie(self, inicio, hasta, increment):
        result = ""
        for i in range(inicio, hasta + 1, increment):
            if i == (hasta):
                result = result + str(i) + "."
            else:
                result = result + str(i) + ", "
        return result
    
    def extention_from_ci(self, ci):
        print(ci[-2:])
