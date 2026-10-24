# jogo.py - Gabriel Barbarini
# A lógica da partida: conferir o chute, mostrar as dicas e escolher a palavra.

import random
from datetime import date

from dados import salvar_dados
from jogadores import registrar_partida

MAX_TENTATIVAS = 6
TAMANHO_PALAVRA = 5


def verificar_chute(chute, palavra):
    """
    Compara o chute com a palavra secreta e devolve uma lista com 5 resultados,
    um pra cada letra do chute:
        "certo"  -> letra no lugar certo
        "existe" -> a letra tá na palavra, mas em outra posição
        "nao"    -> a letra não tá na palavra

    Exemplo: verificar_chute("CARRO", "TERMO")
             -> ["nao", "nao", "certo", "nao", "certo"]

    Cuidado com letra repetida (ex: chute "CARRO" tem dois R).
    """
    # TODO: Gabriel
    pass


def mostrar_dicas(chute, resultado):
    """
    Mostra o chute na tela de um jeito que dê pra entender o resultado.
    Pode ser do jeito que você quiser, por exemplo:
        [C] -> certo   (C) -> existe   _C_ -> não existe
    Se quiser usar cor no terminal, fica à vontade.
    """
    # TODO: Gabriel
    pass


def pedir_chute():
    """
    Pede um chute pro jogador e só aceita se tiver 5 letras e só letras.
    Devolve o chute em MAIÚSCULO.
    """
    # TODO: Gabriel
    pass


def palavra_do_dia(dados):
    """
    Devolve a palavra do dia: tem que ser a mesma pra todo mundo no mesmo dia
    e mudar no dia seguinte. A ideia é usar a data de hoje (date.today())
    pra escolher uma posição da lista dados["palavras"].
    """
    # TODO: Gabriel
    pass


def jogar(dados, nome_jogador, modo):
    """
    Roda uma partida inteira.
    modo == "livre"  -> palavra sorteada com random
    modo == "diario" -> palavra_do_dia(dados)

    Passos:
    1. escolher a palavra
    2. repetir até MAX_TENTATIVAS: pedir chute, verificar, mostrar dicas
    3. parar se acertar
    4. no fim mostrar se ganhou ou perdeu (e qual era a palavra)
    5. chamar registrar_partida(dados, nome_jogador, palavra, venceu, tentativas, modo)
    """
    if not dados["palavras"]:
        print("Não tem nenhuma palavra cadastrada. Cadastre no modo admin.")
        return

    # TODO: Gabriel
    print("Partida ainda não implementada.")
