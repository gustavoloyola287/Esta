datos = []
num = int(input("Cuantos Valores va a ingresar: "))

for i in range(num):
    valor = float(input("Ingrese un numero: "))
    datos.append(valor)
    

print(datos)   
datos.sort()

print(datos)

#MEDIA

media = sum(datos) / len(datos)

print("La media es: ", media)

n = len(datos)
print("Cantidad de datos ingresados: ",n)

#MEDIANA

if n % 2 == 0:
    mediana = (datos[n//2 - 1] + datos[n//2])/ 2
else:
    mediana = datos[n//2]
    

print("La mediana es: ",mediana)

# MODA

m = len(datos)
con = 0
mayor = 0
for h in range(m):
    con = 0
    for j in range(m):
        if(datos[h] == datos[j]):
            con = con + 1
    
    if(con>mayor):
        mayor = con
        moda = datos[h]
print("La moda es ",moda," y se repite",mayor," veces")        
            