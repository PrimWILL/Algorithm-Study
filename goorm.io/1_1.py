myteam = list(map(int, input().split()))
mywish = list(map(int, input().split()))
count = 0
for x in range(len(mywish)):
    temp = 0
    for y in range(len(myteam)):
        if mywish[x] == myteam[y]:
            temp += 1
            continue
    if temp == 0:
        count += 1

print(count)