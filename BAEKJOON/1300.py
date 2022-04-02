N = int(input())
k = int(input())

left = 1
right = k
answer = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, mid // i)

    if cnt < k:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)