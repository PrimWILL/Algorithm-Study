import sys

prime_list = list()
prime_list.append(2)
for i in range(3, 246912, 2):
    floor_num = int((2 * i) ** 0.5) + 1
    prime = True

    for j in range(3, floor_num, 2):
        if (i % j == 0):
            prime = False
            break
    
    if not prime:
        continue
    else:
        prime_list.append(i)


input_n = list()
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    input_n.append(num)

for x in input_n:
    cnt = 0
    double_x = 2 * x + 1

    for i in prime_list:
        if x < i < double_x:
            cnt += 1

    print(cnt)
