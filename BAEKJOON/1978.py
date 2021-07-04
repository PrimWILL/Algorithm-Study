import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
for x in num:
    if x == 1:
        # 1 is not a prime
        continue
    elif x == 2:
        # 2 is prime
        cnt += 1
        continue
    elif x % 2 == 0:
        # all even integers except 2 are not prime
        continue

    prime = True
    for i in range(3, x // 2, 2):
        if x % i == 0:
            prime = False
            break
    
    if prime:
        cnt += 1

print(cnt)