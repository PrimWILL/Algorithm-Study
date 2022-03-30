K, N = map(int, input().split())

line = [int(input()) for _ in range(K)]

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in line:
        cnt += x // mid
    
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)