"""
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador','Ubatuba','Belo Horizonte']
['BA','SP','MG','RJ']
Resultado
[('Salvador','BA'), ('Ubatuba','SP'), ('Belo Horizonte', 'MG')]
"""

#metodo 1
lista_1 = ['Salvador','Ubatuba','Belo Horizonte']
lista_2 = ['BA','SP','MG','RJ']
resultado = []
tam_l1 = len(lista_1)
tam_l2 = len(lista_2)
op = tam_l1
if tam_l1 > tam_l2:
    op = tam_l2

for c in range(op):
    resultado.append((lista_1[c], lista_2[c]))

print(resultado)

#metodo 2
def unir_listas(lista_1, lista_2):
    tam_max = min(len(lista_1), len(lista_2))
    resultado = [
        (lista_1[c], lista_2[c]) for c in range(tam_max)
    ]
    return resultado

a = unir_listas(lista_1, lista_2)
print(a)

#metodo 3

print(list(zip(lista_1, lista_2))) # o python já fornece esse tipo de funcionalidade. Nesse caso ele itera sobre a lista menor, mas podemos fazer o oposto

from itertools import zip_longest
#nesse caso aqui, a biblioteca itertools com a função zip_longest pega a maior lista e itera ela adicionando os itens da segunda lista, e quando os itens da segunda lista acabarem ele adiciona uma string que a gente define
print(list(zip_longest(lista_1, lista_2, fillvalue='Sem cidade'))) 




