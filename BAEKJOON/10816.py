import sys

N = int(sys.stdin.readline())

cards = dict()
temp = list(map(int, sys.stdin.readline().split()))

for i in temp:
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

M = int(sys.stdin.readline())
cards_list = list(map(int, sys.stdin.readline().split()))

for i in cards_list:
    if i in cards:
        print(cards[i], end = ' ')
    else:
        print(0, end=' ')