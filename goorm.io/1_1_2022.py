# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

team = list(map(int, sys.stdin.readline().split()))
select = list(map(int, sys.stdin.readline().split()))

num = len(select)

for x in team:
	if x in select:
		num -= 1

print(num)