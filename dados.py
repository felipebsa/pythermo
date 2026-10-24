# dados.py - parte pronta (Felipe)
# Carrega e salva tudo no arquivo JSON. Ninguém precisa mexer aqui,
# é só usar carregar_dados() e salvar_dados(dados) nos outros arquivos.

import json
import os

ARQUIVO_DADOS = "pythermo_dados.json"

PALAVRAS_INICIAIS = [
    "TERMO", "CAMPO", "LIVRO", "PRAIA", "CHUVA", "NOITE", "PEDRA", "VERDE",
    "FORTE", "MUNDO", "PORTA", "CARRO", "PLANO", "SONHO", "TEMPO", "FESTA",
    "NUVEM", "PEIXE", "BANCO", "GRITO", "LETRA", "JOGAR", "FRUTA", "CINTO",
    "PRATO", "TIGRE", "ZEBRA", "AMIGO", "LOUSA", "SALTO",
]


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        dados = {
            "palavras": list(PALAVRAS_INICIAIS),
            "jogadores": [],
            "partidas": [],
        }
        salvar_dados(dados)
        return dados

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
