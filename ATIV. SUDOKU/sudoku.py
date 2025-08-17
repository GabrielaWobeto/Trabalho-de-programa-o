import random

def tabuleiro(tabuleiro):
    # Cabeçalho das colunas alinhadas
    print("     " + "   ".join(str(i+1) for i in range(9)))
    print("   +" + "---+" * 9)
    
    for i, row in enumerate(tabuleiro):
        print(f" {i+1} |", end="")  # Número da linha
        for val in row:
            cell = str(val) if val != 0 else " "
            print(f" {cell} |", end="")
        print()
        print("   +" + "---+" * 9) # Linha divisória entre as linhas do tabuleiro


def movimento_valido(tabuleiro, row, col, num):
    # Checa linha
    if num in tabuleiro[row]:
        return False
    # Checa coluna
    for r in range(9):
        if tabuleiro[r][col] == num:
            return False
    # Checa subgrade 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if tabuleiro[r][c] == num:
                return False
    return True

def tabuleiro_cheio(tabuleiro):
    for row in tabuleiro:
        if 0 in row:
            return False
    return True

def vitoria(tabuleiro):
    # All cells full and all rows, columns, subgrids valid
    for i in range(9):
        linhas = [tabuleiro[i][j] for j in range(9)]
        colunas = [tabuleiro[j][i] for j in range(9)]
        if len(set(linhas)) != 9 or len(set(colunas)) != 9:
            return False
    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            vals = []
            for r in range(sr, sr+3):
                for c in range(sc, sc+3):
                    vals.append(tabuleiro[r][c])
            if len(set(vals)) != 9:
                return False
    return True

def tabuleiro():
    # Um tabuleiro inicial simples
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

def main():
    tabuleiro = tabuleiro()
    posicoes_fixas = [
        (i, j)
        for i in range(9)
        for j in range(9)
        if tabuleiro[i][j] != 0
    ]
    print("\nBem-vindo ao Sudoku!\n")
    while True:
        tabuleiro(tabuleiro)
        if tabuleiro_cheio(tabuleiro):
            if vitoria(tabuleiro):
                print("\nParabéns! Você completou o Sudoku corretamente!")
                break
            else:
                print("\nO tabuleiro está cheio, mas há erros. Continue tentando!")
        try:
            valor = input("Digite linha coluna valor (ex: 2 4 7) ou 'sair': ").strip()
            if valor.lower() == "sair":
                print("Jogo encerrado.")
                break
            row, col, num = map(int, valor.split())
            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("Valores devem estar entre 1 e 9.")
                continue
            row -= 1
            col -= 1
            if (row, col) in posicoes_fixas:
                print("Não é permitido alterar esta posição.")
                continue
            if movimento_valido(tabuleiro, row, col, num):
                tabuleiro[row][col] = num
            else:
                print("Jogada inválida! Não é permitido repetir números na linha, coluna ou subgrade 3x3.")
        except ValueError:
            print("Entrada inválida. Digite três números separados por espaço ou 'sair'.")

if __name__ == "__main__":
    main()