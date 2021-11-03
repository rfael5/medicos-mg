lista = [5,2,9,20,1,3]

def ordena(l):
    ordenada = sorted(l)
    return ordenada

lista_ordenada = ordena(lista)

print(lista_ordenada)

def encontra(n, l):
    if n in l:
        print(f'{n} está na lista na posição {l.index(n)}.')
    else:
        print(-1)



encontra(5, lista_ordenada)