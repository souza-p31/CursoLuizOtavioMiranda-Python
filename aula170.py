# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

import os

caminho = os.path.join('/home','pedro-souza','Área de Trabalho')
print(caminho)

for pasta in os.listdir(caminho):
    print('Arquivo:', pasta)
    if not os.path.isdir(caminho):
        print('Pasta: ',pasta)