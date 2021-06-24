n = int(input())
position = []
for x in range(n):
	tempList = list(map(int, input().split()))
	position.append(tempList)	

def distance(x1, x2, y1, y2):
	return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);

maxDistance = 0
first = 0 
second = 0

for i in range(0, n):
	for j in range(i + 1, n):
		tempDistance = distance(position[i][0], position[j][0], position[i][1], position[j][1])
		if tempDistance > maxDistance:
			maxDistance = tempDistance
			first = i
			second = j

print("{0} {1}".format(first + 1, second + 1))