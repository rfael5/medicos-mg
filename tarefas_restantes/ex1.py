def soma(x, y):
    return x + y

print(soma(2, 2))

def potencia(x, y):
    return x ** y

print(potencia(2, 3))

def fatorial(x):
    a = x - 1
    while a > 1:
        x = x * a
        a -= 1
    return x

print(fatorial(4))

def fantasma (x, y):
    return soma(potencia(x, y), -x) - (y * -1)

print(fantasma(5, 2))

