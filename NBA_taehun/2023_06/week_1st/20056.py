# [BOJ] 20056. 마법사 상어와 파이어볼
# 소요 시간 : 00분

import sys
from collections import defaultdict

input = sys.stdin.readline


# 방향 d로 속력 s만큼 이동한다.
def rule_1(r, c, d, s):
    dr, dc = rule[d]
    nr, nc = r + (dr * s), c + (dc * s)

    # 범위 안으로 조정
    while True:
        if nr < 0:
            nr = N - (abs(nr) % N)
        elif nr >= N:
            nr %= N
        else:
            break

    while True:
        if nc < 0:
            nc = N - (abs(nc) % N)
        elif nc >= N:
            nc %= N
        else:
            break
    return nr, nc


# 같은 칸에 있는 파이어볼 처리
def rule_2(fire_balls_info):
    m_sum, s_sum, d_set, count = 0, 0, set(), 0
    for info in fire_balls_info:
        count += 1
        m, s, d = info
        m_sum += m
        s_sum += s
        if d % 2 == 0:
            d_set.add(0)
        else:
            d_set.add(1)
    # 질량 = 합쳐진 파이어볼 질량의 합 / 5
    nm = m_sum // 5
    # 속력 = 합쳐진 파이어볼 속력의 합 / 합쳐진 파이어볼 개수
    ns = s_sum // count
    if nm > 0:
        new_fire_balls = []
        if len(d_set) == 1:
            ds = [0, 2, 4, 6]
        else:
            ds = [1, 3, 5, 7]
        for nd in ds:
            new_fire_balls.append((nm, ns, nd))
        return new_fire_balls
    return []


rule = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M, K = map(int, input().strip().split())

fire_balls = defaultdict(list)
# M이 0인 경우가 있다.
turn = 0
for _ in range(M):
    r, c, m, s, d = map(int, input().strip().split())
    fire_balls[(r, c)].append((m, s, d))


while turn < K:
    items = list(fire_balls.items())
    fire_balls = defaultdict(list)

    # 1 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다
    while items:
        location, infos = items.pop()
        for info in infos:
            nr, nc = rule_1(location[0], location[1], info[2], info[1])
            fire_balls[(nr, nc)].append(info)

    # 2 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
    keys = list(fire_balls.keys())
    for location in keys:
        if len(fire_balls[location]) > 1:
            new_fire_balls = rule_2(fire_balls[location])
            if not new_fire_balls:
                del fire_balls[location]
            else:
                fire_balls[location] = new_fire_balls
    turn += 1

result = 0
for infos in fire_balls.values():
    for info in infos:
        result += info[0]

print(result)
