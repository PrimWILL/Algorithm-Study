import sys
import math

t = int(sys.stdin.readline())
bridge = []

for x in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
    bridge.append(int(result))

for x in bridge:
    print(x)
