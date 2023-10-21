"""
Normalmente se fossemos colocar valores
dentro de uma lista sem usar list comprehension
fariamos dessa forma
"""
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
# print(lista)

# Com list comprehension poderiamos simplesmente fazer assim

lista = [x for x in range(3)]
# print(lista)

# E caso precisassemos adicionar dois ou mais valores como no exemplo

lista = [(x, y) for x in range(3) for y in range(3)]
# print(lista) # mesmo resultado

# Também podemos usar em letras e fazer list comprehension dentro de list comprehension

lista = [[(x, letra) for letra in 'Luiz'] for x in range(3)]
print(lista)