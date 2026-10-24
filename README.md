# Pythermo

Termo no terminal, feito em Python com os dados salvos em JSON.
Trabalho de Programação e Algoritmos (PA) da turma 1C2 da ETEC Vasco Antonio Venchiarutti.

> TODO Eduardo: completar este README (sobre o jogo, como jogar, funcionalidades,
> estrutura do JSON, arquivos gerados, integrantes). Dá pra se basear no README do
> https://github.com/felipebsa/snack-bar

## Como rodar

Precisa de Python 3.10 ou mais novo.

```bash
git clone https://github.com/felipebsa/Pythermo.git
cd Pythermo
python main.py
```

Na primeira vez o arquivo `pythermo_dados.json` é criado sozinho com 30 palavras.

## Quem faz o quê

| Integrante | Parte |
| --- | --- |
| Felipe Barbosa Santos | Ideia, planejamento, base (`main.py` e `dados.py`) e revisão |
| Gabriel Barbarini | Lógica da partida e palavra do dia (`jogo.py`), registro de partida e sequência de vitórias (`jogadores.py`) |
| Eduardo Bargueiras | Modo admin (`admin.py`), ranking e histórico (`jogadores.py`), estatística das palavras (`relatorios.py`), README e manual |
| Richard Murilo | Exportar ranking pra CSV e backup (`relatorios.py`) |
