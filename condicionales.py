edad = input('Ingrese su edad, pa: ')

try:
    edad = int(edad)
    if edad > 17:
        print('Usted es mayor de edad')
    else:
        print('Usted es menor de edad')
except ValueError:
    print('La edad debe ser un número entero')