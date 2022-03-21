from collections import deque

N, K = map(int, input().split())

dots = [False] * 100001

queue = deque([])
queue.appendleft((N, 0))
while queue:
    pos, sec = queue.pop()

    if pos == K:
        print(sec)
        break

    if not dots[pos]:
      dots[pos] = True
      
      if (pos - 1) >= 0:
        queue.appendleft((pos - 1, sec + 1))
      if (pos + 1) <= 100000:
        queue.appendleft((pos + 1, sec + 1))
      if (pos * 2) <= 100000:
        queue.appendleft((pos * 2, sec + 1))
