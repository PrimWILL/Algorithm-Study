N = int(input())

paper = list()
for _ in range(N):
  line = list(map(int, input().split()))
  paper.append(line)

results = [0, 0, 0]

def sol(x, y, N):
    cur = paper[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if cur != paper[i][j]:
                sol(x, y, N // 3)
                sol(x, y + N // 3, N // 3)
                sol(x, y + (N // 3) * 2, N // 3)
                sol(x + N // 3, y, N // 3)
                sol(x + N // 3, y + N // 3, N // 3)
                sol(x + N // 3, y + (N // 3) * 2, N // 3)
                sol(x + (N // 3) * 2, y, N // 3)
                sol(x + (N // 3) * 2, y + N // 3, N // 3)
                sol(x + (N // 3) * 2, y + (N // 3) * 2, N // 3)
                return
    
    if cur == -1:
        results[0] += 1
    elif cur == 0:
        results[1] += 1
    else:
        results[2] += 1
    return

sol(0, 0, N)

print(results[0])
print(results[1])
print(results[2])