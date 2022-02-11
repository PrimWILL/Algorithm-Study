# 메모리 초과
# n = int(input())

# triangle = [list(map(int, input().split())) for _ in range(n)]
# result = list()

# def tri_sum(i, j, s):
#     if i == n - 1:
#         result.append(s)
#         return

#     left = (j+1)//2
#     right = (j+1)//2 + 1

#     tri_sum(i + 1, left, s + triangle[i + 1][left])
#     tri_sum(i + 1, right, s + triangle[i + 1][right])

# tri_sum(0, 0, triangle[0][0])
# print(max(result))

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][0]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n - 1]))