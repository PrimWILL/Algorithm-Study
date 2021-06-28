import math

M = int(input())
N = int(input())

num = [x for x in range(M, N + 1) if (x % 2 != 0) and (x > 2)]
if (M <= 2 and N >= 2):
    num.append(2)

prime = list()

for x in range (0, len(num)):
    cp = False

    for i in range (3, math.floor(num[x] / 2), 2):
        if num[x] % i == 0:
            cp = True
            break
    if cp:
        pass
    else:
        prime.append(num[x])

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))