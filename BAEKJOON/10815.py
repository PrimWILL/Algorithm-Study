import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_card = list(map(int, sys.stdin.readline().split()))

cards.sort()

for x in find_card:
    if binary_search(cards, x, 0, N - 1) is not None:
        print("1", end = ' ')
    else:
        print("0", end = ' ')

