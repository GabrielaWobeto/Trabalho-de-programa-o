class SudokuBoard:
    def __init__(self):
        self.board = self.criar_tabuleiro_inicial()
        self.posicoes_fixas = {
            (i, j)
            for i in range(9)
            for j in range(9)
            if self.board[i][j] != 0
        }

    def criar_tabuleiro_inicial(self):
        return [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    def movimento_valido(self, linha, col, num):
        # Checa linha
        if num in self.board[linha]:
            return False

        # Checa coluna
        for r in range(9):
            if self.board[r][col] == num:
                return False

        # Checa subgrade 3x3
        sr, sc = 3 * (linha // 3), 3 * (col // 3)
        for r in range(sr, sr + 3):
            for c in range(sc, sc + 3):
                if self.board[r][c] == num:
                    return False

        return True

    def inserir(self, linha, col, num):
        """Insere um número no tabuleiro se permitido."""
        if (linha, col) in self.posicoes_fixas:
            return False, "Não é permitido alterar esta posição fixa."

        if not self.movimento_valido(linha, col, num):
            return False, "Jogada inválida! Número repetido."

        self.board[linha][col] = num
        return True, "Valor inserido com sucesso."

    def apagar(self, linha, col):
        if (linha, col) in self.posicoes_fixas:
            return False, "Não é permitido apagar uma posição fixa."

        self.board[linha][col] = 0
        return True, "Posição apagada."

    def tabuleiro_cheio(self):
        return all(0 not in linha for linha in self.board)

    def vitoria(self):
        alvo = set(range(1, 10))

        # Checa linhas e colunas
        for i in range(9):
            if set(self.board[i]) != alvo:
                return False
            if set(self.board[r][i] for r in range(9)) != alvo:
                return False

        # Checa 3x3
        for sr in range(0, 9, 3):
            for sc in range(0, 9, 3):
                bloco = [
                    self.board[r][c]
                    for r in range(sr, sr + 3)
                    for c in range(sc, sc + 3)
                ]
                if set(bloco) != alvo:
                    return False

        return True


class SudokuView:
    @staticmethod
    def mostrar(board):
        print("     " + "   ".join(str(i) for i in range(1, 10)))
        print("   +" + "---+" * 9)
        for i, linha in enumerate(board):
            print(f" {i+1} |", end="")
            for val in linha:
                cell = str(val) if val != 0 else " "
                print(f" {cell} |", end="")
            print()
            print("   +" + "---+" * 9)


class SudokuGame:
    def __init__(self):
        self.sudoku = SudokuBoard()
        self.view = SudokuView()

    def jogar(self):
        print("\nBem-vindo ao Sudoku (versão POO)!\n")

        while True:
            self.view.mostrar(self.sudoku.board)

            if self.sudoku.tabuleiro_cheio():
                if self.sudoku.vitoria():
                    print("\n🎉 Parabéns! Sudoku completo corretamente!")
                    break
                else:
                    print("\nO tabuleiro está cheio, mas existem erros.")

            comando = input(
                "Digite 'L C N', 'apagar L C' ou 'sair': "
            ).strip()

            if comando.lower() == "sair":
                print("Jogo encerrado.")
                break

            if comando.lower().startswith("apagar"):
                try:
                    _, l, c = comando.split()
                    linha = int(l) - 1
                    col = int(c) - 1
                    ok, msg = self.sudoku.apagar(linha, col)
                    print(msg)
                except:
                    print("Comando inválido.")
                continue

            try:
                l, c, n = map(int, comando.split())
                linha, col, num = l - 1, c - 1, n
                ok, msg = self.sudoku.inserir(linha, col, num)
                print(msg)
            except:
                print("Entrada inválida.")


if __name__ == "__main__":
    jogo = SudokuGame()
    jogo.jogar()
