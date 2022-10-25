#첫째줄에 명령어를 입력받음. 리스트로 입력받아서 명령어 하나하나로 나눔.
command = list(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
move_dir = 3

for i in range(len(command)):
    if (command[i] == 'L'):
        move_dir = (move_dir - 1 + 4) % 4 #반시계 방향
    elif (command[i] == 'R'):
        move_dir = (move_dir + 1) % 4 #시계 방향
    else:
        x, y = x + dx[move_dir], y + dy[move_dir]

print(x, y)
