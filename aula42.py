frase = 'O Python e uma linguagem de programacao'\
' multiparadigma.'\
'Python foi criado por Guido van Rossum.'

frase = frase.lower()
i = 0 
letra_mais = None
qtd_letra_mais = 0

while i < len(frase):
    letra_atual = frase[i]
    aparece = frase.count(letra_atual)

    if letra_atual != ' ' and letra_atual != '.':
        if aparece > qtd_letra_mais:
            letra_mais = letra_atual
            qtd_letra_mais = aparece
    
    i += 1

print(f'{letra_mais=},{qtd_letra_mais=}')
