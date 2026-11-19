for frequencia in range (0, 22):
    print(f"Frequência é {frequencia}")

    presenca = input("O aluno veio hoje? ")
    if frequencia != 21:
        if presenca == "Sim":
            frequencia += 1

            print('VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO')

            print(f"A frequencia atual é {frequencia}.")
        elif presenca == "não":
            break
    elif frequencia == 21:
        print('UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ')