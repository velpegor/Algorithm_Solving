n = int(input())

for i in range(n):
    num0 = [1,0]
    num1 = [0,1]
    num = int(input())
    if num >1:
        for i in range(num-1):
            num0.append(num1[-1])
            num1.append(num0[-2]+num1[-1])

    print(num0[num], num1[num])
