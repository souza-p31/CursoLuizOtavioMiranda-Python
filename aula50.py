"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria','Helena','Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))


# lista = ['Maria','Helena','Luiz']

# for i,nome in enumerate(lista):
#     print(i,nome)