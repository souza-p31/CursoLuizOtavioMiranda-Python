"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Luiz Otavio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.zfill(10))

# Não é possível mudar os tipos, são imutáveis, mas é permitido fazer copias e modificar essas copias
