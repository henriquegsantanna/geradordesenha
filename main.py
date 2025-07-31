import random
import string

def gerarSenha():
    while True:
        print("1 - Gerar senha pouco segura")
        print("2 - Gerar senha segura")
        print("3 - Gerar senha muito segura")
        x = input("Selecione qual senha quer gerar: ")

        if x == "1":
            senha = ''.join(random.choices(string.ascii_letters, k=8))
            print(f"Senha gerada: {senha}")
        elif x == "2":
            print("Opcao 2 selecionada.")
            print(f"Senha gerada: {senha}")
        elif x == "3":
            print("Opcao 3 selecionada.")
            print(f"Senha gerada: {senha}")
        else:
            print("Opção inválida. Tente novamente.")
            continue

        while True:
            print("Deseja gerar uma nova senha?\n1 - Sim\n2 - Não")
            resposta = input("Digite aqui: ")
            if resposta == "1":
                break
            elif resposta == "2":
                return False
            else:
                print("Opção inválida. Digite 1 ou 2.")

while True:
    print("-" * 7 + " GERADOR DE SENHA " + "-" * 7)
    if not gerarSenha():
        break