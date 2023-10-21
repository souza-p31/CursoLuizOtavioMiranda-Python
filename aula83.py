# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), b = pessoa.items() # desempacotamento dentro dos ()
# print(a1, a2, b)

# (a1, a2), (b1, b2) = pessoa.items() # semelhante ao que acontece dentro de um for
# print(a1, a2, b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa} # Podemos extrair toda tudo (chave e valor) usando **
# print(pessoa_completa)

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa) # Extração de 2 dicionarios e junção em um novo

pessoa_completa = {**pessoa, **dados_pessoa, 'chave': 1}
# print(pessoa_completa) # E ainda da pra adicionar ou editar os dados

# args e kwargs
# args (já vimos, servem para argumentos não nomeados)
# kwargs - keyword arguments (argumentos nomeados, servem para usar, como o nome já diz, com argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# é preciso ficar atento nesse momento, porque a função
# faz a separação do que é argumento nomeado e não nomeado, como podemos ver

# mostro_argumentos_nomeados(1, 2, 3, **pessoa_completa)
# normalmente funções que recebem qualquer valor tem essa extrutura

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}

mostro_argumentos_nomeados(**configuracoes)