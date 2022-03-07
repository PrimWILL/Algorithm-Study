import math

N = int(input())
nums = list()

for _ in range(N):
    nums.append(int(input()))

nums.sort()
new_nums = [nums[i + 1] - nums[i] for i in range(N - 1)]

def FindGCD(a, b):
    if b == 0:
        return a
    return FindGCD(b, a % b)

gcd = new_nums[0]
for i in range(1, N - 1):
    gcd = FindGCD(gcd, new_nums[i])

result = list()
for i in range(2, math.ceil(gcd ** 0.5) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)

result.append(gcd)
print(" ".join(map(str,sorted(list(set(result))))))