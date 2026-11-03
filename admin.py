# admin.py - Eduardo Bargueiras
# Modo admin pra cuidar das palavras do jogo.

from dados import salvar_dados

SENHA_ADMIN = "1c2"


def cadastrar_palavra(dados):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    palavra = input("\nDigite a palavra que será cadastrada: (5 letras, sem acento)\n\n>>> ").strip().upper()

    if len(palavra) != 5:
        print("\nErro: a palavra precisa ter 5 letras.")
        return

    for letra in palavra:
        if letra not in alfabeto:
            print("\nErro: a palavra só pode ter letras, sem números, espaços ou acentos.")
            return

    if palavra in dados["palavras"]:
        print("\nErro: essa palavra já está cadastrada.")
        return

    dados["palavras"].append(palavra)
    salvar_dados(dados)
    print(f"\nA palavra {palavra} foi cadastrada com sucesso!")


def listar_palavras(dados):
    contador = 0
    total_palavras = dados["palavras"]

    for indice, palavra in enumerate(total_palavras, start=1):
        contador += 1
        print(f"{indice} - {palavra}")
    print("TOTAL:", contador)


def remover_palavra(dados):
    palavras = dados["palavras"]

    if len(palavras) == 0:
        print("\nNão há palavras cadastradas.")
        return

    escolha = input("\nDigite qual palavra será removida: (coloque o número correspondente a palavra, OBS: use a função de listar para conferir a numeração)\n\n>>> ").strip()

    if not escolha.isdigit():
        print("\nErro: digite apenas o número da palavra.")
        return

    numero = int(escolha)

    if numero < 1 or numero > len(palavras):
        print("\nErro: esse número não existe na lista.")
        return

    palavra = palavras[numero - 1]
    print(f"\nA Palavra foi encontrada!!\n\nPalavra encontrada: {palavra}\n")

    opcao = input("Deseja remover ela? (s/n)\nEscolha: ").strip().lower()

    match opcao:
        case "s":
            palavras.remove(palavra)
            salvar_dados(dados)
            print(f"\nA palavra {palavra} foi removida com sucesso!")
        case "n":
            print("\nRemoção cancelada.")
        case _:
            print("\nOpção inválida. Nada foi removido.")


def menu_admin(dados):
    tentativa_senha = input("\n===============================================\nPor favor, insira a senha para acessar o painel de admin:\n>>> ")

    if tentativa_senha == SENHA_ADMIN:
        while True:
            print("===============================================\nPAINEL DE ADMIN\n")
            print("1 - Cadastrar palavra")
            print("2 - Listar palavras")
            print("3 - Remover palavra")
            print("0 - Voltar")
            opcao = input("\nEscolha: ").strip()

            match opcao:
                case "1":
                    cadastrar_palavra(dados)
                case "2":
                    listar_palavras(dados)
                case "3":
                    remover_palavra(dados)
                case "0":
                    print("\nVoltando ao menu principal...")
                    break
                case _:
                    print("\nOpção inválida.")
            print("\n===============================================\n")

    else:
        print("\nSenha incorreta.")
        return