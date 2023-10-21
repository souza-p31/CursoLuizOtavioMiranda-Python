"""
Módulos padrão do Python (import, from, as e *)
inteiro - import nome_modulo
Vantagens: você tem o namespace (nome) do módulo 
Desvantagens: nomes grandes
"""
import sys

platform = 'a minha'
print(sys.platform) # Aqui o nome do método está protegido pelo namespace do modulo, e por isso posso ter uma variável com o mesmo nome do método. Caso eu usasse apenas o metodo, sem esse namespace, dependendo da ordem do código, ou a variável ou o método seria sobrescrito.
print(platform) 

"""
Partes - from nome_modulo import objeto1, objeto 2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do módulo
"""
from sys import exit, platform

print(platform)
platform = 'a minha' # sobrescrevi o método do modulo, caso isso aconteceça por acidente pode acabar quebrando um código
print(platform) 

# Alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform) # dei o apelido de s para o modulo sys, assim posso chamar pelo apelido que escolhi. Existem modulos que a comunidade já adotou certos apelidos e é interessante usar também para melhor entendimento de outros que possam olhar o código. Da mesma forma, é bom tomar cuidado com os apelidos, porque se não, por falta de costume, pode acabar confundindo.
print(sys)

# Alias 2 - from nome_modulo import objeto as apelido

from sys import exit as ex
from sys import platform as pf # dei um alias apenas ao método.

print(pf) 

"""
Vantagens: você pode reservar nomes para seu código
Desvantagens: pode ficar fora do padrão da linguagem

Má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo
"""

from sys import * # com o * eu importei tudo, fica ruim de ler, por exemplo, de onde veio esse platform que eu executei? Não está explicito.

print(platform) 