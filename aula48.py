"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, adiciona um item ao final
    insert, adiciona um item no índice escolhido
    pop, remove do final ou do índice escolhido
    del, apaga um índice
    clear, limpa lista
    extend, estende a lista
    +, concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        -54321 
#         01234
# string = 'ABCDE' # 5 caracteres (len)
# lista = [] # falsy
# print(lista, type(lista))

#        0    1      2             3   4
# lista = [123, True, 'Luiz Otávio', 1.2,[]]
# print(lista)
# lista[2] = 'Maria'
# print(lista)

# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# print(lista)
# ultimo_valor = lista.pop()
# print(lista, 'removido', ultimo_valor)

"""
Cuidados com dados mutáveis
= copia do valor (imutáveis)
= aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz',"Maria",1,True,1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
