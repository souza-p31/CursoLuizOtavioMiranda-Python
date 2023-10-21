#count é um iterador sem fim (itertools)

from itertools import count

"""
Count é uma função do modulo itertools, não vem com o Python. O count tem algumas semelhanças com o range, podemos informar onde começa, os passos, mas por aí acabam as semelhanças, porque o count é um iterator assim como o range, mas é iteravel, e o range não é. O count é infinito, o range não. Podemos fazer a prova real chamando o método hasattr para chegar se tem o método __iter__ e __next__ dentro deles.
"""

c1 = count(8, 8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for c in c1: # Aqui fizemos um loop infinito, já que o count conta infinitamente. Para evitar processamento desnecessario vou colocar uma condição para parar o laço
    if c >= 100:
        break
    print(c)

print('range')
for d in r1: # No range não preciso colocar um break, porque ele termina quando chega no intervalo.
    print(d)
