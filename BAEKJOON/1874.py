n = int(input())

stack = list()
nums = [x for x in reversed(range(1, n+1))]
ans = list()

stack.append(nums.pop())
ans.append('+')

for _ in range(n):
    num = int(input())
    
    while not stack or stack[-1] < num:
        if not nums:
            print('NO')
            exit()
        stack.append(nums.pop())
        ans.append('+')

    while stack and stack[-1] > num:
        stack.pop()
        ans.append('-')

    if stack and stack[-1] == num:
        stack.pop()
        ans.append('-')

for x in ans:
    print(x)