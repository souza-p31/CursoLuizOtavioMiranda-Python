
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# print(produtos, '\n')
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**produto,'preco': f"{produto['preco'] * 1.10 :.2f}"}
    for produto in produtos
]


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
from copy import deepcopy

# produtos_ordenados_por_nome = deepcopy(novos_produtos)
# l1 = produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
# print(produtos_ordenados_por_nome)

def ordenar(item):
    return item['nome']

produtos_ordenados_por_nome = [
    {'nome': n['nome'], 'preco': n['preco']}
    for n in novos_produtos
]
produtos_ordenados_por_nome = sorted(produtos, key=ordenar, reverse=True)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])

print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')