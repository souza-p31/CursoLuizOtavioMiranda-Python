# from sys import path
# import aula99_package # package a principio não faz nada, o que interessa pra a gente está dentro dele
# from aula99_package.modulo import soma # aqui do pacote aula99_package e do modulo modulo importamos a função soma
# import aula99_package.modulo # aqui do package aula99_package importamos o modulo modulo inteiro, o ruim de fazer assim é que o namespace fica gigante
# from aula99_package import modulo # aqui do package aula99_package importamos o modulo modulo apenas, porem fazendo dessa forma o namespace fica menor
# from aula99_package.modulo import * # Jeito errado e ruim, que importa tudo e deixa o código confuso. O nome desse * é __all__, e sabendo disso podemos fazer coisas interessantes como manipular o que é esse __all__ (continuação lá no modulo modulo)

# print(soma(2, 3)) # package - modulo - função
# print(aula99_package.modulo.soma(2, 3)) # package - modulo
# print(modulo.soma(2, 3)) # package - modulo (jeito certo)
# # print(__name__)
# # print(*path, sep="\n")


# print(outra_variavel) # se lá no modulo na lista __all__ for retirado essa variavel, o que o Python entende como tudo será modificado e essa variavel vai parar de funcionar.

# ---------------------------------------------------
# aqui importei um modulo que estava dentro do package e nesse modulo tem uma função que esta em outro modulo que também está dentro do package. Pode parece meio confuso mas fica mais simples se analisarmos como pontos de vista. Aqui nosso main (ponto de vista) é do aula99 que vê os arquivos irmãos e os abaixo dele, e lá no package no modulo acontece a mesma coisa, ele vê o irmão, mas o aula99 não, porque ele não olha pra trás. Toda importação tem que ser feita do ponto de vista do __main__.


# from aula99_package.modulo import soma, fala_oi

# print(fala_oi())

# Para esse código funcionar, lá no modulo modulo eu teria que declarar o caminho de onde vem a função, que no caso vem de modulob. Então não posso fazer apenas import modulob, por mais que a ferramenta permita, porque lá no package o main é modulo, aqui no aula99 não vai funcionar, porque desse ponto de vista o main é outro.

"""
Se lá no modulo modulo for importado considerando o ponto de vista dele no modulo aula99 vai dar erro, porque ele não vai encontrar o modulob, atenção nisso. Pode ser que lá não funcione, porque do ponto de vista de lá não vai encontrar o arquivo, mas daqui vai funcionar e se mudar para a importação considerando o ponto de vista de lá, lá vai funcionar e aqui não.
"""

# --------------------------------------------

"""
Como já dito anteriormente, o package sozinho não faz nada, mas
Existe uma forma de fazer o Python entender o package como se fosse um módulo, criando um arquivo dentro dele chamado '__init__.py' precisa ser escrito dessa forma, porque caso contrario ele não vai entender do que se trata e tratar como um modulo normal. Para isso funcionar, só vamos precisar importar o que nos interessa para o init e depois poderemos importar o package e usar o namespace dele para chamar funções. Nesse caso talvez seja interessante usar o * (all) como dito, é uma má pratica importar tudo, porém nesse caso pode ser bom. Imagine que criamos uma nova função dentro de algum dos modulos e esquecemos de importar manualmente para o init, o código não vai funcionar, então fazendo dessa forma se torna mais dinamico. Lembrando que temos que importar lá no init considerando o ponto de vista da __main__ caso contrario não irá 
"""

# Lá no package eu já criei o init e já importei tudo.

import aula99_package

a = aula99_package.fala_oi()
b = aula99_package.soma(2, 3)
print(a)
print(b)
