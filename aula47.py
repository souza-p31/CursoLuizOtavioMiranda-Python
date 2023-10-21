palavra = 'MACACO'
letras_acertadas = ''
tentativas = 0

print('*** Jogo de adivinhação ***\n')
while True:
    chute = str(input('Digite uma letra: ')).upper()[0]
    tentativas += 1
    qtd_letras_ocultas = 0

    if chute in palavra:
        letras_acertadas += chute
    
    print('Palavra formatada: ',end='')
    for p in palavra:
        if p in letras_acertadas:
            print(p,end='')
        else:
            print('*',end='')
            qtd_letras_ocultas += 1
    print()
    if qtd_letras_ocultas == 0:
        print(f'Você ganhou com {tentativas} tentativas!')
        break



