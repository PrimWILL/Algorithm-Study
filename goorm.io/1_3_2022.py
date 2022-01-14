# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num = 0

def solve(cur, sum_num):
	global num
	if cur == N - 1:
		if sum_num == S:
			num += 1
		return
	solve(cur + 1, sum_num)
	solve(cur + 1, sum_num + ability[cur])

N, S = map(int, input().split())

ability = list(map(int, input().split()))
h = ability.pop(0)

solve(0, h)
print(num)