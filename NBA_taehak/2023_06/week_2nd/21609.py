# [BOJ] 21609. 상어 중학교
# 소요 시간 : 00분

# 검은색, 무지개, 일반(M가지 색상)
# -1, 0, ~

# 1. 연결된 
# 2. 일반블록 하나이상
# 3. 일반블록 같은색
# 4. 검은색 블록 x
# 5. 무지개 블록은 상관 없
# 6. 개수2개이상
# 7. 기준블록 : 행열 번호가 가장 낮은(무지개가아닌)

# 1. 블록그룹 찾기
## 개수가 가장 많은
## 무지개블록많은거
## 기준블록 행이 가장 큰거
## 기준블록 열이 가장 큰거
# 2. 1에서 찾은거 제거, 점수 (개수)^2 만큼 얻고
# 3. 중력작용 : 검은블록 빼고 모든 블록이 행의 번호가 큰칸으로 이동
# 4. 90도 반시계 회전
# 5. 중력작용
# 반복: 블록 그룹이 존재하는 동안 계속해서 반복

from collections import deque


def inrange(r, c):
    return 0 <= r < size and 0 <= c < size


def block_group(nomal_r, nomal_c):
    '''
    r, c는 일반블록의 행열좌표
    r, c 에서 시작된 블록그룹정보를 출력하는 함수
    그룹크기, 행열좌표, 무지개블록개수, 기준블록좌표
    '''
    group_color = area[nomal_r][nomal_c]
    que = deque([(nomal_r, nomal_c)])
    visited[nomal_r][nomal_c] = True
    block_visited = [[False] * size for _ in range(size)]

    group_rc = []
    rainbow_cnt = 0

    while que:
        r, c = que.popleft()
        group_rc.append((r, c))

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if inrange(nr, nc):

                # 같은색
                if area[nr][nc] == group_color and not visited[nr][nc]:
                    visited[nr][nc] = True
                    que.append((nr, nc))

                # 무지개블록
                elif area[nr][nc] == rainbow_color and not block_visited[nr][nc]:
                    block_visited[nr][nc] = True
                    que.append((nr, nc))
                    rainbow_cnt += 1

    # 기준블록 : 행 열 번호가 낮은
    group_rc.sort(key=lambda x : (x[0], x[1]))

    # 기분블록 : 무지개 블록 제외
    for r, c in group_rc:
        if area[r][c] > 0:
            main_rc = (r, c)
            break

    return len(group_rc), group_rc, rainbow_cnt, main_rc


def get_max_group():
    global group

    for r in range(size):
        for c in range(size):
            if area[r][c] > 0 and not visited[r][c]:
                group_size, group_rc, rainbow_cnt, main_rc = block_group(r, c)

                if group_size <= 1:
                    continue

                if group_size > group[0]:
                    group = (group_size, group_rc, rainbow_cnt, main_rc)
                elif group_size == group[0]:
                    if rainbow_cnt > group[2]:
                        group = (group_size, group_rc, rainbow_cnt, main_rc)
                    elif rainbow_cnt == group[2]:
                        if main_rc[0] > group[3][0]:
                            group = (group_size, group_rc, rainbow_cnt, main_rc)
                        elif main_rc[0] == group[3][0]:
                            if main_rc[1] > group[3][1]:
                                group = (group_size, group_rc, rainbow_cnt, main_rc)


def del_block():
    for r, c in group[1]:
        area[r][c] = -2


def gravity():
    for c in range(size):
        for r in range(size - 2, -1, -1):
            if area[r][c] > -1:
                while 0 <= r < size-1 and area[r + 1][c] == blank:
                    area[r + 1][c], area[r][c] = area[r][c], area[r + 1][c]
                    r += 1


def rotate():
    return list(map(list, zip(*area)))[::-1]


size, color_cnt = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(size)]

blank = -2
black_color = -1
rainbow_color = 0
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

score = 0

while True:
    group = (1, [], 0, ())
    visited = [[False] * size for _ in range(size)]
    get_max_group()

    if group[0] == 1:
        break

    score += group[0]**2
    del_block()
    gravity()
    area = rotate()
    gravity()

print(score)