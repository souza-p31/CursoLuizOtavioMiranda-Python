# Reduce - faz a redução de um iterável em um valor

"""
Basicamente o método reduce faz o que um acumulador faz. Ele recebe uma função, um iterável e um ponto de partida. Até é possível usar sem colocar o ponto de partida, mas não é indicado porque pode gerar erros. Exemplo, se não for informado o ponto partida, que no caso é o acumulador, o primeiro item do iterável vai ser o acumulador e o segundo item vai ser o produto, bem mais confuso. Reduce é um método do modulo functools.
"""
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# Acumulador convencional (basicamente o reduce faz isso)
total = 0
for p in produtos:
    total += p['preco']
print(total)

total2 = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0 # aqui é um bom exemplo, caso não seja colocado esse acumulador o código vai quebrar, porque o primeiro item vai entrar como int e o resto vai entrar como dict e não tem como somar esses tipos diferentes. 
)

print(total2) 


# aqui podemos ver melhor o que acontece dentro do reduce. Ele vai acumulando no acumulador e sempre retorna o produto que está sendo acumulado.
def funcao_reduce(acumulador, produto):
    print(f'{acumulador=}')
    print(f'{produto=}')
    return acumulador + produto['preco']

total3 = reduce(
    funcao_reduce,
    produtos,
    0
)