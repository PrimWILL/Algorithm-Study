from collections import deque

queue = deque([])

M, N = map(int, input().split())
box = list()

for i in range(N):
  line = list(map(int, input().split()))
  box.append(line)

  for j in range(M):
    if line[j] == 1:
      queue.appendleft((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
  x, y = queue.pop()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
      box[nx][ny] = box[x][y] + 1
      queue.appendleft((nx, ny))

mx = 0
cp = False
for i in range(N):
  if 0 in box[i]:
    cp = True
    break
  box_mx = max(box[i])
  mx = max(box_mx, mx)
if cp:
  print(-1)
else:
  print(mx - 1)
  