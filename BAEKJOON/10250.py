import sys

T = int(sys.stdin.readline())
customer = list()
for x in range (T):
    customer.append((list(map(int, sys.stdin.readline().split()))))

for x in range (T):
    room_num = 1
    H, W, N = customer[x]
    while (N > H):
        N -= H
        room_num += 1
    print(N, end='')
    if (len(str(room_num)) == 2):
        pass
    else:
        print("0", end='')
    print(room_num)
    