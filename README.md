# Connect Four

Jogo Connect Four (Quatro em Linha) desenvolvido em Python para a disciplina
INE5201 - Introdução à Ciência da Computação, da Universidade Federal de Santa
Catarina.

## Como executar

Requer Python 3.8 ou superior. A interface usa `tkinter`, incluído na
instalação padrão do Python para Windows.

```bash
python connect_four.py
```

O jogo possui um tabuleiro de 7 colunas por 6 linhas. Os jogadores alternam
entre as fichas vermelha e amarela, escolhendo a coluna pelos botões na parte
superior. Vence quem formar quatro fichas consecutivas na horizontal, vertical
ou diagonal. A coluna cheia é rejeitada e o botão **Reiniciar Jogo** começa uma
nova partida.

## Organização

- `connect_four.py`: regras do jogo e interface gráfica em `tkinter`.

## Uso do GitHub Copilot

O GitHub Copilot foi usado como assistente durante o desenvolvimento. Foram
solicitadas sugestões para estruturar as funções do tabuleiro, detectar quatro
fichas em todas as direções e organizar os componentes da interface. As
sugestões foram revisadas, adaptadas e testadas manualmente para compreender
as regras e manter o código de autoria do projeto.
