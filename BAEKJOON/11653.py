import sys

N = int(sys.stdin.readline())

end = False
while True:
    if N == 1:
        break
    if end:
        break
    for x in range(2, N + 1):
        if (N % x == 0):
            print(x)
            N = int(N / x)
            break
        if (x == N):
            end = True