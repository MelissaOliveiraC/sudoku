import csv
import time

def verifica(tabuleiro, linha, coluna, num):
    if num in tabuleiro[linha]:
        return False
    if num in [tabuleiro[i][coluna] for i in range(9)]:
        return False
    inicioLin, inicioCol = 3 * (linha // 3), 3 * (coluna // 3)
    for i in range(inicioLin, inicioLin + 3):
        for j in range(inicioCol, inicioCol + 3):
            if tabuleiro[i][j] == num:
                return False
    return True

def validaTabuleiro(tabuleiro):
    for linha in tabuleiro:
        if len(set(linha)) != 9 or any(num == 0 for num in linha):
            return False
    for coluna in range(9):
        if len(set(tabuleiro[linha][coluna] for linha in range(9))) != 9:
            return False
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

def fbResSudoku(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if verifica(tabuleiro, linha, coluna, num): 
                        tabuleiro[linha][coluna] = num
                        if fbResSudoku(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return validaTabuleiro(tabuleiro)

def mostrarTab(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) for num in linha))

def main():
    jogosResolvidos = 0
    somaTempos = 0.0
    
    with open(r"C:/Users/melis/Documents/GitHub/sudoku/db/sudoku100.csv", newline='') as arquivoCsv:
        leitor = csv.reader(arquivoCsv)
        for linha in leitor:
            desafio = linha[0]
            solucaoCorreta = linha[1]
            tabuleiro = [[int(desafio[i * 9 + j]) for j in range(9)] for i in range(9)]
            print("Tabuleiro inicial:")
            mostrarTab(tabuleiro)
            inicioTempo = time.perf_counter()
            if fbResSudoku(tabuleiro):
                fimTempo = time.perf_counter()
                tempoExecucao = fimTempo - inicioTempo
                somaTempos += tempoExecucao
                jogosResolvidos += 1
                print("\nSolução encontrada:")
                mostrarTab(tabuleiro)
                print(f"\nTempo de execução: {tempoExecucao:.9f} segundos")
                tabuleiroResolvido = "".join(str(num) for linha in tabuleiro for num in linha)
                if tabuleiroResolvido == solucaoCorreta:
                    print("A solução está correta!\n")
                else:
                    print("A solução está incorreta!\n")
            else:
                print("Não foi possível resolver o Sudoku.\n")
    if jogosResolvidos > 0:
        mediaTempo = somaTempos / jogosResolvidos
        print(f"\nTotal de jogos resolvidos: {jogosResolvidos}")
        print(f"Média de tempo para resolver: {mediaTempo:.9f} segundos")
    else:
        print("\nNenhum jogo foi resolvido.")

if __name__ == "__main__":
    main()
