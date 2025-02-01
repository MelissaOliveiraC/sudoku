import csv
import time

# Verifica se o num pode ser colocado na posição 
def verifica(tabuleiro, linha, coluna, num, linSet, colSet, subgradesSet):
    # Verifica se o número já está na linha, coluna ou subgrade (otimização)
    if num in linSet[linha] or num in colSet[coluna] or num in subgradesSet[(linha // 3, coluna // 3)]:
        return False
    return True

# Função para resolver o Sudoku com o método de backtracking
def resSudoku(tabuleiro, linSet, colSet, subgradesSet):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                # Tenta todos os números de 1 a 9
                for num in range(1, 10):
                    if verifica(tabuleiro, linha, coluna, num, linSet, colSet, subgradesSet):
                        # Add o número no tabuleiro
                        tabuleiro[linha][coluna] = num
                        # Atualiza os conjuntos de linhas, colunas e subgrades (evita outras verificações)
                        linSet[linha].add(num)
                        colSet[coluna].add(num)
                        subgradesSet[(linha // 3, coluna // 3)].add(num)

                        # Continua a resolver recursivamente
                        if resSudoku(tabuleiro, linSet, colSet, subgradesSet):
                            return True

                        # Se não for possível, desfaz a mudança
                        tabuleiro[linha][coluna] = 0
                        linSet[linha].remove(num)
                        colSet[coluna].remove(num)
                        subgradesSet[(linha // 3, coluna // 3)].remove(num)

                return False   # Se nenhum num funcionar, volta e tenta de novo

    return True  # Caso o sudoku seja resolvido

# Função para mostrar o tabuleiro
def mostrarTab(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) for num in linha))

# Carregar o .csv, resolver o Sudoku e medir o tempo de execução
def main():
    # Lendo o arquivo CSV com os Sudokus
    with open(r"C:/Users/melis/Documents/GitHub/sudoku/db/sudoku100.csv", newline='') as arquivoCsv:
        leitor = csv.reader(arquivoCsv)
        for linha in leitor:
            desafio = linha[0]  # Tabuleiro inicial
            solucaoCorreta = linha[1]  # Solução correta

            # Convertendo o -desafio- p/ uma matriz 9x9
            tabuleiro = [[int(desafio[i * 9 + j]) for j in range(9)] for i in range(9)]

            # Inicializando os conjuntos para as linhas, colunas e subgrades
            linSet = [set() for _ in range(9)]
            colSet = [set() for _ in range(9)]
            subgradesSet = { (i, j): set() for i in range(3) for j in range(3) }

            # Preenche os conjuntos com os números já presentes no tabuleiro (inicialização)
            for linha in range(9):
                for coluna in range(9):
                    num = tabuleiro[linha][coluna]
                    if num != 0:
                        linSet[linha].add(num)
                        colSet[coluna].add(num)
                        subgradesSet[(linha // 3, coluna // 3)].add(num)

            print("Tabuleiro inicial:")
            mostrarTab(tabuleiro)

            # P/ medir o tempo de execução
            inicioTempo = time.perf_counter()
            if resSudoku(tabuleiro, linSet, colSet, subgradesSet):
                fimTempo = time.perf_counter()
                tempoExecucao = fimTempo - inicioTempo

                print("\nSolução encontrada:")
                mostrarTab(tabuleiro)
                print(f"\nTempo de execução: {tempoExecucao:.9f} segundos")

                # Faz verificação se a solução tá correta
                tabuleiroResolvido = "".join(str(num) for linha in tabuleiro for num in linha)
                if tabuleiroResolvido == solucaoCorreta:
                    print("A solução está correta!\n")
                else:
                    print("A solução está incorreta!\n")
            else:
                print("Não foi possível resolver o Sudoku.\n")

if __name__ == "__main__":
    main()