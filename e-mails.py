'''O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário tem o @jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto.

Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, documente e suba os resultados no Bitrix da sua equipe. 

'''
email = input("Digite o email a ser verificado: ")  

if "@jogajuntoinstituto.org" in email:
    print("O email é válido.")
else:
    print("O email é inválido.")