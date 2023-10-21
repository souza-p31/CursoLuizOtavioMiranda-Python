"""
Tipo tupla - uma lista imutável
"""

nomes = 'Maria','Helena', 'Luiz' # Se os elementos não forem colocados dentro de colchetes o python já entende que é uma tupla
nomes = ('Maria','Helena', 'Luiz') # Outra forma é colocar entre parenteses para deixar em evidencia

nomes = list(nomes)
print(nomes)
nomes = tuple(nomes) # é possível fazer a coersão de tuplas para listas e vice-versa
print(nomes)
# nomes[1] = 'Outro' # vai retornar um erro pois tuplas são imutáveis
print(nomes[-1])
print(nomes)
