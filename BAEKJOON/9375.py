import sys

n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())

  clothes = dict()
  for _ in range(num):
    name, kind = map(str, sys.stdin.readline().split())

    if kind in clothes:
      clothes[kind] += 1
    else:
      clothes[kind] = 1
    
  kinds = list(clothes.values())
  cnt = 1
  for x in kinds:
    cnt *= (x + 1)

  print(cnt - 1)

    