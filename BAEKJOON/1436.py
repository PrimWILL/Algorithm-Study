import sys

n = int(sys.stdin.readline())

cnt = 0
temp = 0
while True:
    temp += 1
    if "666" in str(temp):
        cnt += 1
        if cnt == n:
            print(temp)
            break