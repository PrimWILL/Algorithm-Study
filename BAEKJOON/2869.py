import sys

B, A, V = map(int, sys.stdin.readline().split())
V -= B
result = V // (B - A)
if V == 0:
    print(1)
elif V % (B - A) > 0:
    print(result + 2)
else:
    print(result + 1)