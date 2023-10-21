"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio' #Iteráveis
#    -1110987654321
tam_nome = len(nome)
print(nome)
print(tam_nome)
print(nome[3])

pos = 0
while pos < tam_nome:
    print(f'*{nome[pos]}',end='')
    pos += 1