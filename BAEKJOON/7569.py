from collections import deque

queue = deque([])

M, N, H = map(int, input().split())
box = list()

for i in range(H):
  line = list()
  for j in range(N):
    row = list(map(int, input().split()))
    line.append(row)
    
    for k in range(M):
      if row[k] == 1:
        queue.appendleft((i, j, k))
    
  box.append(line)


dx = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, -1, 1, 0, 0]

while queue:
  x, y, z = queue.pop()

  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]

    if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
      box[nx][ny][nz] = box[x][y][z] + 1
      queue.appendleft((nx, ny, nz))

def findMax(H, N):
  mx = 0
  for i in range(H):
    for j in range(N):
      if 0 in box[i][j]:
        return -1
      box_mx = max(box[i][j])
      mx = max(box_mx, mx)

  return mx - 1
    
print(findMax(H, N))