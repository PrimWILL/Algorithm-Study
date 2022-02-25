N = int(input())

sequence = [0] + list(map(int, input().split()))
LCS_up = [0] * (N + 1)
LCS_down = [0] * (N + 1)

for x in range(1, N + 1):
    up = 0
    for i in range(0, x):
        if sequence[i] < sequence[x] and LCS_up[up] < LCS_up[i]:
            up = i
    LCS_up[x] = LCS_up[up] + 1

    down = 0
    updown = 0
    for i in range(0, x):
        if sequence[i] > sequence[x] and LCS_down[down] < LCS_down[i]:
            down = i
        if sequence[i] > sequence[x] and LCS_up[updown] < LCS_up[i]:
            updown = i

    LCS_down[x] = max(LCS_down[down], LCS_up[updown]) + 1

print(max(max(LCS_down), max(LCS_up)))