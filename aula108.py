
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# from itertools import zip_longest

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# tam_max = len(lista_a)
# contador = 0
# if len(lista_a) > len(lista_b):
#     tam_max = len(lista_b) 
# print(tam_max)
# lista_soma = []

# for l1, l2 in zip_longest(lista_a, lista_b, fillvalue=0):
#     if contador == tam_max:
#         break
#     lista_soma.append(l1+l2)
#     contador += 1

# print(lista_soma)

# lista_soma.clear()
# lista_soma = [(l1 + l2) for l1, l2 in zip_longest(lista_a, lista_b, break)]
# print(lista_soma)

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
tam_max = len(lista_a)
lista_soma = []
if len(lista_a) > len(lista_b):
    tam_max = len(lista_b)

for c in range(tam_max):
    lista_soma.append(lista_a[c] + lista_b[c])
print(lista_soma)

lista_soma.clear()
for c, _ in enumerate(lista_b):
    lista_soma.append(lista_a[c] + lista_b[c])
print(lista_soma)

lista_soma.clear()
lista_soma = [a + b for a, b in zip(lista_a, lista_b)]
print(lista_soma)