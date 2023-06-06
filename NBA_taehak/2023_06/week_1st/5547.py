# [BOJ] 5547. 일루미네이션
# 소요 시간 : 00분

# bfs로 외곽은 True
# 행열 전체 순회하면서 6방향 체크하기

from collections import deque

x_size_0, y_size_0 = map(int, input().split())
x_size, y_size = x_size_0 + 2, y_size_0 + 2
area_0 = [[0] * (x_size)] + [[0] + list(map(int, input().split())) + [0] for _ in range(y_size_0)] + [[0] * (x_size)]
area = [[False] * (x_size) for _ in range(y_size)]

# 6방향 델타
hexa_even = [(-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]
hexa_odd = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (1, 1)]
hexa = [hexa_even, hexa_odd]

# 덩어리 체크, 외곽은 True
que = deque([(0, 0)])
area[0][0] = True

while que:
    x, y = que.popleft()

    for dx, dy in hexa[y % 2]:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < x_size and 0 <= ny < y_size and not area[ny][nx] and area_0[ny][nx] == 0:
            area[ny][nx] = True
            que.append((nx, ny))

# 6방향 체크
answer = 0

for y in range(1, 1 + y_size_0):
    for x in range(1, 1 + x_size_0):

        # 외곽은 넘기고
        if area[y][x]:
            continue
        
        # y좌표가 짝수인지 홀수인지
        # 6방향 체크해서 외곽이면 길이 추가
        for dx, dy in hexa[y % 2]:
            ny = y + dy
            nx = x + dx

            if area[ny][nx]:
                answer += 1

print(answer)
