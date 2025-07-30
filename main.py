def gerarSenha():
    print("1 - Gerar senha pouco segura")
    print("2 - Gerar senha segura")
    print("3 - Gerar senha muito segura")
    x = input("Selecione qual senha quer gerar: ")
    
    if x is not int:
        print("Opcao invalida. Digite somente o numero: ")
        return
    elif x == "1":
        print("Opcao 1 selecionada.")
    elif x == "1":
        print("Opcao 2 selecionada.")
    elif x == "1":
        print("Opcao 3 selecionada.")
    else:
        print("Opcao invalida.")
        return

while True:
    print("-"*5 + "GERADOR DE SENHA" + "-"*5)