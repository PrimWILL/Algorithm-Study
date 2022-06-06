from collections import defaultdict
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_dict = defaultdict()
pokemon_list = [0]

for i in range(1, N + 1):
    temp = input().strip()
    pokemon_dict[temp] = i
    pokemon_list.append(temp)

for _ in range(M):
    temp = input().strip()
    if temp.isdigit():
        print(pokemon_list[int(temp)])
    else:
        print(pokemon_dict[temp])