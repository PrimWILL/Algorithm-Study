import sys

N = sys.stdin.readline()

num_join = ":".join(N)
num_split = num_join.split(":")
num_split.sort(reverse=True)
for x in range(0, len(num_split) - 1):
    print(num_split[x], end='')