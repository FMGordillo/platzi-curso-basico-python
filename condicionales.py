edad = input('Ingrese su edad, pa: ')

try:
    edad = int(edad)
    if edad > 17:
        print('Usted es mayor de edad')
    elif edad == 17:
        print('Usted tiene 17 años, justito')
    else:
        print('Usted es menor de edad')
except ValueError:
    print('La edad debe ser un número entero')