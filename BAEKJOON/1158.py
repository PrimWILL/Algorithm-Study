from collections import deque

N, K = map(int, input().split())

queue = deque([x for x in range(1, N + 1)])
result = list()

while queue:
    index = K - 1
    index %= len(queue)

    queue.rotate(-index)
    result.append(queue.popleft())

# print("<", end = '')
# for i in range(N):
#     if i == N - 1:
#         print(f'{result[i]}>')
#     else:
#         print(result[i], end = ", ")

print("<" + ", ".join(map(str, result)) + ">")