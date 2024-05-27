datos = []
num = int(input("Cuantos Valores va a ingresar: "))

for i in range(num):
    valor = float(input("Ingrese un numero: "))
    datos.append(valor)
    
    
#a = [1,2,2,5,5,5,6,7,8]
n = len(datos)
con = 0
mayor = 0
for i in range(n):
    con = 0
    for j in range(n):
        if(datos[i] == datos[j]):
            con = con + 1
    #print("a[",i,"]= ", a[i],"se repite",con, "veces")
    if(con>mayor):
        mayor = con
        moda = datos[i]
print("La moda es ",moda," y se repite",mayor," veces")        
            