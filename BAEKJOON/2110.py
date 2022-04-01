import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    temp = house[0]
    for i in range(1, N):
        if temp + mid <= house[i]:
            cnt += 1
            temp = house[i]
    
    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)