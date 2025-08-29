def mostrar_tabuleiro(board):
    # Cabeçalho das colunas
    print("     " + "   ".join(str(i) for i in range(1, 10)))#imprime os números em cima das colunas
    print("   +" + "---+" * 9)
    for i, linha in enumerate(board):
        print(f" {i+1} |", end="")#imprime os números na lateral das linhas
        for val in linha:
            cell = str(val) if val != 0 else " "
            print(f" {cell} |", end="")
        print()
        print("   +" + "---+" * 9)#linha de baixo


def movimento_valido(board, linha, col, num):
    # Checa linha
    if num in board[linha]:
        return False
    # Checa coluna
    for r in range(9):
        if board[r][col] == num:
            return False
    # Checa subgrade 3x3
    sr, sc = 3 * (linha // 3), 3 * (col // 3)
    for r in range(sr, sr + 3):
        for c in range(sc, sc + 3):
            if board[r][c] == num:
                return False
    return True


def tabuleiro_cheio(board):
    return all(0 not in linha for linha in board)


def vitoria(board):
    # Garante que cada linha, coluna e 3x3 contém exatamente {1..9}
    alvo = set(range(1, 10))
    for i in range(9):
        if set(board[i]) != alvo:
            return False
        if set(board[r][i] for r in range(9)) != alvo:
            return False
    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            bloco = [board[r][c] for r in range(sr, sr + 3) for c in range(sc, sc + 3)]
            if set(bloco) != alvo:
                return False
    return True


def criar_tabuleiro():
    # Tabuleiro inicial
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


def principal():
    board = criar_tabuleiro() # Posições fixas
    posicoes_fixas = {(i, j) for i in range(9) for j in range(9) if board[i][j] != 0}

    print("\nBem-vindo ao Sudoku!\n")
    while True:
        mostrar_tabuleiro(board)

        if tabuleiro_cheio(board):
            if vitoria(board):
                print("\nParabéns! Você completou o Sudoku corretamente!")
                break
            else:
                print("\nO tabuleiro está cheio, mas há erros. Continue tentando!")

        valor = input(
            "Digite 'linha coluna valor' (ex: 2 4 7), "
            "'apagar L C' para limpar uma célula, ou 'sair' para sair: "
        ).strip()

        if not valor:
            continue
        if valor.lower() == "sair":
            print("Jogo encerrado.")
            break

        try:
            # Comando para apagar uma célula que não é fixa
            if valor.lower().startswith("apagar"):
                _, r_str, c_str = valor.split()
                linha, col = int(r_str) - 1, int(c_str) - 1
                if not (0 <= linha < 9 and 0 <= col < 9):
                    print("Coordenadas fora do intervalo 1-9.")
                    continue
                if (linha, col) in posicoes_fixas:
                    print("Não é permitido alterar esta posição fixa.")
                    continue
                board[linha][col] = 0
                continue

            # Jogada 
            r, c, n = map(int, valor.split())
            if not (1 <= r <= 9 and 1 <= c <= 9 and 1 <= n <= 9):
                print("Valores devem estar entre 1 e 9.")
                continue
            linha, col, num = r - 1, c - 1, n

            if (linha, col) in posicoes_fixas:
                print("Não é permitido alterar esta posição fixa.")
                continue

            if movimento_valido(board, linha, col, num):
                board[linha][col] = num
            else:
                print("Jogada inválida! Não é permitido repetir números na linha, coluna ou subgrade 3x3.")

        except ValueError:
            print("Entrada inválida. Use: 'Linha Coluna Valor' (ex: 2 4 7), 'apagar Linha Coluna' ou 'sair' para sair.")


if __name__ == "__principal__":
    principal()