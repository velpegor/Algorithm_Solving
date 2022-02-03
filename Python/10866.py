from collections import deque
import sys

n = int(sys.stdin.readline())

dq = deque()

for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push_front':
        dq.appendleft(cmd[-1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[-1])
    elif cmd[0] == 'pop_front':
        if len(dq) != 0:
            a = dq.popleft()
            print(a)
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(dq) != 0:
            b = dq.pop()
            print(b)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if len(dq) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)