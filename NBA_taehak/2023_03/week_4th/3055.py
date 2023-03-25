# [BOJ] 3055. 탈출
# 소요 시간 : 00분
rsize, csize = map(int, input().split())
area = [list(input()) for _ in range(rsize)]

water = []
for r in range(rsize):
    for c in range(csize):
        if area[r][c] == 'S':
            runner_start = (r, c)
        elif area[r][c] == '*':
            water.append((r, c))


def inrange(r, c):
    '''
    r: 행
    c: 열
    output: 범위안에 있으면 True 아니면 False
    '''
    if 0 <= r < rsize and 0 <= c < csize:
        return True
    else:
        return False


def bfs(runner_start, water):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    time = 0

    runner = [runner_start]
    runner_cnt = [0, 1]
    water_cnt = [0, len(water)]

    while runner_cnt[-1] != runner_cnt[-2]:
        time += 1

        # print('++++++++++++++++++++++++++++++++++++++++++++++')
        # print(time)
        # for i in area:
        #     print(i)
        

        # 물이 먼저 이동
        for w in range(water_cnt[time-1], water_cnt[time]):
            wr, wc = water[w]
            for dr, dc in delta:
                nr = wr + dr
                nc = wc + dc
                if inrange(nr, nc) and area[nr][nc] in ['.', 'S']:
                    area[nr][nc] = '*'
                    water.append((nr, nc))
        water_cnt.append(len(water))

        # 고슴도치가 이동
        for r in range(runner_cnt[time-1], runner_cnt[time]):
            rr, rc = runner[r]
            for dr, dc in delta:
                nr = rr + dr
                nc = rc + dc
                if inrange(nr, nc):
                    if area[nr][nc] == 'D':
                        return time
                    elif area[nr][nc] == '.':
                        area[nr][nc] = 'S'
                        runner.append((nr, nc))
        runner_cnt.append(len(runner))

        # print(runner_cnt)
        # print('++++++++++++++++++++++++++++++++++++++++++++++')
    return 'KAKTUS'


print(bfs(runner_start, water))