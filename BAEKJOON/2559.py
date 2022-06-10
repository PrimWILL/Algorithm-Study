N, K = map(int, input().split())

temperature = list(map(int, input().split()))

result = [sum(temperature[0:K])]
for i in range(N - K):
    result.append(result[i] - temperature[i] + temperature[i + K])

print(max(result))