def compare_abc(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    a, b, c = compare_abc(a, b, c)
    if a ** 2 == b ** 2 + c ** 2:
        print("right")
    else:
        print("wrong")