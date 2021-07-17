import sys

cnt = int(sys.stdin.readline())

divisor = list(map(int, sys.stdin.readline().split()))
divisor.sort()

print(divisor[0] * divisor[-1])