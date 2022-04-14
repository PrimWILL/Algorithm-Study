sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]

def find(i, j):
    visited = [0] * 10

    for k in range(9):
        visited[sudoku[i][k]] = 1
        visited[sudoku[k][j]] = 1

    r = i//3 * 3
    c = j//3 * 3

    for x in range(r, r + 3):
        for y in range(c, c + 3):
            visited[sudoku[x][y]] = 1
    
    temp = [i for i in range(1, 10) if not visited[i]]
    return temp

cp = False
def dfs(index):
    global cp
    if cp:
        return

    if index == len(zeros):
        for i in range(9):
            print(' '.join(list(map(str, sudoku[i]))))
        cp = True
        return
    else:
        i, j = zeros[index]
        for k in find(i, j):
            sudoku[i][j] = k
            dfs(index + 1)
            sudoku[i][j] = 0

dfs(0)