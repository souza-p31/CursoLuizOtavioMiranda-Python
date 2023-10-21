#Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor
    if isinstance(valor, float) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'categoria' 
}   

# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}
# print(dc)

#Set Comprehension
s1 = {i for i in range(3)}
print(s1)

s1 = {i for i in range(10) if i % 2 == 0}
print(s1)