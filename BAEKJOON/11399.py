N = int(input())

time = list(map(int, input().split()))
time.sort()

minimum = 0
wait = 0
for x in time:
    wait += x
    minimum += wait

print(minimum)