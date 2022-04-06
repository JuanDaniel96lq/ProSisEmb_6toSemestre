N = int(input("Ingrese un número: "))
a = 1
b = 0
c = 0
r = ''
for i in range(1, N + 1, 1):
    r = r + "[" + str(c) + "]"
    c = a + b
    a = b
    b = c
    
print(r)