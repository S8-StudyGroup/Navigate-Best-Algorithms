# [BOJ] 1194. 달이 차오른다, 가자.
# 소요 시간 : 00분
from collections import deque

# Input
row_size, col_size = map(int, input().split())
maze = [input() for _ in range(row_size)]

# const
keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for r in range(row_size):
    for c in range(col_size):
        if maze[r][c] == '0':
            sr = r
            sc = c

keys_bin = {}
doors_bin = {}
for idx in range(1, 7):
    keys_bin[keys[idx-1]] = idx
    doors_bin[doors[idx-1]] = idx


# canOpen
def canOpen(cur_key, door):
    value = cur_key & (1 << (doors_bin[door] - 1))
    if value > 0:
        return True
    else:
        return False


# bfs
def bfs(sr, sc):
    que = deque([(sr, sc, 0, 0)])
    check = [[[False] * (1 << 6) for _ in range(col_size)] for _ in range(row_size)]
    check[sr][sc][0] = True

    while que:
        r, c, cnt, key = que.popleft()

        if maze[r][c] == '1': 
            return cnt
        
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < row_size and 0 <= nc < col_size and not check[nr][nc][key]:
                if maze[nr][nc] in ['1', '.', '0']:
                    check[nr][nc][key] = True
                    que.append((nr, nc, cnt + 1, key))
                elif maze[nr][nc] in keys:
                    tmp_key = key | (1 << (keys_bin[maze[nr][nc]] - 1))
                    check[nr][nc][tmp_key] = True
                    que.append((nr, nc, cnt + 1, tmp_key))
                elif maze[nr][nc] in doors:
                    if canOpen(key, maze[nr][nc]):
                        check[nr][nc][key] = True
                        que.append((nr, nc, cnt + 1, key))
    return -1


# Output
print(bfs(sr, sc))