# [BOJ] 7562. 나이트의 이동
# 소요 시간 : 30분

import sys
from collections import deque

input = sys.stdin.readline

def bfs(r, c, cnt):
    global tr, tc, i

    # 방문 처리
    visited = set()

    # deque 선언
    dq = deque([(r, c, cnt)])
    visited.add((r,c))

    # 목표 위치에 도착한 경우
    if tr == r and tc == c:
        return cnt
    while dq:
        r, c , cnt = dq.popleft()
        if tr == r:
            if tc < c:
                d = [2, 3]
            else:
                d = [1, 4]
        elif tc == c:
            if tr < r:
                d = [1, 2]
            else:
                d = [3, 4]

        # 이 아래의 케이스에 각각 한가지 사분면만 적용했을 때 83%에서 틀리는 문제 발생
        elif tr < r and tc > c:
            d = [1, 2, 4]
        elif tr < r and tc < c:
            d = [2, 1, 3]
        elif tr > r and tc < c:
            d = [3, 2, 4]
        else:
            d = [4, 1, 3]
        for dn in d:
            for dr, dc in d_dict[dn]:
                nr, nc = r + dr, c + dc

                # 이동할 위치가 목표 위치인 경우 한번 더 검사
                if nr == tr and nc == tc:
                    return cnt + 1

                # 다음 위치가 범위 내에 있고, 방문하지 않은 곳일 때
                if 0 <= nr < i and 0 <= nc < i and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dq.append((nr, nc, cnt + 1))
# 움직일 수 있는 방향
d_dict = {1: [(-2, 1), (-1, 2)], 2: [(-1, -2), (-2, -1)], 3: [(1, -2), (2, -1)], 4: [(2, 1) , (1, 2)]}

# 테스트 케이스
tc = int(input().strip())
result = []
for _ in range(tc):
    i = int(input().strip())
    r,c = map(int,input().strip().split())
    tr,tc = map(int,input().strip().split())

    # bfs
    result.append(bfs(r, c, 0))
print(*result, sep='\n')