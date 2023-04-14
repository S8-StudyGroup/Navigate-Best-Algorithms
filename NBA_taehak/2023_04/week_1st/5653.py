# [SWEA] 5653. 줄기세포배양
# 소요 시간 : 00분
from collections import defaultdict


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def spread(cell):
    '''
    '''
    row, col = cell
    life_time, state, inactive_time, active_time = cells[cell]

    # 죽은 세포
    if state == 0:
        dead_cells.add(cell)
        return

    # 비활성화 상태
    elif state == 1:
        if inactive_time < life_time:
            next_step[cell] = [life_time, state, inactive_time + 1, active_time]
            return
        else:
            next_step[cell] = [life_time, 2, inactive_time, active_time]
            return
    
    # 활성화 상태
    elif state == 2:
        # spread
        if active_time == 1: 
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if (nr, nc) not in cells and (nr, nc) not in dead_cells:
                    if (nr, nc) in next_step:
                        next_step[(nr, nc)] = [max(next_step[(nr, nc)][0], life_time), 1, 1, 1]
                    else:
                        next_step[(nr, nc)] = [life_time, 1, 1, 1]


        if active_time < life_time:
            next_step[cell] = [life_time, state, inactive_time, active_time + 1]
            return
        else:
            next_step[cell] = [life_time, 0, inactive_time + 1, active_time]
            return


for case_num in range(1, int(input()) + 1):
    row_size, col_size, times = map(int, input().split())

    # {(row, col) : [life_time, state, inactive_time, active_time]}
    # state : 0: 죽음, 1: 비활성화, 2: 활성화
    cells = defaultdict(tuple)
    dead_cells = set()
    
    for row_idx in range(row_size):
        for col_idx, active_time in enumerate(map(int, input().split())):
            if active_time == 0:
                continue
            cells[(row_idx, col_idx)] = [active_time, 1, 1, 1]

    for time in range(times):
        next_step = defaultdict(tuple)
        for cell in cells:
            spread(cell)
        cells = next_step

    result = 0
    for cell, info in cells.items():
        active_time, state, inactive_time, active_time = info
        if state > 0:
            result += 1

    print(f'#{case_num} {result}')