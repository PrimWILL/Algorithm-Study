# Solve using Counter 
import sys
from collections import Counter

N = int(sys.stdin.readline())

temp = list(map(int, sys.stdin.readline().split()))
counter = Counter(temp)

M = int(sys.stdin.readline())
cards_list = list(map(int, sys.stdin.readline().split()))

for i in cards_list:
    print(counter[i], end = ' ')