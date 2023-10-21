"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

usuario_nome = str(input('Digite seu nome: '))
usuario_idade = int(input('Digite a sua idade: '))

if usuario_nome and usuario_idade:
    print(f'Seu nome é {usuario_nome}')
    print(f'Seu nome invertido é {usuario_nome[::-1]}')
    if ' ' in usuario_nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    cont_espacos = usuario_nome.count(' ')
    print(f'Seu nome tem {len(usuario_nome)-cont_espacos} letras')
    print(f'A primeira letra do seu nome é {usuario_nome[0]}')
    print(f'A última letra do seu nome é {usuario_nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
