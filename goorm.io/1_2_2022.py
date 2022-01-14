# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def is_secret(n):
	if n == 0 or n == 1:
		return 'Yes'
	if n % 2 == 1:
		return 'No'
	return is_secret(n // 2)

n = int(input())
print(is_secret(n))

