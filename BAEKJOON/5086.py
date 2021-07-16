import sys

relation = list()

a, b = map(int, sys.stdin.readline().split())
relation.append([a, b])

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    relation.append([a, b])

for a, b in relation:
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
    