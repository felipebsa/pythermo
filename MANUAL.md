# Manual do Pythermo

> TODO Eduardo: escrever o manual de uso pra quem nunca jogou.
> Sugestão de partes:
> - Como entrar no modo admin e cadastrar/remover palavras
> - Exportar o CSV e fazer backup (onde os arquivos aparecem)


## O que é o Pythermo

Pythermo é um jogo inspirado em Termo e Wordle,
onde você tem que adivinhar uma palavra de cinco letras em seis tentativas ou menos.


## Como ler as dicas

Após digitar a palavra cada letra terá um sinal indicando se ela está no lugar correto, exemplos:

- Palavra: NUVEM
- Chute: NEGAR
  
- Resultado: [N] {E} _G_ _A_ _R_

As letras que estão entre underlines '_' não estão na palavra que você tem que adivinhar.
As letras que estão entre colchetes '[]' estão no lugar correto da palavra que você tem que adivinhar.
As letras que estão entre chaves '{}' estão na palavra porém na posição errada.


## Modos de jogo

Existem dois modos de jogo no Pythermo, o modo livre e o modo diario.

### Livre
- No modo livre você recebe uma palavra aleatória para adivinhar que muda toda vez.

### Diario
- No modo diario todos os jogadores recebem a mesma palavra para adivinhar, ela muda todos os dias.


## Ranking e sequência de vitórias

O ranking mostra os jogadores com o maior número de vitórias e de sequência de vitórias.

Toda vez que você adivinhar uma palavra corretamente a sua sequência de vitórias aumentará, ela será reiniciada se você perder alguma vez.
