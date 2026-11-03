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

    for jogador in dados["jogadores"]:
        if jogador["nome"].lower() == nome.lower():
            return jogador

    jogador_novo ={
        "nome": nome,
        "vitorias": 0,
        "derrotas": 0,
        "sequencia_atual": 0,
        "melhor_sequencia": 0
    }

    dados["jogadores"].append(jogador_novo)

    return jogador_novo

    # TODO: Gabriel

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
    
    jogador = buscar_jogador(dados, nome)

    if venceu:
        jogador["vitorias"] += 1
        jogador["sequencia_atual"] += 1

        if jogador["sequencia_atual"] > jogador["melhor_sequencia"]:
            jogador["melhor_sequencia"] = jogador["sequencia_atual"]

    else:
        jogador["derrotas"] += 1
        jogador["sequencia_atual"] = 0   # sobrou nada pro beta

    partida = {
        "jogador": nome,
        "palavra": palavra,
        "venceu": venceu,
        "tentativas": tentativas,
        "modo": modo,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    dados["partidas"].append(partida)

    salvar_dados(dados)

    # TODO: Gabriel


def mostrar_ranking(dados):
    jogadores = dados["jogadores"]

    if len(jogadores) == 0:
        print("\nAinda não há jogadores no ranking.")
        return

    ordenados = sorted(jogadores, key=lambda j: j["vitorias"], reverse=True)

    print("\n===============================================")
    print("RANKING\n")
    print(f"{'Pos':<6}{'Nome':<16}{'Vitórias':<10}{'Derrotas':<10}{'Seq. atual':<12}{'Melhor seq.'}")
    print("-" * 65)

    for posicao, jogador in enumerate(ordenados, start=1):
        nome = jogador["nome"]
        vitorias = jogador["vitorias"]
        derrotas = jogador["derrotas"]
        atual = jogador["sequencia_atual"]
        melhor = jogador["melhor_sequencia"]
        print(f"{posicao:<6}{nome:<16}{vitorias:<10}{derrotas:<10}{atual:<12}{melhor}")


def mostrar_historico(dados):
    partidas = dados["partidas"]

    if len(partidas) == 0:
        print("\nAinda não há partidas no histórico.")
        return

    print("\n===============================================")
    print("HISTÓRICO DE PARTIDAS\n")

    for partida in partidas:
        data = partida["data"]
        jogador = partida["jogador"]
        palavra = partida["palavra"]
        tentativas = partida["tentativas"]

        if partida["venceu"]:
            resultado = "ganhou"
        else:
            resultado = "perdeu"

        print(f"{data} | {jogador} | {palavra} | {resultado} em {tentativas} tentativas")