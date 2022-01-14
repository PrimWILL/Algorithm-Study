# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())

pos = list()
for x in range(N):
	pos.append(list(map(int, input().split())))
	
num1 = 0
num2 = 0
dist = 0
	
for i in range(N - 2):
	j = i + 1
	x1, y1 = pos[i][0], pos[i][1]
	while j < N:
		x2, y2 = pos[j][0], pos[j][1]
		temp = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
		if temp > dist:
			num1 = i
			num2 = j
			dist = temp
		j += 1

print(f'{num1+1} {num2+1}')
	