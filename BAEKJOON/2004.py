import sys

def count_num_of_2(number):
    cnt = 0
    while (number != 0):
        number //= 2
        cnt += number
    return cnt

def count_num_of_5(number):
    cnt = 0
    while (number != 0):
        number //= 5
        cnt += number
    return cnt


n, m = map(int, sys.stdin.readline().split())

num_two = count_num_of_2(n) - count_num_of_2(m) - count_num_of_2(n - m)
num_five = count_num_of_5(n) - count_num_of_5(m) - count_num_of_5(n - m)

print(min(num_five, num_two))
