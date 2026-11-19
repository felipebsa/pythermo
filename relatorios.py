# relatorios.py
#   palavras_dificeis -> eduardo
#   exportar_ranking_csv e fazer_backup -> Richard Murilo

import csv
import shutil
from datetime import datetime

from dados import ARQUIVO_DADOS


def palavras_dificeis(dados):
    """
    Mostra as palavras que mais derrubam gente: conta, em dados["partidas"],
    quantas vezes cada palavra apareceu numa partida perdida (venceu == False)
    e mostra da que mais derrubou pra que menos derrubou (top 5 tá bom).
    Se ninguém perdeu ainda, avisa.
    """
    partidas = dados["partidas"]
    derrotas_por_palavra = {}

    for partida in partidas:
        if not partida["venceu"]:
            palavra = partida["palavra"]
            if palavra in derrotas_por_palavra:
                derrotas_por_palavra[palavra] += 1
            else:
                derrotas_por_palavra[palavra] = 1

    if len(derrotas_por_palavra) == 0:
        print("\nAinda não há derrotas registradas.")
        return

    ordenados = sorted(derrotas_por_palavra.items(), key=lambda item: item[1], reverse=True)
    top_5 = ordenados[:5]

    print("\n===============================================")
    print("PALAVRAS QUE MAIS DERRUBAM\n")
    print(f"{'Pos':<6}{'Palavra':<16}{'Derrotas'}")
    print("-" * 35)

    for posicao, item in enumerate(top_5, start=1):
        palavra = item[0]
        derrotas = item[1]
        print(f"{posicao:<6}{palavra:<16}{derrotas}")


def exportar_ranking_csv(dados):
    """
    Cria o arquivo "ranking.csv" com uma linha de cabeçalho:
        nome, vitorias, derrotas, sequencia_atual, melhor_sequencia
    e uma linha pra cada jogador de dados["jogadores"].
    No fim mostra uma mensagem dizendo que exportou.
    Dica: tem uma função parecida no snack-bar (export_report_csv).
    """
    # RICHARD: Exportação do ranking para CSV

    campos = [
        "nome",
        "vitorias",
        "derrotas",
        "sequencia_atual",
        "melhor_sequencia"
    ]

    jogadores = dados["jogadores"]

    with open("ranking.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()

        for jogador in jogadores:
            escritor.writerow({
                campo: jogador.get(campo, "")
                for campo in campos
            })

    print("Ranking exportado com sucesso para ranking.csv!")


def fazer_backup():
    """
    Copia o ARQUIVO_DADOS pra um arquivo com a data e hora no nome,
    tipo "backup_20261024_163000.json", e mostra o nome do arquivo criado.
    Dica: tem uma função parecida no snack-bar (backup_data).
    """
    # RICHARD: Criação de backup dos dados

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_backup = "backup_" + data_hora + ".json"

    try:
        shutil.copy2(ARQUIVO_DADOS, nome_backup)

        print(f"Backup criado com sucesso: {nome_backup}")

    except FileNotFoundError:
        print("Erro: arquivo de dados não encontrado.")

    except OSError as erro:
        print(f"Erro ao criar backup: {erro}")
