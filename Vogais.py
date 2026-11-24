'''Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.
Solicitação de Entrada:

Implementem a solicitação de entrada de uma palavra (string).
Contagem de Vogais:

Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra. '''

contagem_vogais = 0
palavra = str(input("Digite uma palavra: "))

for letra in palavra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        contagem_vogais += 1
    break

print(f"O número total de vogais na palavra '{palavra}' é: {contagem_vogais}")