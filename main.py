# main.py - parte pronta (Felipe)
# Menu principal do Pythermo. Só chama as funções dos outros arquivos.

from dados import carregar_dados
from jogo import jogar
from jogadores import mostrar_ranking, mostrar_historico
from admin import menu_admin
from relatorios import palavras_dificeis, exportar_ranking_csv, fazer_backup


def pedir_nome():
    while True:
        nome = input("Seu nome: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def mostrar_menu():
    print("\n===== PYTHERMO =====")
    print("1 - Jogar (palavra aleatória)")
    print("2 - Palavra do dia")
    print("3 - Ranking")
    print("4 - Histórico de partidas")
    print("5 - Palavras que mais derrubam")
    print("6 - Modo admin")
    print("7 - Exportar ranking pra CSV")
    print("8 - Fazer backup dos dados")
    print("0 - Sair")


def main():
    dados = carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha: ").strip()

        match opcao:
            case "1":
                jogar(dados, pedir_nome(), "livre")
            case "2":
                jogar(dados, pedir_nome(), "diario")
            case "3":
                mostrar_ranking(dados)
            case "4":
                mostrar_historico(dados)
            case "5":
                palavras_dificeis(dados)
            case "6":
                menu_admin(dados)
            case "7":
                exportar_ranking_csv(dados)
            case "8":
                fazer_backup()
            case "0":
                print("Valeu por jogar!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
