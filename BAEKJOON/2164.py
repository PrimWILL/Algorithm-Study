from collections import deque

N = int(input())

queue = deque([x for x in range(1, N + 1)])

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    x = queue.popleft()
    queue.append(x)
