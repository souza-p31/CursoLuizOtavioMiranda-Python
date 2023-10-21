"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta os espaços do
inicio e fim, mas existem variações
que cortam apenas da esquerda ou direita,
eles são lstrip e rstrip 
"""

frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
