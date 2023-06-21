# [BOJ] 17837. 새로운 게임 2
# 소요 시간 : 00분
def newgame2():
    turn = 1

    while turn <= turn_limit:
        for unit_num in range(unit_cnt):
            r, c, di = unit_info[unit_num]
            nr = r + dr[di]
            nc = c + dc[di]

            # 범위밖 or 파란색
            if not (0 <= nr < size and 0 <= nc < size) or board_color[nr][nc] == blue:
                di = change_di[di]
                nr = r + dr[di]
                nc = c + dc[di]
                if not (0 <= nr < size and 0 <= nc < size) or board_color[nr][nc] == blue:
                    nr = r
                    nc = c

            unit_info[unit_num] = [nr, nc, di]

            # 제자리일경우
            if nr == r and nc == c:
                continue
            
            # 옮기는거 mass
            idx = board[r][c].index(unit_num)
            mass = board[r][c][idx:]
            board[r][c] = board[r][c][:idx]
            for unit in mass:
                unit_info[unit][0] = nr
                unit_info[unit][1] = nc
            
            # 흰색일경우
            if board_color[nr][nc] == white:
                board[nr][nc] = board[nr][nc] + mass
            # 빨간색일경우
            elif board_color[nr][nc] == red:
                board[nr][nc] = board[nr][nc] + mass[::-1]
            
            # 게임종료조건
            if len(board[nr][nc]) >= 4:
                return turn

        turn += 1

    return -1


# 0: 흰색, 1: 빨간색, 2: 파란색
# 방향 : 우 좌 상 하
turn_limit = 1000
white, red, blue = 0, 1, 2
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
change_di = [1, 0, 3, 2]

size, unit_cnt = map(int, input().split())
board_color = [list(map(int, input().split())) for _ in range(size)]
board = [[[] for _ in range(size)] for _ in range(size)]
unit_info = []

for unit_num in range(unit_cnt):
    r, c, di = map(int, input().split())
    board[r-1][c-1].append(unit_num)
    unit_info.append((r-1, c-1, di-1))

print(newgame2())