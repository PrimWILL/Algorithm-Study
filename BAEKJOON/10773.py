from collections import deque

k = int(input())

queue = deque([])
for x in range(k):
    num = int(input())
    if num == 0:
        queue.pop()
    else:
        queue.append(num)

print(sum(queue))