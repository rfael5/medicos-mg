palavra = input(str('Digite uma palavra: '))

def palindromo(lista):
    palavra_frente = []
    palavra_inverso = []

    for p in range(0, len(lista)):
        palavra_frente.append(lista[p])

    for l in range(len(lista)-1,0-1,-1):
        palavra_inverso.append(lista[l])

    if palavra_frente == palavra_inverso:
        print(f'{lista} é um palindromo')
    else:
        print(f'{lista} não é um palindromo')

palindromo(palavra)