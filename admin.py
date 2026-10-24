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
    """
    Mostra todas as palavras cadastradas (numeradas) e o total no final.
    """
    # TODO: Eduardo
    print("Listagem ainda não implementada.")


def remover_palavra(dados):
    """
    Pede a palavra, confere se existe, pede confirmação (s/n)
    e remove. Depois salva.
    """
    # TODO: Eduardo
    print("Remoção ainda não implementada.")


def menu_admin(dados):
    """
    Pede a senha (SENHA_ADMIN). Se errar, volta pro menu principal.
    Se acertar, mostra um submenu:
        1 - Cadastrar palavra
        2 - Listar palavras
        3 - Remover palavra
        0 - Voltar
    Dica: dá pra copiar o jeito que o main() do main.py faz o menu.
    """
    # TODO: Eduardo
    print("Modo admin ainda não implementado.")
