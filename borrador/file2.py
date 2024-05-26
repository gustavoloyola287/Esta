
def ingresar_datos():
    datos = []
    print("Ingrese los valores de los datos (escriba 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == 'fin':
            break
        try:
            dato = float(entrada)
            datos.append(dato)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return datos
    