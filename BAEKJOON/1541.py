equation = input().split('-')

result = 0
for i in range(len(equation)):
  temp = list(map(int, equation[i].split('+')))
  if i == 0:
    result += sum(temp)
  else:
    result -= sum(temp)

print(result)