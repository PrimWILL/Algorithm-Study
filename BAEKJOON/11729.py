import sys


def hanoi(h_from, temp, to, n):
    if n == 1:
        print(f'{h_from} {to}')
    else:
        hanoi(h_from, to, temp, n-1)
        print(f'{h_from} {to}')
        hanoi(temp, h_from, to, n-1)


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    print(2 ** n - 1)
    hanoi(1, 2, 3, n)