bar = int(64)
ans = i = 0
bCount = 0
print('input the length of the bar ', end='')
X0 = input()
X = int(X0)
while i == 0:
    print(1)
    if X > (ans + bar):
        ans += bar
        bCount += 1
        bar = bar/2
        print(2)

    if X == (ans + bar):
        bCount += 1
        i -= 1
        print(3)

    if X < (ans + bar):
        bar = bar/2
        print(4)
a
print(bCount, end='')
print('개')
