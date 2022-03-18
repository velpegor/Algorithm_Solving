n = int(input())
s = input()
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

stack = []

for i in s:
    if 'A' <= i <= 'Z':
        stack.append(arr[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
            print(str1 / str2)

print("{:.2f}".format(stack[0]))

