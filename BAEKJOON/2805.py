N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    cnt = sum(x - mid for x in trees if x > mid)
    
    if cnt < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)