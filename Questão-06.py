"""
O DBA da empresa criou um script para fazer uma atualização no banco de dados
MongoDB:
var sku = "" // a pessoa informa o sku aqui
var estoque = 0 // valor a ser informado do novo estoque
db.produto.update(
{
sku: sku
},
{
$inc: estoque
}
)
"""

print('-=-=-=-=-=-=-=-=PROVA DA GAMA-=-=-=-=-=-=-=-=')

def ajustar_estoque(sku, estoque, collection):
    collection.update_one({"sku": sku}, {"$set": {"estoque": estoque}})

if __name__ == '__main__':
    sku = input('Digite o sku: ')
    estoque = int(input("Qual o estoque: "))
    print()