import sys

X = int(sys.stdin.readline())

line = 1

while X:
    if (X - line <= 0):
        if line % 2 == 1:
            print(str(line + 1 - X) + '/' + str(X))
            break
        else:
            print(str(X) + '/' + str(line + 1 - X))
            break
    else:
        X -= line
        line += 1
