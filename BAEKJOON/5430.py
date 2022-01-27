import sys
from collections import deque

T = int(sys.stdin.readline())
direct = True
error = False

for _ in range(T):
    p = deque(list(sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())
    if n == 0:
        sys.stdin.readline()
        d = deque([])
    else:
        d = deque(sys.stdin.readline().strip()[1:-1].split(','))

    while p:
        func = p.popleft()
        if func == 'R':
            direct = not direct
        else:
            if d:
                if direct:
                    d.popleft()
                else:
                    d.pop()
            else:
                error = True
                break
    
    if error:
        print('error')
    else:
        if direct:
            print("[" + ",".join(d) + "]")
        else:
            d.reverse()
            print("[" + ",".join(d) + "]")
    
    error = False
    direct = True