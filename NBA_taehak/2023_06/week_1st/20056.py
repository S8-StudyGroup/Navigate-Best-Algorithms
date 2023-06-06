# [BOJ] 20056. 마법사 상어와 파이어볼
# 소요 시간 : 00분

delta = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
]

size, ball_cnt, command_cnt = map(int, input().split())
balls = []
for _ in range(ball_cnt):
    r, c, mass, velocity, direction = map(int, input().split())
    balls.append((r-1, c-1, mass, velocity, direction))

area = [[[] for _ in range(size)] for _ in range(size)]

for command in range(command_cnt):
    while balls:
        r, c, mass, velocity, direction = balls.pop()
        dr, dc = delta[direction]
        nr = (r + velocity * dr) % size
        nc = (c + velocity * dc) % size
        area[nr][nc].append((nr, nc, mass, velocity, direction))

    for row in range(size):
        for col in range(size):
            area_ball = area[row][col]
            area_ball_cnt = len(area_ball)
            if area_ball_cnt > 1:
                sum_mass = 0
                sum_velocity = 0
                sum_direction = 0

                while area_ball:
                    r, c, mass, velocity, direction = area_ball.pop()
                    sum_mass += mass
                    sum_velocity += velocity
                    if direction % 2 == 0:
                        sum_direction += 1
                    else:
                        sum_direction -= 1
                
                new_mass = sum_mass // 5

                if new_mass == 0:
                    continue

                new_velocity = sum_velocity // area_ball_cnt
                direction_start_idx = 1

                if sum_direction == area_ball_cnt or sum_direction == - area_ball_cnt:
                    direction_start_idx = 0
                
                for new_direction in range(direction_start_idx, direction_start_idx + 8, 2):
                    balls.append((row, col, new_mass, new_velocity, new_direction))

            elif area_ball_cnt == 1:
                balls.append(area_ball.pop())

answer = 0
while balls:
    r, c, mass, velocity, direction = balls.pop()
    answer += mass

print(answer)