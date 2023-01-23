"""
Na programação é comum relacionar dados usando um campo que identifica
registros (id). Elabore uma modelagem de dados em que os registros estão
relacionados através de um campo identificador (o id), atendendo as seguintes
afirmações:
"""
print('-=-=-=-=-=-=-=-=PROVA DA GAMA-=-=-=-=-=-=-=-=')

estados = [{'id': 1, 'estado': 'Goiás'}, {'id':2, 'estado': 'Paraná'}]

cidades = [{'id': 1, 'cidade': 'Diamantina', 'estado_id':1},
            {'id': 2, 'cidade': 'Noronha', 'estado_id': 2}]
bairros =  [{'id': 21, 'bairro': 'Betânia', 'cidade_id':11, 'estado_id':1}, {'id':22, 'baiiro':'Agostinho',
                'cidade_id': 12, 'estado_id':2}, {'id':23, 'bairro': 'Natal', 'cidade_id':12, 'estado_id':2}]