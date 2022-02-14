N = int(input())

nums = [list(map(int, input().split())) for _ in range(N)]

nums.sort(key = lambda x: (x[1], x[0]))
for x in nums:
    print(f'{x[0]} {x[1]}')