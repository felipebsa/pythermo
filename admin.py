# admin.py - Eduardo Bargueiras
# Modo admin pra cuidar das palavras do jogo.

from dados import salvar_dados

SENHA_ADMIN = "1c2"


def cadastrar_palavra(dados):
    """
    Pede uma palavra nova e só cadastra se:
    - tiver exatamente 5 letras
    - só tiver letras (sem número, espaço ou acento)
    - não estiver repetida na lista
    Salva em MAIÚSCULO e chama salvar_dados(dados).
    """
    # TODO: Eduardo
    print("Cadastro ainda não implementado.")


def listar_palavras(dados):
    contador = 0
    total_palavras = dados["palavras"]
    
    for indice, palavra in enumerate(total_palavras, start=1):
        contador += 1
        print(f"{indice} - {palavra}")
    print("TOTAL:", contador)


def remover_palavra(dados):
    """
    Pede a palavra, confere se existe, pede confirmação (s/n)
    e remove. Depois salva.
    """
    # TODO: Eduardo
    remover = int(input("\nDigite qual palavra será removida: (coloque o número correspondente a palavra, OBS: use a função de listar para conferir a numeração)\n\n>>> "))
    total_palavras = len(dados["palavras"])

    if remover >= 1 and remover <= total_palavras:
        print("\nA Palavra foi encontrada!!\n\nPalavra encontrada: \n")

        opcao = input("Deseja remover ela? (s/n)\nEscolha: ").strip()

        match opcao:
            case "s":
                print("aaa")
            case "n":
                print("bbb")



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
                    print("\nSaindo do terminal...")
                    break
                case _:
                    print("\nOpção inválida.")
            print("\n===============================================\n")

    else:
        print("\nSenha incorreta.")
        return