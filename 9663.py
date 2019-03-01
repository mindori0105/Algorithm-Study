#let's solve N-Queen algorithm!!

import pprint

#queen을 몇 개 로 설정할지 입력을 받는다.
N = input()
N = int(N)

col = list()

for i in range(0, N):
    col.append(i)

print(col)
