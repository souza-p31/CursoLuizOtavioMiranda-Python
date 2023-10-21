#Problemas dos parâmetros mutáveis em funções Python

# def adicionar_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# cliente1 = adicionar_clientes('luiz')
# cliente1 = adicionar_clientes('joana', cliente1)
# print(cliente1)

# #Se colocamos parametros mutáveis nos argumentos de uma função no python pode acontecer esse vinculo que estamos vendo. Para corrigir isso o correto é fazer o seguinte.
# cliente2 = adicionar_clientes('helena')
# print(cliente2)

def adicionar_cliente(nome, lista=None):
    # checar se a lista foi informada ou não, e se não foi criar uma
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionar_cliente('luiz')
adicionar_cliente('joana', cliente1)
adicionar_cliente('fernando', cliente1)
print(cliente1)

cliente2 = adicionar_cliente('Helena')
adicionar_cliente('Moreira', cliente2)
adicionar_cliente('Maria', cliente2)
print(cliente2)

#construindo dessa forma não acontece o vinculo, porque a criação da lista é executada toda vez que a função é chamada.
