# Pythermo

Status: jogo completo no terminal, com modo livre, modo diário, ranking, modo admin, exportação de CSV e backup.

Termo no terminal, feito em Python com os dados salvos em JSON.

## Visão geral

Pythermo é um jogo inspirado no Termo e em outros jogos de navegador. Em cada partida, o jogador tem que adivinhar uma palavra de cinco letras em até seis tentativas. A cada chute, o jogo mostra o que está certo, o que está no lugar errado e o que não existe na palavra.

Existem dois modos: no **livre**, a palavra é aleatória e muda a cada partida; no **diário**, todos os jogadores recebem a mesma palavra, que muda todos os dias.

O jogo guarda as vitórias, as derrotas e a sequência de cada jogador e monta um ranking com os melhores. Tudo fica salvo em um arquivo JSON, sem banco de dados e sem bibliotecas externas.

## Como ler as dicas

Depois de digitar a palavra, cada letra aparece com um sinal que indica se ela está no lugar certo.

- Palavra: NUVEM
- Chute: NEGAR
- Resultado: `[N] {E} _G_ _A_ _R_`

| Sinal | Significado |
| --- | --- |
| `[N]` | letra certa, no lugar certo |
| `{E}` | letra existe na palavra, mas em outra posição |
| `_G_` | letra não existe na palavra |

## Como o projeto foi feito

O projeto foi planejado e organizado por Felipe Barbosa Santos, que também fez a base do jogo (`main.py` e `dados.py`) e a revisão final.

O código foi dividido em módulos, cada um cuidando de uma parte:

- **Partida e palavra do dia** (`jogo.py`) e **registro de partidas e sequência de vitórias** (`jogadores.py`): Gabriel Barbarini
- **Modo admin** (`admin.py`), **ranking e histórico** (`jogadores.py`) e **estatística das palavras** (`relatorios.py`): Eduardo Bargueiras
- **Exportar ranking para CSV e backup** (`relatorios.py`): Richard Murilo

## Objetivos

É um trabalho da disciplina de Programação e Algoritmos (PA), e serviu para estudar:

- Funções e divisão do código em módulos
- Listas, dicionários e strings
- Leitura e escrita de arquivos JSON
- Exportação de dados para CSV
- Validação de entradas do usuário
- Trabalho em equipe com Git e GitHub

(E também serviu para colocar em prática aquilo que aprendemos no ano escolar).

## Funcionalidades

**Jogo**
- [x] Palavra de 5 letras com 6 tentativas
- [x] Dicas por letra: certa, no lugar errado ou ausente
- [x] Modo livre, com palavra aleatória
- [x] Modo diário, com a mesma palavra para todos

**Jogadores**
- [x] Registro de vitórias e derrotas
- [x] Sequência de vitórias, que reinicia ao perder
- [x] Ranking com mais vitórias e maiores sequências
- [x] Histórico de partidas

**Modo admin**
- [x] Cadastrar palavra (5 letras, só letras, sem repetir)
- [x] Listar palavras com o total
- [x] Remover palavra com confirmação

**Relatórios**
- [x] Estatística das palavras
- [x] Exportar o ranking para CSV
- [x] Backup dos dados em JSON

## Estrutura do projeto

```
Pythermo/
├── main.py
├── dados.py
├── jogo.py
├── jogadores.py
├── admin.py
├── relatorios.py
├── MANUAL.md
└── pythermo_dados.json   (criado sozinho na primeira vez)
```

## Rodando localmente

### Requisitos

- Python 3.10 ou mais novo

```bash
git clone https://github.com/felipebsa/Pythermo.git
cd Pythermo
python main.py
```

Na primeira vez, o arquivo `pythermo_dados.json` é criado sozinho com 30 palavras.

## Modo admin

Para cuidar das palavras do jogo, escolha a opção **6 - Modo admin** no menu principal e digite a senha. Se a senha estiver errada, o jogo avisa e volta para o menu. A senha está no [manual](MANUAL.md).

```
PAINEL DE ADMIN

1 - Cadastrar palavra
2 - Listar palavras
3 - Remover palavra
0 - Voltar
```

Para cadastrar, a palavra precisa ter exatamente 5 letras, só letras (sem números, espaços ou acentos) e não pode já existir no jogo. Ela é salva em maiúsculo. Para remover, digite o número da palavra (veja na opção de listar) e confirme com `s` ou cancele com `n`.

## Exportar o CSV e fazer backup

- **Opção 7 do menu:** cria o `ranking.csv` na pasta do `main.py`, com nome, vitórias, derrotas, sequência atual e melhor sequência. Dá para abrir no Excel ou em outra planilha.
- **Opção 8 do menu:** copia o `pythermo_dados.json` para um arquivo com data e hora no nome, como `backup_20261103_083000.json`.

## Tecnologias

- Python 3.10+
- JSON (armazenamento dos dados)
- CSV (exportação do ranking)

## Quem faz

| Integrante | Parte |
| --- | --- |
| Felipe Barbosa Santos | Ideia, planejamento, base (`main.py` e `dados.py`) e revisão |
| Gabriel Barbarini | Lógica da partida e palavra do dia (`jogo.py`), registro de partida e sequência de vitórias (`jogadores.py`) |
| Eduardo Bargueiras | Modo admin (`admin.py`), ranking e histórico (`jogadores.py`), estatística das palavras (`relatorios.py`), README e manual |
| Richard Murilo | Exportar ranking para CSV e backup (`relatorios.py`) |

Trabalho da disciplina de Programação e Algoritmos (PA), da turma 1C2 da ETEC Vasco Antonio Venchiarutti.

## Sites que nos inspiraram

- [Termo](https://term.ooo), o jogo de adivinhar palavras que deu origem a tudo
- [Wordle](https://www.nytimes.com/games/wordle/index.html), o jogo original em que o Termo se baseia
