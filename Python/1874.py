n = int(input())
arr = []
stack = []
cur = 1

temp = True

for i in range(n):
    num = int(input())
    while cur <= num:
        arr.append(cur)
        cur += 1
        stack.append('+')

    if arr[-1] == num:
        stack.append('-')
        arr.pop()
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in stack:
        print (i)