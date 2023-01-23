"""
Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se
conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os
seguintes parâmetros:
○ url_conexao: URI de conexão com banco de dados MongoDB, que também
informa a base de dados (database). Por exemplo: a URI
`mongodb://localhost/bancoexemplo', é a string de conexão para o banco
"bancoexemplo" da minha máquina local ("localhost").
○ colecao: É o nome da coleção (collection) do MongoDB que estaremos
acessando com esta função.
Tempo estimado: 6 minutos. Dificuldade: quase média, a pessoa precisará lembrar
como pegar o database ou da URI ou da própria biblioteca.
"""

print('-=-=-=-=-=-=-=-=PROVA DA GAMA-=-=-=-=-=-=-=-=')

from pymongo import MongoClient

url_conexao = MongoClient('mongodb+srv://div_junior:991832Alo@cluster0.ulqdmhn.mongodb.net/?retryWrites=true&w=majority')

def obter_colecao_mongodb(url_conexao, colecao):
    db = MongoClient(url_conexao)
    col = db[colecao]
    return col

if __name__ == '__main__':
    url_conexao = MongoClient('mongodb+srv://div_junior:991832Alo@cluster0.ulqdmhn.mongodb.net/?retryWrites=true&w=majority')
    colecao = 'coleção'

    mongo = obter_colecao_mongodb(url_conexao, colecao)
    print(mongo)
