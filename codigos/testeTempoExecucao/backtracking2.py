import csv
import time

# Verifica se o num pode ser colocado na posição 
def verifica(tabuleiro, linha, coluna, num, linSet, colSet, subgradesSet):
    if num in linSet[linha] or num in colSet[coluna] or num in subgradesSet[(linha // 3, coluna // 3)]:
        return False
    return True

# Função para resolver o Sudoku com o método de backtracking
def resSudoku(tabuleiro, linSet, colSet, subgradesSet):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if verifica(tabuleiro, linha, coluna, num, linSet, colSet, subgradesSet):
                        tabuleiro[linha][coluna] = num
                        linSet[linha].add(num)
                        colSet[coluna].add(num)
                        subgradesSet[(linha // 3, coluna // 3)].add(num)

                        if resSudoku(tabuleiro, linSet, colSet, subgradesSet):
                            return True

                        tabuleiro[linha][coluna] = 0
                        linSet[linha].remove(num)
                        colSet[coluna].remove(num)
                        subgradesSet[(linha // 3, coluna // 3)].remove(num)
                return False
    return True

# Função para mostrar o tabuleiro
def mostrarTab(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) for num in linha))

# Carregar o .csv, resolver o Sudoku e medir o tempo de execução
def main():
    totalJogos = 0
    tempoTotal = 0.0

    #with open(r"C:/Users/melis/Documents/GitHub/sudoku/db/sudoku.csv", newline='') as arquivoCsv:
    with open(r"C:/Users/melis/Documents/GitHub/sudoku/db/sudoku100.csv", newline='') as arquivoCsv:
        leitor = csv.reader(arquivoCsv)
        for linha in leitor:
            desafio = linha[0]
            solucaoCorreta = linha[1]

            tabuleiro = [[int(desafio[i * 9 + j]) for j in range(9)] for i in range(9)]

            linSet = [set() for _ in range(9)]
            colSet = [set() for _ in range(9)]
            subgradesSet = {(i, j): set() for i in range(3) for j in range(3)}

            for linha in range(9):
                for coluna in range(9):
                    num = tabuleiro[linha][coluna]
                    if num != 0:
                        linSet[linha].add(num)
                        colSet[coluna].add(num)
                        subgradesSet[(linha // 3, coluna // 3)].add(num)

            print("Tabuleiro inicial:")
            mostrarTab(tabuleiro)

            inicioTempo = time.perf_counter()
            if resSudoku(tabuleiro, linSet, colSet, subgradesSet):
                fimTempo = time.perf_counter()
                tempoExecucao = fimTempo - inicioTempo
                tempoTotal += tempoExecucao
                totalJogos += 1

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
    
    if totalJogos > 0:
        mediaTempo = tempoTotal / totalJogos
        print(f"Total de jogos resolvidos: {totalJogos}")
        print(f"Média de tempo por solução: {mediaTempo:.9f} segundos")
    else:
        print("Nenhum jogo foi resolvido.")

if __name__ == "__main__":
    main()