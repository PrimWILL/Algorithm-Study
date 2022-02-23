def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
ring = list(map(int, input().split()))

first = ring[0]

for i in range(N - 1):
    second = ring[i + 1]
    num = gcd(first, second)
    print(f'{first // num}/{second // num}')
