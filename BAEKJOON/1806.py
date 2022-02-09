import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

i = 0
j = 1

min_num = 100001
cnt = 1
sum_num = num[0]

while True:
    if sum_num >= S:
        min_num = min(min_num, j - i)
        sum_num -= num[i]
        i += 1
    else:
        if j == N:
            break
        sum_num += num[j]
        j += 1

if min_num == 100001:
    print(0)
else:
    print(min_num)