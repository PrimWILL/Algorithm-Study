str1 = ' ' + input().strip()
str2 = ' ' + input().strip()

LCS = [[0] * len(str1) for _ in range(len(str2))]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str2[i] == str1[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])