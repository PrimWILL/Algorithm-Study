N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
cur = price[0]
s_dist = 0
for i in range(N - 1):
    if cur > price[i]:
        result += cur * s_dist
        s_dist = dist[i]
        cur = price[i]
        continue

    s_dist += dist[i]

result += cur * s_dist
print(result)