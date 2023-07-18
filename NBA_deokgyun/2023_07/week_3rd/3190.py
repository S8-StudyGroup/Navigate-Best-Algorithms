# [BOJ] 3190. 뱀
# 소요 시간 : 00분
from collections import deque

def rotate(x, lr):
    dir_list = [(0,1), (1,0), (0,-1), (-1,0)]
    idx = dir_list.index(x)
    if lr == "L":
        return dir_list[idx - 1]
    else:
        return dir_list[(idx + 1) % 4]

length = int(input())
apple = []
for _ in range(int(input())):
    apple.append(tuple(map(lambda x: int(x) - 1, input().split())))
steer = deque([])
steer_len = 0
for _ in range(int(input())):
    steer.append((lambda x: (int(x[0]), x[1]))(input().split()))
    steer_len += 1

time_cnt = 0
snake = deque([(0,0)])
dir = (0,1)

plustuple = lambda x, y: (x[0] + y[0], x[1] + y[1])

while True:
    time_cnt += 1
    head = plustuple(snake[-1], dir)
    if head in snake or not(0 <= head[0] < length and 0 <= head[1] < length):
        print(time_cnt)
        break
    snake.append(head)
    try:
        appleidx = apple.index(head)
        apple.pop(appleidx)
    except ValueError:
        snake.popleft()
    if steer_len > 0:
        if time_cnt == steer[0][0]:
            dir = rotate(dir, steer.popleft()[1])
            steer_len -= 1