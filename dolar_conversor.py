opciones = """
¡Te doy la bienvenida! ¿De qué país sos?
  1. Argentina
  2. Brasil
  3. Chile
  4. Colombia
"""

paises = ["Argentina", "Brasil", "Chile", "Colombia"]
cotizacion_dolar = [185, 99, 100, 25]
opcion_elegida = input(opciones)


# 1. Saluda al pais
# 2. Convierte a dolares
# 3. Imprime el resultado
def calcular_e_imprimir(pais_index, cantidad_pesos):
  print('Hola %s' % (paises[pais_index - 1]))
  pesos_convertidos = round((pesos / cotizacion_dolar[pais_index - 1]), 2)
  print('Tenes US$%s' % pesos_convertidos)

try:
    opcion_elegida = int(opcion_elegida)
    if opcion_elegida > len(paises):
      print("No conozco ese pais pa, ahre que pusiste cualquier cosa")
      exit()
    pesos = int(input("¿Cuántos pesos tienes? "))
    calcular_e_imprimir(opcion_elegida, pesos)
    
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