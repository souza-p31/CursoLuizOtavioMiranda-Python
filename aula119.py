"""
Exercicio - lista de tarefas com desfazer e refazer

todo = [] -> lista de tarefas
todo = ['fazer café'] -> adicionar fazer café
todo = ['fazer café', 'caminhar'] -> adicionar caminhar
desfazer = ['fazer'café'] -> refazer ['caminhar']
desfazer = [] -> refazer ['caminhar','fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""

# tarefas = []
# desfazer = []
# comando = None

# while True:
#     print('Comandos: listar, desfazer, refazer')
#     comando = str(input('Digite uma tarefa ou comando: ')).strip().lower()
#     if comando not in ('listar', 'desfazer', 'refazer'):
#         tarefas.append(comando.capitalize())
#         print('\nTAREFAS:')
#         a = [print(tarefa) for tarefa in tarefas]
#         print()

#     elif comando == 'listar':
#         if len(tarefas) < 1:
#             print('Não há tarefas')
#         print('\nTAREFAS:')
#         a = [print(tarefa) for tarefa in tarefas]
#         print()
        
#     elif comando == 'desfazer':
#         if len(tarefas) < 1:
#             print('\nNão há o que desfazer\n')
#         else:
#             desfazer.append(tarefas[-1])
#             tarefas.pop()
#             print('\nTAREFAS:')
#             a = [print(tarefa) for tarefa in tarefas]
#             print()
    
#     elif comando == 'refazer':
#         if len(desfazer) < 1:
#             print('\nNão há o que refazer\n')
#         else:
#             tarefas.append(desfazer[0])
#             desfazer.pop(0)
#             print('\nTAREFAS:')
#             a = [print(tarefa) for tarefa in tarefas]
#             print()

#     else:
#         break

"""
Não é interessante abusar de condicionais no código. Claro, são muito importantes, mas se pudermos evitar de afastar da margem é bom, porque quanto mais afastado mais complexo é o código, e isso vai contra as regras de simplicidade do python. Poderiamos refazer o código da seguinte forma:
"""

import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
    with open('lista_tarefas.json', 'w') as lista_tarefas:
        json.dump(tarefas, lista_tarefas, indent=2)


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

