import sys

stack1 = []
stack2 = []

temp = sys.stdin.readline().strip()

for x in temp:
    stack1.append(x)

M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().strip()

    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        comm, ch = command.split()
        stack1.append(ch)

for x in stack1:
    print(x, end ='')

for x in reversed(stack2):
    print(x, end = '')

print()