from collections import Counter

name = sorted(list(input()))
counter = dict(Counter(name))
num_counter = Counter(list(x for x in counter.values() if x % 2 == 1))

if len(num_counter) > 1 or (len(num_counter) == 1 and list(num_counter.values())[0] > 1):            # 개수가 홀수인 문자가 여러개인 경우
    print("I'm Sorry Hansoo")
else:
    stack = []
    result = ''
    char = ''

    for key, value in counter.items():
        while value > 0:
            if value == 1:
                char = key
                break
            value -= 2
            result += key
            stack.append(key)

    result += char
    while stack:
        result += stack.pop()

    print(result)
