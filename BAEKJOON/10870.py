import sys

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n-2)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(fibo(n))
