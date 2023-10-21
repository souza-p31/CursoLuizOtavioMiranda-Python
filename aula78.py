"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.
"""

# Criando um set
# set(iterável) ou {1, 2, 3} # com dados
# s1 = set('Luiz')

"""
Sets são eficientes para remover valores duplicados
de iteráveis.
Não aceitam valores mutáveis
Seus valores serão sempre únicos
Não tem indexes
Não garantem ordem
São iteráveis (for, in, not in)
"""

# s1 = {1, 2, 3, [123]} #Vai retornar um erro, pois set só aceita valores imutáveis
# s1 = {1, 2, 3, (123,)} #Não vai retornar erro, porque a lista foi trocada por uma tupla, e tuplas são imutáveis. Tem que ter uma virgula sobrando, se não ele não entende que é uma tupla.
# print(s1)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# print(s1) #Seus valores serão sempre únicos

# # print(s1[1]) #Vai dar erro, porque sets não tem index
# s2 = {'Pedro', 1, 2, 3}
# print(s2, type(s2)) # Set não garante ordem

# for c in s1:
#     print(c)
# for d in s2:
#     print(d) #Sets são iteráveis


"""
Métodos úteis:
add, update, clear, discard
"""
# s1 = set()
# s1.add('Luiz') #add adiciona um item no set
# # s1.add(1, 2) #porem só pode adicionar um por vez
# # s1.update('Olá mundo') #update é parecido com o add, porém ele já itera e não garante ordem
# s1.update(('Olá mundo',1, 2)) #uma forma de contornar isso é adicionar dentro de um iteravel
# # s1.clear() #limpa o set inteiro
# s1.discard('Olá mundo') #como o set não tem indice, mas tem valores unicos, podemos nos referenciar a eles pelo proprio valor
# s1.discard('Luiz')
# print(s1)

"""
Operadores úteis:
união | união (union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ - itens que não estão em ambos 
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  #usando pipe ele une dois sets, porém como nos sets os valores são unicos os valores repetidos somem
s3 = s1 & s2 #o ecomercial faz uma intersecção nos dois sets e retorna os itens presentes em ambos  
s3 = s1 - s2 #o menos faz a diferença entre os sets e retorna os itens do set a esquerda que NÃO estão presentes no set a direita
s3 = s1 ^ s2 #o circunflexo faz a diferença simétrica e retorna os itens que estão presentes em ambos os sets independente da ordem
print(s3)