pesos = input('Cuantos pesos argentinos tenes? = ')
pesos = float(pesos)

dolar_hoy = 182.00

dolar_convertido = round(pesos / dolar_hoy, 2)

# TODO: Cual es mejor?
print('Tenes US$%s' % (dolar_convertido))