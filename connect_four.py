import tkinter as tk
from tkinter import messagebox


LINHAS = 6
COLUNAS = 7
VAZIO = 0
JOGADOR_1 = 1
JOGADOR_2 = 2
CORES = {
    VAZIO: "#F4F7FB",
    JOGADOR_1: "#E74C3C",
    JOGADOR_2: "#F1C40F",
}


def criar_tabuleiro():
    return [[VAZIO for _ in range(COLUNAS)] for _ in range(LINHAS)]


def inserir_ficha(tabuleiro, coluna, jogador):
    if not 0 <= coluna < COLUNAS:
        return None

    for linha in range(LINHAS - 1, -1, -1):
        if tabuleiro[linha][coluna] == VAZIO:
            tabuleiro[linha][coluna] = jogador
            return linha
    return None


def verificar_vitoria(tabuleiro, jogador):
    direcoes = ((0, 1), (1, 0), (1, 1), (1, -1))

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if tabuleiro[linha][coluna] != jogador:
                continue
            for deslocamento_linha, deslocamento_coluna in direcoes:
                total = 1
                for passo in range(1, 4):
                    proxima_linha = linha + deslocamento_linha * passo
                    proxima_coluna = coluna + deslocamento_coluna * passo
                    if not (
                        0 <= proxima_linha < LINHAS
                        and 0 <= proxima_coluna < COLUNAS
                    ):
                        break
                    if tabuleiro[proxima_linha][proxima_coluna] != jogador:
                        break
                    total += 1
                if total == 4:
                    return True
    return False


def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[0][coluna] != VAZIO for coluna in range(COLUNAS))


class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.root.resizable(False, False)
        self.tabuleiro = criar_tabuleiro()
        self.jogador_atual = JOGADOR_1
        self.jogo_encerrado = False
        self.botoes_coluna = []
        self.celulas = []
        self.status = tk.StringVar()

        self.criar_interface()
        self.atualizar_status()
        self.desenhar_tabuleiro()

    def criar_interface(self):
        tk.Label(
            self.root,
            text="CONNECT FOUR",
            font=("Arial", 20, "bold"),
            fg="#17324D",
            pady=12,
        ).pack()

        tk.Label(
            self.root,
            textvariable=self.status,
            font=("Arial", 12, "bold"),
            pady=4,
        ).pack()

        controles = tk.Frame(self.root)
        controles.pack()
        for coluna in range(COLUNAS):
            botao = tk.Button(
                controles,
                text=f"▼ {coluna + 1}",
                width=5,
                command=lambda coluna=coluna: self.jogar(coluna),
            )
            botao.grid(row=0, column=coluna, padx=2, pady=4)
            self.botoes_coluna.append(botao)

        tabuleiro_frame = tk.Frame(
            self.root,
            bg="#2471A3",
            padx=8,
            pady=8,
        )
        tabuleiro_frame.pack(padx=12, pady=8)

        for linha in range(LINHAS):
            linha_celulas = []
            for coluna in range(COLUNAS):
                celula = tk.Label(
                    tabuleiro_frame,
                    bg=CORES[VAZIO],
                    width=4,
                    height=2,
                    relief="sunken",
                    bd=1,
                )
                celula.grid(row=linha, column=coluna, padx=3, pady=3)
                linha_celulas.append(celula)
            self.celulas.append(linha_celulas)

        tk.Button(
            self.root,
            text="Reiniciar Jogo",
            font=("Arial", 11, "bold"),
            command=self.reiniciar,
            padx=12,
            pady=5,
        ).pack(pady=(2, 14))

    def desenhar_tabuleiro(self):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                jogador = self.tabuleiro[linha][coluna]
                self.celulas[linha][coluna].configure(bg=CORES[jogador])

    def atualizar_status(self):
        nome = "Jogador 1 (vermelho)" if self.jogador_atual == JOGADOR_1 else (
            "Jogador 2 (amarelo)"
        )
        self.status.set(f"Vez do {nome}")

    def jogar(self, coluna):
        if self.jogo_encerrado:
            return

        linha = inserir_ficha(self.tabuleiro, coluna, self.jogador_atual)
        if linha is None:
            messagebox.showwarning("Coluna cheia", "Escolha outra coluna.")
            return

        self.desenhar_tabuleiro()
        if verificar_vitoria(self.tabuleiro, self.jogador_atual):
            nome = f"Jogador {self.jogador_atual}"
            self.status.set(f"{nome} venceu!")
            self.jogo_encerrado = True
            self.desativar_colunas()
        elif tabuleiro_cheio(self.tabuleiro):
            self.status.set("Empate! O tabuleiro está cheio.")
            self.jogo_encerrado = True
            self.desativar_colunas()
        else:
            self.jogador_atual = (
                JOGADOR_2 if self.jogador_atual == JOGADOR_1 else JOGADOR_1
            )
            self.atualizar_status()

    def desativar_colunas(self):
        for botao in self.botoes_coluna:
            botao.configure(state=tk.DISABLED)

    def reiniciar(self):
        self.tabuleiro = criar_tabuleiro()
        self.jogador_atual = JOGADOR_1
        self.jogo_encerrado = False
        for botao in self.botoes_coluna:
            botao.configure(state=tk.NORMAL)
        self.desenhar_tabuleiro()
        self.atualizar_status()


def main():
    root = tk.Tk()
    ConnectFour(root)
    root.mainloop()


if __name__ == "__main__":
    main()
