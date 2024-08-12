
#1. Cálculo manual de los cuartiles
#Los cuartiles dividen una lista ordenada en cuatro partes iguales. El primer cuartil (Q1) es el valor en el 25% de la lista, el segundo cuartil (Q2) es la mediana, y el tercer cuartil (Q3) es el valor en el 75%.

#python
#Copiar código
def calcular_cuartiles(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    Q2 = calcular_mediana(lista_ordenada)
    if n % 2 == 0:
        mitad = n // 2
        Q1 = calcular_mediana(lista_ordenada[:mitad])
        Q3 = calcular_mediana(lista_ordenada[mitad:])
    else:
        mitad = n // 2
        Q1 = calcular_mediana(lista_ordenada[:mitad])
        Q3 = calcular_mediana(lista_ordenada[mitad+1:])

    return Q1, Q2, Q3

def calcular_mediana(lista):
    n = len(lista)
    mitad = n // 2

    if n % 2 == 0:
        return (lista[mitad - 1] + lista[mitad]) / 2
    else:
        return lista[mitad]

# Ejemplo de uso
mi_lista = [7, 1, 3, 5, 9, 11, 15]
Q1, Q2, Q3 = calcular_cuartiles(mi_lista)
print(f"Q1: {Q1}, Q2 (Mediana): {Q2}, Q3: {Q3}")