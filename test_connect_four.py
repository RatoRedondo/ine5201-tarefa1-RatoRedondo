import unittest

from connect_four import (
    JOGADOR_1,
    JOGADOR_2,
    criar_tabuleiro,
    inserir_ficha,
    tabuleiro_cheio,
    verificar_vitoria,
)


class ConnectFourTest(unittest.TestCase):
    def test_ficha_cai_para_a_linha_inferior(self):
        tabuleiro = criar_tabuleiro()

        linha = inserir_ficha(tabuleiro, 3, JOGADOR_1)

        self.assertEqual(linha, 5)
        self.assertEqual(tabuleiro[5][3], JOGADOR_1)

    def test_coluna_cheia_e_rejeitada(self):
        tabuleiro = criar_tabuleiro()
        for _ in range(6):
            inserir_ficha(tabuleiro, 0, JOGADOR_1)

        self.assertIsNone(inserir_ficha(tabuleiro, 0, JOGADOR_2))

    def test_detecta_vitoria_horizontal_vertical_e_diagonal(self):
        horizontal = criar_tabuleiro()
        for coluna in range(4):
            inserir_ficha(horizontal, coluna, JOGADOR_1)
        self.assertTrue(verificar_vitoria(horizontal, JOGADOR_1))

        vertical = criar_tabuleiro()
        for _ in range(4):
            inserir_ficha(vertical, 0, JOGADOR_2)
        self.assertTrue(verificar_vitoria(vertical, JOGADOR_2))

        diagonal = criar_tabuleiro()
        jogadas = (0, 1, 1, 2, 2, 2, 3, 3, 3, 3)
        for coluna in jogadas:
            inserir_ficha(diagonal, coluna, JOGADOR_1)
        self.assertTrue(verificar_vitoria(diagonal, JOGADOR_1))

    def test_detecta_tabuleiro_cheio(self):
        tabuleiro = [[JOGADOR_1 for _ in range(7)] for _ in range(6)]

        self.assertTrue(tabuleiro_cheio(tabuleiro))


if __name__ == "__main__":
    unittest.main()
