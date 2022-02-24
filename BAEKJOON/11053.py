N = int(input())

sequence = [0] + list(map(int, input().split()))
LCS = [0] * (N + 1)

for x in range(1, N + 1):
    tmp = 0
    for i in range(0, x):
        if sequence[i] < sequence[x] and LCS[tmp] < LCS[i]:
            tmp = i
    LCS[x] = LCS[tmp] + 1

print(max(LCS))