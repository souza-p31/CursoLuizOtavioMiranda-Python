# Filter é um filtro funcional

"""
Lembrando da list comprehension, do lado esquerdo do laço fica o mapeamento, e para mapeamento aprendemos o map. Do lado direito fica os filtros, e é claro que existe um método para replicar o filtro. Para isso podemos usra o método filter. Ele vai receber uma função que vai retornar as condições e vai receber também o iteravel, e pronto.
"""
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = filter(lambda produto: produto['preco'] > 10, produtos)

print(novos_produtos) # o filter retorna um filter object, então é o mesmo esquema dos anteriores, desempacotar, jogar em uma lista e por aí vai.

print(*novos_produtos) # Realmente filtrou e só retornou os valores maiores que 10