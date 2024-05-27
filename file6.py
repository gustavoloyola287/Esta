
lista = [2,2,2,4,5,6,8]


def moda(lista):
    modalista = []
    con = 0
    for elemento in lista:
        if lista.count(elemento) > con:
            modalista = []
            modalista.append(elemento)
            con = lista.count(elemento)
        elif lista.count(elemento) == con:
            if not elemento in modalista:
                modalista.append(elemento)
                con = lista.count(elemento)
    if con * len(modalista) == len(lista):
        modalista = [-1] 
    return modalista

print(moda) 

                  
        
        

    