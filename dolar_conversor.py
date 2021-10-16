pesos = input('Cuantos pesos argentinos tenes? = ')
pesos = float(pesos)

dolar_hoy = 182.00

dolar_convertido = pesos / dolar_hoy

# TODO: Cual es mejor?
print('Tenes US$%f' % (dolar_convertido))
print('Tenes US$' + str(dolar_convertido))