import sys

N = int(sys.stdin.readline())
color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def sol(x, y, N):
    cur = color_paper[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color_paper[i][j] != cur:
                sol(x, y, N // 2)
                sol(x + N // 2, y, N // 2)
                sol(x, y + N // 2, N // 2)
                sol(x + N // 2, y + N // 2, N // 2)
                return
    
    if cur == 0:
        global white
        white += 1
    else:
        global blue
        blue += 1

sol(0, 0, N)
print(white)
print(blue)
