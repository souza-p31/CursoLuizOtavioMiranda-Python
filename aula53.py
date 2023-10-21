"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria','Helena','Luiz']
lista.append('João')

lista_enumerada = enumerate(lista) # enumera os itens e retorna o id, tanto que podemos usar o método next nele para trazer os valores
print(lista_enumerada)
print(next(lista_enumerada)) # fazer dessa forma tem um problema, quando acabarem os itens do iterador não sera mais possivel usar esse enumerate, aí teriamos que criar um novo, por isso geralmente ele é utilizado direto no laço

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# é igual a 

for indice, nome in enumerate(lista):
    print(indice, nome)