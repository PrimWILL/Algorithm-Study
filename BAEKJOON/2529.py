k = int(input())
inequality = list(map(str, input().split()))

temp = list()
result = [-1 , -1]

visited = [0] * 10

def find(index):
    if len(temp) == k + 1:
        if result[0] == -1:
            result[0] = "".join(map(str, temp))
        else:
            result[1] = "".join(map(str, temp))
        return

    for x in range(10):
        if visited[x]:
            continue
        if inequality[index] == '<':
            if temp[-1] < x:
                temp.append(x)
                visited[x] = 1
                find(index + 1)
                temp.pop()
                visited[x] = 0
        else:
            if temp[-1] > x:
                temp.append(x)
                visited[x] = 1
                find(index + 1)
                temp.pop()
                visited[x] = 0

for i in range(10):
    temp.append(i)
    visited[i] = 1
    find(0)
    temp.pop()
    visited[i] = 0

print(result[1])
print(result[0])