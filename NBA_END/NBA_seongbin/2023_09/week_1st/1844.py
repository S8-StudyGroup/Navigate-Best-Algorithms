# [Programmers] 1844. 게임 맵 최단거리
# 소요 시간 : 00분
def solution(maps):
    row = len(maps) - 1
    col = len(maps[0]) - 1
    queue = [[0, 0, 1]]
    maps[0][0] = 0
    while queue:
        r, c, count = queue.pop(0)
        if r == row and c == col:
            return count
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr > row or 0 > nc or nc > col:
                continue
            if maps[nr][nc] == 0:
                continue
            maps[nr][nc] = 0
            queue.append([nr, nc, count + 1])
    return -1
