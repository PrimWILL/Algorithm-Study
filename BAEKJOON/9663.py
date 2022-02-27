import sys

N = int(sys.stdin.readline())

board = [0] * N
queen = [0] * N
result = 0

# def check(index):
#     for x in range(index):
#         if abs(board[index] - board[x]) == index - x:
#             return False
#     return True

def dfs(index):
    if index == N:
        global result
        result += 1
        return
    else:
        for i in range(N):
            if queen[i]:
                continue

            board[index] = i

            check = True
            for x in range(index):
                if abs(board[index] - board[x]) == index - x:
                    check = False
                    break

            if check:
                queen[i] = 1
                dfs(index + 1)
                queen[i] = 0

dfs(0)
print(result)