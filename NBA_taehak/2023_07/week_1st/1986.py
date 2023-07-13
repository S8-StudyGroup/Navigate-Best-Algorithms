# [BOJ] 1986. 체스
# 소요 시간 : 00분

row_size, col_size = map(int, input().split())
queen_input = list(map(int, input().split()))
knight_input = list(map(int, input().split()))
pawn_input = list(map(int, input().split()))

board = [[0] * col_size for _ in range(row_size)]
unit_info = {x:[] for x in range(3)}
unit_cnt = 0

for unit_idx, unit_input in enumerate([queen_input, knight_input, pawn_input]):
    unit_cnt += unit_input[0]
    for unit in range(unit_input[0]):
        r, c = (unit_input[unit * 2 + 1] - 1, unit_input[unit * 2 + 2] - 1)
        unit_info[unit_idx].append((r, c))
        board[r][c] = 1

# print('{0: queen, 1: knight, 2: pawn}\nunit_info :', unit_info)
# for line in board: print(line)


def inrange(r, c):
    return 0 <= r < row_size and 0 <= c < col_size


# 안전하지 않은 좌표
not_safe = set()

# queen check
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for qr_start, qc_start in unit_info[0]:
    for dr, dc in delta:
        qr, qc = qr_start, qc_start
        while True:
            nr = qr + dr
            nc = qc + dc
            if inrange(nr, nc) and board[nr][nc] == 0:
                not_safe.add((nr, nc))
                qr, qc = nr, nc
            else:
                break

# knight check
knight_delta = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for kr_start, kc_start in unit_info[1]:
    for dr, dc in knight_delta:
        kr = kr_start + dr
        kc = kc_start + dc
        if inrange(kr, kc) and board[kr][kc] == 0:
            not_safe.add((kr, kc))


print(row_size * col_size - unit_cnt - len(not_safe))