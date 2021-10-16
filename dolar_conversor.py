opciones = """
¡Te doy la bienvenida! ¿De qué país sos?
  1. Argentina
  2. Brasil
  3. Chile
  4. Colombia
"""

opcion_elegida = input(opciones)

try:
    opcion_elegida = int(opcion_elegida)

    if opcion_elegida == 1:
        print("¡Hola Argentina!")
        cotizacion_dolar = 185
    elif opcion_elegida == 2:
        print("¡Hola Brasil!")
        cotizacion_dolar = 99
    elif opcion_elegida == 3:
        print("¡Hola Chile!")
        cotizacion_dolar = 100
    elif opcion_elegida == 4:
        print("¡Hola Colombia!")
        cotizacion_dolar = 25 
    else:
        print("No conozco ese pais pa, ahre que pusiste cualquier cosa")
        exit()
    
    pesos = int(input("¿Cuántos pesos tienes? "))

    pesos_convertidos  = round(pesos / cotizacion_dolar, 2)

    print('Tenes US$%s' % pesos_convertidos)

except ValueError:
    print("Por favor, ingrese un número entero.")
    retry = input("¿Desea intentarlo de nuevo? (s/n) ")
    if retry == "s":
      print('Te la debo mi rey')
    elif retry == "n":
      exit() # Como hacer retry?
    else:
      print('No te entendi, pero paja preguntar de nuevo. ¡Bai!')
      exit()