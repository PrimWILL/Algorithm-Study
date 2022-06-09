string = input()
result = set()

for i in range(1, len(string) + 1):
    for j in range(len(string) - i + 1):
        result.add(string[j:j + i])

print(len(result))