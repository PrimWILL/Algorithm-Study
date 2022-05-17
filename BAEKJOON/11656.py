import sys

input = sys.stdin.readline

S = input().strip()
temp = [S[x:] for x in range(len(S))]

temp.sort()

for x in temp:
    print(x)