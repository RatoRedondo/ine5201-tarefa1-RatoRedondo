# Connect Four

Jogo **Connect Four (Quatro em Linha)** desenvolvido em Python para a
disciplina **INE5201 - Introdução à Ciência da Computação**, da Universidade
Federal de Santa Catarina.

## Sobre o jogo

Connect Four é um jogo para duas pessoas em um tabuleiro de **7 colunas por
6 linhas**. Em cada turno, o jogador escolhe uma coluna e sua ficha ocupa a
posição mais baixa disponível. Ganha quem formar uma sequência de quatro fichas
na horizontal, vertical ou diagonal.

## Funcionalidades

- Interface gráfica desenvolvida com `tkinter`;
- identificação visual dos jogadores por cores:
  - Jogador 1: vermelho;
  - Jogador 2: amarelo;
- alternância automática de turnos;
- gravidade das fichas;
- validação de colunas cheias;
- detecção de vitória em todas as direções;
- detecção de empate quando o tabuleiro fica cheio;
- botão **Reiniciar Jogo** para começar uma nova partida;
- desativação automática de colunas cheias ou após o encerramento da partida.

## Requisitos

- Python 3.8 ou superior;
- `tkinter`, normalmente incluído na instalação padrão do Python.

O projeto não possui dependências externas.

## Como executar

Na pasta do projeto, execute:

```bash
python connect_four.py
```

Na primeira jogada, o Jogador 1 começa. Use os botões numerados acima do
tabuleiro para inserir as fichas.

## Testes

Os testes das regras principais podem ser executados com:

```bash
python -m unittest test_connect_four.py
```

Eles verificam a queda das fichas, a rejeição de colunas cheias, as vitórias
horizontal, vertical e diagonal, além do empate.

## Estrutura do projeto

| Arquivo | Descrição |
| --- | --- |
| `connect_four.py` | Regras do jogo e interface gráfica. |
| `test_connect_four.py` | Testes automatizados das regras. |

## Uso do GitHub Copilot

O GitHub Copilot foi utilizado como assistente durante o desenvolvimento para
explorar a estrutura das funções do tabuleiro, a detecção de sequências de
quatro fichas e a organização da interface. As sugestões foram revisadas,
adaptadas e testadas manualmente, mantendo a compreensão do código e das
regras implementadas.
