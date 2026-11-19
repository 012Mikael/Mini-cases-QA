x = 0

while x < 5:
    print(f"o valor de {x} é menor que 5")
    x += 2

print("o valor de x é maior ou igual a 5")
print("fim do while")

print(50*"=")

numero_secreto = 7
acertou = False

while not acertou:
    chute = int(input("Digite um número entre 1 e 10: "))
    
    if chute == numero_secreto:
        acertou = True
        print("Parabéns! Você acertou o número secreto!")
    else:
        print("Tente novamente!")
