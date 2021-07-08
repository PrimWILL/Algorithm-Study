import sys

point = list()

for x in range (3):
    a, b = map(int, sys.stdin.readline().split())
    point.append((a, b))

x_point = {}
y_point = {}

x_point[point[0][0]] = 1
y_point[point[0][1]] = 1

for i in range (1, 3):
    x = point[i][0]
    y = point[i][1]

    if x in x_point:
        x_point[x] += 1
    else:
        x_point[x] = 1
    
    if y in y_point:
        y_point[y] += 1
    else:
        y_point[y] = 1

x = [key for key, value in x_point.items() if value == 1]
y = [key for key, value in y_point.items() if value == 1]

print("{} {}".format(x[0], y[0]))
