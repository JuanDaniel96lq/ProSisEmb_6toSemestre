# from [Nombre de Archivo] import [Nombre de Clase]
from student import Student

student1 = Student()
cadena = input("Introduzca su apellido: ")
student1.set_last_name(cadena)
cadena = input("Introduzca su nombre: ")
student1.set_full_name(cadena)

student1.print_student();