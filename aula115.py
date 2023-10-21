"""
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação
Do Python Para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.
venv é o módulo que vamos usar para criar ambientes virtuais.
Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
venv env .venv .env

Basicamente, quando criamos um ambiente virtual, é como se criassemos um local isolado onde podemos fazer as instalações e os scripts que precisamos sem interferencias externas. Normalmente o terminal executa o script no python instalado na máquina, mas no ambiente virtual ele executa o no python que está dentro do ambiente virtual. Através do comando "gcm python.exe" podemos ver o local onde ele está sendo executado (serve até como teste para ver se está sendo executado no local certo).

Para criar o ambiente virtual usamos python -m venv (nome do ambiente)    ("m" executa um script no terminal, nesse caso para criar o ambiente usando o modulo venv).

Para ativar o ambiente virtual, só precisamos acessar a pasta que foi criada, dentro dela em algum lugar vai ter um arquivo que ativa e outro que desativa (independente do SO). Então nesse caso basta por exemplo acessar pelo terminal .\venv\Scripts\Activate e para desativar a mesma coisa .\venv\Scripts\Deactivate. 

No VScode na parte inferir podemos selecionar o interpretador que será usado, é bom conferir se está no do ambiente virtual para não acabar instalando as coisas no local errado. Pela barra de pesquisa também tem como encontrar usando >select interpreter.

o pip é um diretório onde ficam armazenadas várias bibliotecas do Python, por isso é muito comum usarmos ele para instalar coisas, por exemplo pip install pymysql (no windows pode acontecer do pip não funcionar legal, então precisamos dizer para o terminal que estamos executando um script python, dessa forma: python -m pip install pymysql). Com o comando pip freeze podemos ver quais bibliotecas estão instaladas no nosso ambiente. Caso aconteceça de instalarmos uma biblioteca e depois acabarmos não usando, basta desinstalar para não ter arquivos inuteis pesando o programa, usando pip uninstall pymysql. Esse freeze é importante porque ele mostra exatamente o que vai aparecer em um arquivo chamado requirements, que são os passos necessários para recriar aqueel ambiente virtual. As bibliotecas costumam ter várias versões, caso acontecer de precisarmos de uma versão expecifica, podemos usar pip index versions pymysql para mostrar as versões, e para instalar podemos usar pip install pymysql=="numero da versão".

O arquivo de requirements tira um pouco da necessidade de ficar transportando a pasta venv por aí (que tende a ficar bem pesada). Isso porque ele requistra as bibliotecas que estavam no ambiente e permite recriar ele inteiro apenas com um comando. 
Para criar o arquivo de requirements só precisamos executar o comando pip freeze > "nome do arquivo"(mas geralmente é requirements.txt). Se abrirmos iremos ver que lá estão registradas as libs e suas versões. Podemos até fazer o teste de apagar a pasta venv, depois recria-la com python -m venv venv, claro que sem as bibliotecas o código não irá funcionar, mas agora não precisamos instalar item por item correndo o risco de esquecer algo, basta executar python -r "arquivo de requirements" e deixar ele recriar o ambiente. Lembrando que, caso a gente instale novas libs depois de criar o arquivo de requirements, vamos precisar atualizar ele, aí é só executar novamente o comando pip freeze > requirements.txt.

"""

