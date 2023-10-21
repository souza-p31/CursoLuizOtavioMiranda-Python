"""
Modularização - entendendo os seus próprios módulos Python
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro o parte do módulo
O Python conhece a pasta onde o __main__ está e as pastas abaixo dele
Ele não reconhece pastas e módulos acima do __main__ por padrão
O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
"""

# import sys # é interessante separar as importações dos modulos python dos nossos modulos.
# sys.path.append(r'C:\Users\ph324\Desktop') # Adicionei o novo caminho onde está o modulo que eu quero ao sys.path (tive que colocar o r antes das aspas para indicar que é uma raw string e que não tem variavel dentro, para o python ler como está escrito.)
# import teste_modulo # importei o modulo do caminho novo 

# importei a aula97_m.py dessa forma porque está no mesmo caminho do __main__ de aula97.py, se fosse outro caso seria necessário adicionar o caminho.
# import aula97_m # está executando o código de lá que diz o __name__ do módulo e o de cá.

# sempre o primeiro módulo que o python executa é o __main__ 
# através de __name__ podemos ver o nome do módulo
# print('Este módulo se chama', __name__)

# Python reconhece módulos abaixo do __main__, acima não. 
# Ou seja, se quisermos adicionar um módulo que vem depois, como é o caso de aula97_m.py vamos conseguir, mas se tentassemos adicionar um módulo em uma PASTA anterior a desse modulo daria erro.

# print(*sys.path, sep="\n") # O python também reconhece os pacotes no caminho de sys.path. Aqui podemos ver os caminhos. Podemos incluir novos caminhos usando o append por se tratar de uma lista.

"""
Não é muito comum fazer esse tipo de manipulação de pacotes, o mais usual é ter o modulo __main__ e criar 
em torno dele, adicionar os outros modulos na pasta dele e etc."""

#--------------------------------------------------

import aula97_m
from aula97_m import soma, variavel

# Assim como os modulos irmãos do Python podemos importar total ou parcialmente nossos modulos

print(aula97_m.variavel)
print(variavel)

print(soma(2, 3))
print(aula97_m.soma(2, 3))