# Manual do Pythermo


## O que é o Pythermo

Pythermo é um jogo inspirado em jogos de navegador como o famoso Termo,
e nele você tem que adivinhar uma palavra de cinco letras em seis tentativas ou menos.

(É um ótimo jogo para se divertir com os amigos e competir para ver quem é o melhor!)


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


## Modo admin

Basicamente o modo admin serve para cuidar das palavras do jogo. Para entrar, escolha a opção **6 - Modo admin** no menu principal e digite a senha (e a senha super secreta é `1c2`). Se a senha estiver errada, o jogo avisa e volta para o menu principal.

Depois da senha, aparece o painel de admin:

```
PAINEL DE ADMIN

1 - Cadastrar palavra
2 - Listar palavras
3 - Remover palavra
0 - Voltar
```

### Cadastrar palavra
Nessa função você pode digitar a palavra que você quer adicionar. Só que precisa cumprir algumas condições: 1 - ela precisa ter exatamente 5 letras, 2 - só letras (sem números, espaços ou acentos) e 3 - não pode já estar cadastrada no jogo. Se algo estiver errado, o jogo explica o erro e nada é cadastrado. Quando dá certo, a palavra é salva em maiúsculo.

### Listar palavras
Mostra todas as palavras cadastradas, numeradas, e o total no final.

EX:\n
1 - ARROZ\n
2 - BAGRE\n
3 - PELOS\n
TOTAL: 3

### Remover palavra
Digite o **número** da palavra que você quer remover (use a opção de listar para ver a numeração). O jogo mostra a palavra encontrada e pergunta se você quer mesmo remover: digite `s` para confirmar ou `n` para cancelar.

### Voltar
A opção `0` volta para o menu principal.


## Exportar o CSV e fazer backup

### Exportar ranking pra CSV
Escolha a opção **7** no menu principal. O jogo cria o arquivo `ranking.csv` na mesma pasta onde está o `main.py`, com a tabela do ranking (nome, vitórias, derrotas, sequência atual e melhor sequência). Esse arquivo pode ser aberto no Excel ou em outro programa de planilhas.

### Fazer backup dos dados
Escolha a opção **8** no menu principal. O jogo faz uma cópia de segurança do arquivo `pythermo_dados.json` e salva na mesma pasta, com a data e a hora no nome, por exemplo `backup_20261103_083000.json`. O nome do arquivo criado aparece na tela.
