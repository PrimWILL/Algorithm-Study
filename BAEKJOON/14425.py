N, M = map(int, input().split())

string = set()
for _ in range(N):
    string.add(input().strip())

result = 0
for _ in range(M):
    if input().strip() in string:
        result += 1

print(result)