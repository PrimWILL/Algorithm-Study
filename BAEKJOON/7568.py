N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    x = people[i][0]
    y = people[i][1]

    for j in range(N):
        if i == j:
            continue

        p = people[j][0]
        q = people[j][1]

        if x > p and y > q:
            rank[j] += 1

print(' '.join(map(str, rank)))
        