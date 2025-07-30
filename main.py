def gerarSenha():
    while True:
        print("1 - Gerar senha pouco segura")
        print("2 - Gerar senha segura")
        print("3 - Gerar senha muito segura")
        x = input("Selecione qual senha quer gerar: ")
        
        if x == "1":
            print("Opcao 1 selecionada.")
            break
        elif x == "2":
            print("Opcao 2 selecionada.")
            break
        elif x == "3":
            print("Opcao 3 selecionada.")
            break
        else:
            print("Opcao invalida.")
            return

while True:
    print("-"*7 + "GERADOR DE SENHA" + "-"*7)
    gerarSenha()