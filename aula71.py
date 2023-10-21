"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total

soma123 = soma(1, 2, 3)
print(soma123)

soma456 = soma(4, 5, 6)
print(soma456)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
outrasoma = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
outrasoma = soma(*numeros)
print(outrasoma)

print(sum(numeros))
print(*numeros)