a = input()

temp = ''
ans = ''

for i in a:
    if i == ' ':
        if '<' not in temp:
            ans += temp[::-1] + i
            temp = ''
        else:
            temp += i
    elif i == '<':
        ans += temp[::-1]
        temp = ''
        temp += i
    elif i == '>':
        ans += temp + i
        temp = ''
    else:
        temp += i

ans += temp[::-1]
print(ans)