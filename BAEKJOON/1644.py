N = int(input())

prime = list()

def find_prime(N):
    num = [True] * (N + 1)
    num[0] = False
    num[1] = False

    for i in range(2, N + 1):
        if not num[i]:
            continue
        j = i * 2
        while j <= N:
            num[j] = False
            j += i
    
    for x in range(2, N + 1):
        if num[x]:
            prime.append(x)

find_prime(N)

answer = 0
i, j = 0, 1

if prime:
    s = prime[i]

    while True:
        if s >= N:
            if s == N:
                answer += 1
            s -= prime[i]
            i += 1
        else:
            if j == len(prime):
                break
            s += prime[j]
            j += 1

print(answer)