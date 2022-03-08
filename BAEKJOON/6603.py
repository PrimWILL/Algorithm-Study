result = list()

def dfs(s, k):
    if len(result) == 6:
        if sorted(result) == result and len(set(result)) == 6:
            print(" ".join(map(str, result)))
        return
    
    for x in range(k):
        if s[x] in result:
            continue
        result.append(s[x])
        dfs(s, k)
        result.pop()

while True:
    test_case = list(map(int, input().split()))

    if not test_case[0]:
        break

    k = test_case[0]
    dfs(test_case[1:], k)
    print()
