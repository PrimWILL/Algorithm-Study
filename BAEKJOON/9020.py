import sys

prime = [True] * 10001

def find_prime():
    for i in range(2, 10001):
        if not prime[i]:
            continue
        else:
            for j in range(i * 2, 10001, i):
                prime[j] = False

find_prime()

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    ans = list()

    i, j = 2, n
    while not prime[j]:
        j -= 1
    
    while i <= j:
        s = i + j
        
        if s == n:
            ans.append((i, j))

            j -= 1
            while not prime[j]:
                j -= 1

            i += 1
            while not prime[i]:
                i += 1

        elif s > n:
            j -= 1
            while not prime[j]:
                j -= 1
        else:
            i += 1
            while not prime[i]:
                i += 1

    print(ans[-1][0], ans[-1][1])