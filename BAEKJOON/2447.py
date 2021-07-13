import sys 

def star(i, j, n):
    if (((i // n) % 3 == 1) and ((j // n) % 3 == 1)):
        print(' ', end = '')
    else:
        if (n // 3 == 0):
            print('*', end = '')
        else:
            star(i, j, n // 3)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range (0, n):
        for j in range (0, n):
            star(i, j, n)
        print('\n')

# 이거 c++에서는 시간 초과 안 나는데 파이썬은 시간 초과남 !!