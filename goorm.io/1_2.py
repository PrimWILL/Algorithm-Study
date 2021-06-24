a = int(input())

ans = 0
while True:
	if a == 1 or a == 0:
		break
	elif a % 2 == 1:
		ans = 1
		break
	else:
		a /= 2

if ans == 0:
	print('Yes')
else:
	print('No')