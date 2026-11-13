
nota1 = float(input("Qual sua nota? "))

nota2 = float(input("Qual sua nota? "))

nota3 = float(input("Qual sua nota? "))

nota4 = float(input("Qual sua nota? "))
              
media = (nota1 + nota2 + nota3 + nota4 ) /4 

print(f"A media das suas notas é: {media}")

if media >= 5:
 print("Voce foi aprovado!")

else:
 print("Você foi reprovado!")