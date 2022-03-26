import sys

input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

def power(a, b):
    if b == 1:
        return a % p
    
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p

fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = (fact[K] * fact[N - K]) % p

result = (A % p) * (power(B, p - 2) % p) % p
print(result)