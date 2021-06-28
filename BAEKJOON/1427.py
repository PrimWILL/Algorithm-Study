import sys

N = sys.stdin.readline()

num_split = list(N)
num_split.sort(reverse=True)
for x in range(0, len(num_split) - 1):
    print(num_split[x], end='')