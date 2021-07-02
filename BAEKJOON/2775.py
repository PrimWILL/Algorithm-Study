import sys

T = int(sys.stdin.readline())
resident = list()

for x in range (T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    resident.append((k, n))


for x in range (T):
    k = resident[x][0]
    n = resident[x][1]
    floor = 0
    apartment = [x for x in range (1, n + 1)]

    while (floor < k) :
        for i in range (1, n):
            apartment[i] = apartment[i] + apartment[i-1]

        floor += 1
    
    print(apartment[n - 1])