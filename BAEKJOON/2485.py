def find_gcd(a, b):
  while b != 0:
    n = a % b
    a = b
    b = n
  return a

N = int(input())
tree = list()

for _ in range(N):
  tree.append(int(input()))

diff = list()
for i in range(1, N):
  diff.append(tree[i] - tree[i - 1])

gcd = diff[0]
for x in diff:
  gcd = find_gcd(gcd, x)
  if gcd == 1:
    break

cnt = 0
for x in diff:
  cnt += (x // gcd - 1)

print(cnt)