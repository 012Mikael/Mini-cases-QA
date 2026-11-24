#RETURN
#Faça um código para formar a soma de dois números, usando o comando 'return'.

def Calculo (a , b):
    resultado = a + b 
    return resultado
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = Calculo(a, b)
print(f"A soma de {a} e {b} é: {soma}")
