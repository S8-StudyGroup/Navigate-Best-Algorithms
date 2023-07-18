# [BOJ] 3190. 뱀
# 소요 시간 : 90분

# 뱀의 정보를 배열로

size = int(input())
apple_num = int(input())
apple_location = [tuple(map(int, input().split())) for _ in range(apple_num)]
change_num = int(input())
change_info = [input().split() for _ in range(change_num)] # X초 후 왼(L) 또는 오(D)로 이동

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
snake_dir = 1 # 처음에 오른쪽 방향
snake_body = [(1, 1)]


def direction_change(second):
    global snake_dir
    if change_info:
        a, b = change_info[0]
        if int(a) == second:
            if b == 'L':
                snake_dir = (snake_dir + 4 - 1) % 4
            elif b == 'D':
                snake_dir = (snake_dir + 1) % 4
            change_info.pop(0)


def apple(x, y):
    for i in range(len(apple_location)):
        if (x, y) == apple_location[i]:
            del apple_location[i]
            return True
    return False


def end(x, y):
    if 1 <= x < size + 1 and 1 <= y < size + 1:
        if (x, y) not in snake_body:
            return False
    return True


def snake_move(x, y):
    sec = 0
    nx = x + di[snake_dir]
    ny = y + dj[snake_dir]

    while not end(nx, ny):
        sec += 1
        snake_body.append((nx, ny))
        if not apple(nx, ny):
            snake_body.pop(0) # 꼬리 이동
        direction_change(sec)
        nx += di[snake_dir]
        ny += dj[snake_dir]

    return sec + 1

print(snake_move(1, 1))
