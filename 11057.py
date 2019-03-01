length = input()
length = int(length)
wlength = length
flag = 1
count = 1
upGoing = list()

upGoing.append(1)

if length > 1:
   while length > 1:
       upGoing.append(1)
       length -= 1

print (upGoing)
""""""
while sum(upGoing) != (wlength*9):

    for i in upGoing:
        if upGoing[i] < upGoing[i+1]:
            count += 1
""""""





print(upGoing)
