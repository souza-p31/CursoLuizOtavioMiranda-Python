"""
Exercício - sistema de perguntas e respostas  
"""

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


# # Acessar os dois primeiros itens do dicionario
# acertos = 0
# for c in range(len(perguntas)):    
#     print(f"{perguntas[c]['Pergunta']}\n")
#     print('Opções: ')

#     opcoes = perguntas[c]['Opções']
#     for e, opcao in enumerate(opcoes):
#         print(f'{e}) {opcao}')

#     # Input
#     resposta_correta = opcoes.index(perguntas[c]['Resposta'])
#     selecao = input('Escolha uma opção: ')
#     try:
#         selecao = int(selecao)
#     except ValueError:
#         print('Digite apenas números ❌')
#     except Exception:
#         print('Erro desconhecido')
#     # Se o input for igual ao valor do ultimo item do dicionario mensagem positiva
#     if selecao == resposta_correta:
#         print('Acertou ✅\n')
#         acertos += 1
#     else:
#         print('Errou ❌\n')
# print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')



# Resolução
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')