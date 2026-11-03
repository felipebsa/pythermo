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

    chute = chute.upper()
    palavra = palavra.upper()

    resultado = ["nao"] * 5
    letras_restantes = {}

    for i in range (TAMANHO_PALAVRA):
        if chute[i] == palavra[i]:
            resultado[i] = "certo"

        else:
            letra = palavra[i]
            letras_restantes[letra] = letras_restantes.get(letra, 0) + 1

    for i in range (TAMANHO_PALAVRA):
        if resultado[i] == "certo":
            continue

        letra = chute[i]

        if letras_restantes.get(letra, 0) > 0:
            resultado[i] = "existe"
            letras_restantes[letra] -= 1

    return resultado


    # TODO: Gabriel

def mostrar_dicas(chute, resultado):
    """
    Mostra o chute na tela de um jeito que dê pra entender o resultado.
    Pode ser do jeito que você quiser, por exemplo:
        [C] -> certo   (C) -> existe   _C_ -> não existe
    Se quiser usar cor no terminal, fica à vontade.
    """

    for letra, res in zip(chute, resultado):
        if res == "certo":
            print(f"[{letra}]", end=" ")
        elif res == "existe":
            print(f"({letra})", end=" ")
        else:
            print(f"_{letra}_", end=" ")


    # TODO: Gabriel

def pedir_chute():
    """
    Pede um chute pro jogador e só aceita se tiver 5 letras e só letras.
    Devolve o chute em MAIÚSCULO.
    """
    
    chute = input("Digite uma palavra de 5 letras: ").strip().upper()

    if len(chute) != 5:
        print("A palvra tem que ter 5 letras. ")

    elif not chute.isalpha():
        print("A palavra só pode conter letras. ")

    else:
        return chute
        
    # TODO: Gabriel

def palavra_do_dia(dados):
    """
    Devolve a palavra do dia: tem que ser a mesma pra todo mundo no mesmo dia
    e mudar no dia seguinte. A ideia é usar a data de hoje (date.today())
    pra escolher uma posição da lista dados["palavras"].
    """
    palavra = dados["palavras"]

    indice = date.today().toordinal() % len(palavra)

    return palavra[indice].upper() 
    
    # TODO: Gabriel
    
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
    
    if modo == "livre":
        palavra = random.choice(dados["palavras"]).upper()

    else:
        palavra = palavra_do_dia(dados)

    tentativas = 0
    venceu = False

    while tentativas < MAX_TENTATIVAS:
        print(f"\n Tentativa {tentativas + 1} de 6 \n")

        chute = pedir_chute()

        tentativas += 1

        resultado = verificar_chute(chute, palavra)

        mostrar_dicas(chute, resultado)

        if chute == palavra:
            venceu = True
            break

    print("\n Resultado \n")

    if venceu:
        print("Você acertou a palavra. ")
        print(f"Palavra: {palavra}")
        print(f"Você venceu em {tentativas} tentativas")

    else:
        print("Você perdeu. ")
        print(f"A palavra era: {palavra}")

    # Salvar a partida
    registrar_partida(
        dados,
        nome_jogador,
        palavra,
        venceu,
        tentativas,
        modo
    )

    salvar_dados(dados)

    print("Partida registrada com sucesso!")

    # TODO: Gabriel
