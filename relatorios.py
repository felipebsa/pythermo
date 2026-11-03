# relatorios.py
#   palavras_dificeis -> Eduardo
#   exportar_ranking_csv e fazer_backup -> Richard Murilo

import csv
import shutil
from datetime import datetime

from dados import ARQUIVO_DADOS


def palavras_dificeis(dados):
    contagem = {}

    for partida in dados["partidas"]:
        if not partida["venceu"]:
            palavra = partida["palavra"]
            contagem[palavra] = contagem.get(palavra, 0) + 1

    if len(contagem) == 0:
        print("\nNinguém perdeu ainda. (ainda tá sobrando algo)")
        return

    ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    print("\n===============================================")
    print("PALAVRAS QUE MAIS DERRUBAM (mogaram os betas)\n")

    for posicao, item in enumerate(ordenadas[:5], start=1):
        palavra = item[0]
        derrotas = item[1]
        print(f"{posicao}. {palavra} - {derrotas} derrotas")


def exportar_ranking_csv(dados):
    """
    Cria o arquivo "ranking.csv" com uma linha de cabeçalho:
        nome, vitorias, derrotas, sequencia_atual, melhor_sequencia
    e uma linha pra cada jogador de dados["jogadores"].
    No fim mostra uma mensagem dizendo que exportou.
    Dica: tem uma função parecida no snack-bar (export_report_csv).
    """
    # TODO: Richard
    print("Exportação ainda não implementada.")


def fazer_backup():
    """
    Copia o ARQUIVO_DADOS pra um arquivo com a data e hora no nome,
    tipo "backup_20261024_163000.json", e mostra o nome do arquivo criado.
    Dica: tem uma função parecida no snack-bar (backup_data).
    """
    # TODO: Richard
    print("Backup ainda não implementado.")