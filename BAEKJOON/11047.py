import sys

N, K = map(int, sys.stdin.readline().split())
coin = list()

for _ in range(N):
    coin.append(int(sys.stdin.readline()))

coin.reverse()
cnt = 0

for x in coin:
    cnt += K // x
    K %= x

print(cnt)