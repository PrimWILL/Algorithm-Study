import sys

T = int(sys.stdin.readline())

zero = [-1] * 41
one = [-1] * 41
zero[0] = 1; zero[1] = 0; zero[2] = 1
one[0] = 0; one[1] = 1; one[2] = 1

for i in range(2, 41):
    zero[i] = zero[i - 1] + zero[i - 2]
    one[i] = one[i - 1] + one[i - 2]

for _ in range(T):
    N = int(sys.stdin.readline())

    print(f'{zero[N]} {one[N]}')