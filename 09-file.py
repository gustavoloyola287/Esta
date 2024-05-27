def moda(datos):
    modalista = []
    con = 0
    for elemento in datos:
        if datos.count(elemento) > con:
            modalista = []
            modalista.append(elemento)
            con = datos.count(elemento)
        elif datos.count(elemento) == con:
            if not elemento in modalista:
                modalista.append(elemento)
                con = datos.count(elemento)
    if con * len(modalista) == len(datos):
        modalista = [-1] 
    return modalista
print(moda)
                  
        
        

    