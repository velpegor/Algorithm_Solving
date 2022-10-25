a = list(input())

sum = 0
stack = []

for i in range(len(a)):
    if a[i] == '(':
        stack.append('(')
    else:
        if a[i-1] == '(':
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1

print(sum)
