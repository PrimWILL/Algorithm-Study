def binary_search(num):
    start = 0
    end = len(lis)

    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if num <= lis[mid]:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    return answer

N = int(input())
seq = list(map(int, input().split()))

lis = list()
lis.append(seq[0])

for x in seq:
    if x == lis[-1]:
        continue 
    elif x > lis[-1]:
        lis.append(x)
    else:
        index = binary_search(x)
        lis[index] = x

print(len(lis))   