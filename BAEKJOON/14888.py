import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

result = [2e9, -2e9] # result[0] is min, result[1] is max
visited = [0] * 4

def dfs(i, s, plus, minus, mul, div):
    if i == N:
        result[0] = min(s, result[0])
        result[1] = max(s, result[1])
        return
    
    if plus:
        dfs(i + 1, s + nums[i], plus - 1, minus, mul, div)
    if minus:
        dfs(i + 1, s - nums[i], plus, minus - 1, mul, div)
    if mul:
        dfs(i + 1, s * nums[i], plus, minus, mul - 1, div)
    if div:
        if s >= 0:
            dfs(i + 1, s // nums[i], plus, minus, mul, div - 1)
        else:
            dfs(i + 1, -(-s // nums[i]), plus, minus, mul, div - 1)


dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(result[1])
print(result[0])
        
