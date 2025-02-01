import csv
import time

# Verifica se um número pode ser colocado na posição 
def verifica(tabuleiro, linha, coluna, num):

    # Verifica a linha
    if num in tabuleiro[linha]:
        return False
    
    # Verifica a coluna
    if num in [tabuleiro[i][coluna] for i in range(9)]:
        return False
    
    # Verifica a subgrade 3x3
    inicioLin, inicioCol = 3 * (linha // 3), 3 * (coluna // 3)
    for i in range(inicioLin, inicioLin + 3):
        for j in range(inicioCol, inicioCol + 3):
            if tabuleiro[i][j] == num:
                return False

    return True

# Valida o tabuleiro completo (no final)
def validaTabuleiro(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if len(set(linha)) != 9 or any(num == 0 for num in linha):
            return False

    # Verifica colunas
    for coluna in range(9):
        if len(set(tabuleiro[linha][coluna] for linha in range(9))) != 9:
            return False

    # Verifica subgrades 3x3
    for inicioLin in range(0, 9, 3):
        for inicioCol in range(0, 9, 3):
            subgrade = [
                tabuleiro[i][j]
                for i in range(inicioLin, inicioLin + 3)
                for j in range(inicioCol, inicioCol + 3)
            ]
            if len(set(subgrade)) != 9:
                return False

    return True

# Resolve o Sudoku com força bruta (otimizada)
def fbResSudoku(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                # Tenta todos os números de 1 a 9
                for num in range(1, 10):
                    if verifica(tabuleiro, linha, coluna, num): 
                        tabuleiro[linha][coluna] = num

                        # Continua a resolver recursivamente
                        if fbResSudoku(tabuleiro):
                            return True

                        # Volta para 0 se a solução falhar
                        tabuleiro[linha][coluna] = 0

                return False  # Caso nenhum num funcione p/ a posição

    # Verifica se o tabuleiro completo é válido
    return validaTabuleiro(tabuleiro)

# Função p/ printar o tabuleiro
def mostrarTab(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) for num in linha))

# Carregar o arquivo, resolve o Sudoku e mede o tempo de execução
def main():
    with open(r"C:/Users/melis/Documents/GitHub/sudoku/db/sudoku100.csv", newline='') as arquivoCsv:
        leitor = csv.reader(arquivoCsv)
        for linha in leitor:
            desafio = linha[0]  # Tabuleiro inicial
            solucaoCorreta = linha[1]  # Solução correta

            # Convertendo desafio para mat[9x9]
            tabuleiro = [[int(desafio[i * 9 + j]) for j in range(9)] for i in range(9)]

            print("Tabuleiro inicial:")
            mostrarTab(tabuleiro)

            # Mede tempo de execução
            inicioTempo = time.perf_counter()
            if fbResSudoku(tabuleiro):
                fimTempo = time.perf_counter()
                tempoExecucao = fimTempo - inicioTempo

                print("\nSolução encontrada:")
                mostrarTab(tabuleiro)

                print(f"\nTempo de execução: {tempoExecucao:.9f} segundos")

                # Verificando se a solução tá correta
                tabuleiroResolvido = "".join(str(num) for linha in tabuleiro for num in linha)
                if tabuleiroResolvido == solucaoCorreta:
                    print("A solução está correta!\n")
                else:
                    print("A solução está incorreta!\n")
            else:
                print("Não foi possível resolver o Sudoku.\n")

if __name__ == "__main__":
    main()