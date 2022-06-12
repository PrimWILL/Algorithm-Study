K = int(input())

farm = list()
adjacent = [False] * 6
long_h = 0; long_w = 0
long_index = [0, 0]

for i in range(6):
    a, b = map(int, input().split())
    farm.append(b)
    if a == 1 or a == 2:
        if b > long_w:
            long_w = b
            long_index[0] = i
    else:
        if b > long_h:
            long_h = b
            long_index[1] = i

for i in long_index:
    adjacent[i] = True
    adjacent[i - 1] = True
    adjacent[(i + 1) % 6] = True

small_area = 1
for i in range(6):
    if not adjacent[i]:
        small_area *= farm[i]

print((long_h * long_w - small_area) * K)