from itertools import combinations

N = int(input())

ability = list()
for _ in range(N):
    ability.append(list(map(int, input().split())))

members = [x for x in range(N)]
team = list(combinations(members, N // 2))

mn = 1e9
for i in range(len(team) // 2):
    start = team[i]
    s_start = 0
    for j in start:
        for k in start:
            s_start += ability[j][k]

    link = team[-i - 1]
    s_link = 0
    for j in link:
        for k in link:
            s_link += ability[j][k]

    mn = min(mn, abs(s_start - s_link))

print(mn)