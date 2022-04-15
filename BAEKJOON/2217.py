N = int(input())
rope = [int(input()) for x in range(N)]
rope.sort()

result = 0
for i in range(N):
    temp = rope[i] * (N - i)
    if temp > result:
        result = temp

print(result)