# Generator expression, Iterables e Iterators em Python

"""
O iterador não sabe nada sobre o item, não sabe tamanho,
nem ordem, ele só retorna o próximo item até levar o StopIteration
que significa que o iteravel chegou ao fim.
"""

import sys

iteravel = ['Eu', 'Tenho', '__iter__']
iterador = iter(iteravel) # tem __iter__ e __next__
# print(next(iterador))
# print(next(iterador))
# print(next(iterador)) # Até aqui tem next, após não tem mais nada e o StopIteration aparece
# print(next(iterador))

"""
Iterator e generator tem suas semelhanças, mas
são coisas diferentes.
O generator tem um iterador, mas o iterator não é generator.
Iterator só sabe mostrar o próximo item até que o iterável acabe,
já o generator é uma função de pausa.

Vantagens do generator são, ele só chama um item por vez, então economiza
muito espaço na memoria durante as execuções. Ele sabe de onde até onde tem que ir
mas ainda não foi, só avança para o proximo quando for requisitado.

Desvantagens, ele não sabe o tamanho dele e não é iteravel, então não da pra navegar
pelo indice.

Abaixo podemos ver quanto de espaço ocupa.

"""

lista = [n for n in range(10000)]
generator = (n for n in range(10000)) # não existe tuple comprehension, essa estrutura é o generator

# print(lista) 
# print(generator) # retorna o ID na memoria, usando o modulo sys com metodo getsizeof
#podemos ver o tamanho que ocupa na memoria

print(sys.getsizeof(lista)) 
print(sys.getsizeof(generator)) # generator sempre ocupa o mesmo espaço

print(next(generator)) # chamando os itens do generator
