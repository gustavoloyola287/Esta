datos = []
num = int(input("Cuantos Valores va a ingresar: "))

for i in range(num):
    valor = float(input("Ingrese un numero: "))
    datos.append(valor)
    

print(datos)   
datos.sort()

print(datos)

media = sum(datos) / len(datos)

print("La media es: ", media)
    