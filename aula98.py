import aula98_m

# print(aula98_m.variavel)

"""
Por questões de eficiencia os módulos Python são Singleton, o que quer dizer que só pode haver um mesmo modulo executando por vez durante o programa, mas podem haver casos (casos raros) de a gente precisar recarregar o modulo. Para esses casos é feito de uma forma diferente e temos que deixar explicito que o Python precisa recarregar. 
"""
for i in range(10):
    import aula98_m
#     print(i)

# print('fim')




import importlib # modulo que tem a função de recarregar
import aula98_m

# print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('fim')