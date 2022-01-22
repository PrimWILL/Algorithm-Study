import sys
import copy

ship = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
check = [False] * (11)
ans = 0
formation = [0 for _ in range(11)] 
seq = [0 for _ in range(11)]
cnt = 0

def set_ship(i, s):
	global ans
	global formation
	global cnt
	
	cnt += 1
	if i == 11:
		if ans < s:
			ans = s
			formation = copy.deepcopy(seq)
		return
	
	for x in range(11):
		if check[x]:
			continue
		check[x] = True
		seq[i] = x + 1
		set_ship(i + 1, s + ship[i][x])
		check[x] = False
		seq[i] = 0

set_ship(0, 0)
print(ans)
print(formation)
