sequencia = int(input('Quantos números você quer mostrar?: '))

def fib(n):
    a = 0
    b = 1
    contador = 0
    if n >= 2:
        print(a, b, end=' ')
        while contador < n - 2:
            c = a + b
            a = b
            b = c
            contador += 1
            print(c,end=' ')
    else:
        print(a)

fib(sequencia)



