#Crie uma persona com a biblioteca Faker com nome, idade e cidade. Criando o atributo random.int para gerar valores aleatórios para idade.

from faker import Faker 
import pandas as pd

faker = Faker("pt_BR")

for i in range(1, 11):
   pessoas = { 
       'nome' : faker.name(),
       'idade' : faker.random_int(min=18, max=80),
       'cidade' : faker.city(),
   }

pessoas_falsas = pd.DataFrame([pessoas])

print(pessoas_falsas)