"""
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu interador
"""

"""
O laço de repetição for funciona da seguinte forma,
chamando o método __iter__ ele identifica a id do iterável e
utilizando o método next conseguimos avançar através dele até chegar ao
fim, que se tentar avançar mais vai resultar em um erro. O laço for é semelhante
a estrutura while abaixo
"""

texto = 'Luiz'


# for letra in texto:
#     texto = 'Luiz' # iterável

iteratador = iter(texto) # iterator
# print(next(iteratador))
# print(next(iteratador))
# print(next(iteratador))
# print(next(iteratador))

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# for letra in texto:
#     print(letra)