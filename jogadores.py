# jogadores.py
# Funções de jogador: registrar a partida, sequência de vitórias, ranking e histórico.
#   registrar_partida e buscar_jogador -> Gabriel
#   mostrar_ranking e mostrar_historico -> Eduardo

from datetime import datetime

from dados import salvar_dados


def buscar_jogador(dados, nome):
    """
    Procura o jogador pelo nome em dados["jogadores"] (sem ligar pra maiúscula).
    Se não achar, cria um novo assim e coloca na lista:
        {"nome": nome, "vitorias": 0, "derrotas": 0,
         "sequencia_atual": 0, "melhor_sequencia": 0}
    Devolve o dicionário do jogador.
    """
    # TODO: Gabriel
    pass


def registrar_partida(dados, nome, palavra, venceu, tentativas, modo):
    """
    Chamada no fim de cada partida.
    1. busca o jogador com buscar_jogador
    2. se venceu: +1 vitória, +1 na sequencia_atual e atualiza melhor_sequencia
       se perdeu: +1 derrota e zera a sequencia_atual
    3. adiciona em dados["partidas"]:
        {"jogador": nome, "palavra": palavra, "venceu": venceu,
         "tentativas": tentativas, "modo": modo,
         "data": datetime.now().strftime("%Y-%m-%d %H:%M")}
    4. salvar_dados(dados)
    """
    # TODO: Gabriel
    pass


def mostrar_ranking(dados):
    """
    Mostra os jogadores ordenados por vitórias (quem tem mais em cima).
    Mostra também derrotas, sequência atual e melhor sequência.
    Se não tiver jogador, avisa.
    """
    # TODO: Eduardo
    print("Ranking ainda não implementado.")


def mostrar_historico(dados):
    """
    Lista as partidas de dados["partidas"]: data, jogador, palavra,
    se ganhou ou perdeu e em quantas tentativas.
    Extra (se quiser): perguntar um nome e mostrar só as partidas dele.
    """
    # TODO: Eduardo
    print("Histórico ainda não implementado.")
