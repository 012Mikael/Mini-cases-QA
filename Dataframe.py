#data freme 
'''
Crie um DataFrame com os seguintes dados:

Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus

Depois, filtre os dados para exibir na tela apenas os moradores do Recife. 
'''

dados = {
    "nome" : ['João', 'Marta', 'Ary', 'caio', 'Lucas', 'Julia', 'Marcos'],
    "idade" : [51, 37, 23, 21, 18, 35, 42],
    "cidade" : ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus'],
}

import pandas as pd 
city = pd.DataFrame(dados)

Moradores_recife = city[city['cidade'] == 'Recife'] 

print(Moradores_recife)