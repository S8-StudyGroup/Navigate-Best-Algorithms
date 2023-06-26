# [BOJ] 16988. Baaaaaaaaaduk2 (Easy)
# 소요 시간 : 90++분

from collections import deque, defaultdict

def bfs(i, j, team):
    matrix[i][j] += team 
    queue = deque()
    queue.append((i, j))
    blank_set = set()
    blank = 0
    stone = 1
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if 0 <= move_y < N and 0 <= move_x < M:
                if matrix[move_y][move_x] == 0 and (move_y, move_x) not in blank_set:
                    blank += 1
                    blank_set.add((move_y, move_x))
                
                if matrix[move_y][move_x] == 2:
                    matrix[move_y][move_x] = matrix[y][x]
                    queue.append((move_y, move_x))
                    stone += 1

    if len(blank_set) == 1:
        return [list(blank_set)[0], stone]
    elif len(blank_set) == 2:
        blank_list = sorted(list(blank_set))
        return [(*blank_list[0], *blank_list[1]), stone]
    else:
        return [(), -1]


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
team = 1
stone_list = defaultdict(int)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            blank_tuple, stone = bfs(i, j, team)
            if stone != -1:
                stone_list[blank_tuple] += stone
            team += 1

max_with_one_stone = [0, 0]
max_with_two_stone = 0
stone_keys = list(stone_list.keys())[:]
for key in stone_keys:
    if len(key) == 2:
        if max_with_one_stone[0] < stone_list[key]:
            max_with_one_stone = [stone_list[key], max_with_one_stone[0]]
        elif max_with_one_stone[1] < stone_list[key]:
            max_with_one_stone[1] = stone_list[key]
    else:
        max_with_two_stone = max(max_with_two_stone, stone_list[(key[0], key[1])] + stone_list[(key[2], key[3])] + stone_list[key])

print(max(sum(max_with_one_stone), max_with_two_stone))