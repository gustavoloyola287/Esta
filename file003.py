
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2

    if n % 2 == 0:
        # Si la longitud es par, la mediana es el promedio de los dos valores centrales
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        # Si la longitud es impar, la mediana es el valor central
        return lista_ordenada[mitad]
   