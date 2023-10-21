""" while/else """

string = 'Valorqualquer'

i = 0 
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Else do while')
print('Fora do while')