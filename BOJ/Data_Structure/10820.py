import sys

while True:
    so = 0
    dae = 0
    num = 0
    space = 0
    arr = sys.stdin.readline().rstrip('\n')
    if not arr:
        break
    for i in arr:
        if i.isupper():
            dae += 1
        elif i.islower():
            so += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1
    print(so, dae, num, space)
