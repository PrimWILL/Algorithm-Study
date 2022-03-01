T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    circle = (x1 - x2) ** 2 + (y1 - y2) ** 2
    dist = (r1 + r2) ** 2

    if circle == 0 and r1 == r2:                        # 아예 같은 원인 경우
        print(-1)
    elif circle == dist or circle == (r1 - r2) ** 2:    # 내접 및 외접
        print(1)
    elif abs(r1 - r2) ** 2 < circle < dist:             # 서로 다른 두 점 
        print(2)
    else:                                               # 안 만나는 경우(원 안에 원, 서로 동떨어져 있는 경우)
        print(0)