class SeriesStrings:
    pass

    def __init__(self):
        pass
    
    def fibonacci(self, limit):
        a = 1
        b = 0
        c = 0
        r = ''
        
        for i in range(0, limit, 1):
            if(i == 0):
                r = r + str(c)
            else:
                r = r + "," + str(c)
            c = a + b
            a = b
            b = c
        
        print(r)
            
    
    def factorial(self, limit):
        c = 1
        r = ''
        for i in range(1, limit + 1, 1):
            c = c * i
            if(i == 0):
                r = r + str(c)
            else:
                r = r + " * " + str(i)
        
        print(str(limit)+'! = ' + r + ' = ' + str(c))
    
    
    def verify(self, letra):
        if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U"):
            print('VOCAL')
        else:
            print('CONSONANTE')


SaS = SeriesStrings()

N = int(input("Ingrese el valor de N: "))
print()
SaS.fibonacci(N)
print()
SaS.factorial(N)
print()
N = input("Ingrese una letra: ")
print()
SaS.verify(N)
print()