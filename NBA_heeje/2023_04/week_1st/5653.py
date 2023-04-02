# [SWEA] 5653. 줄기세포배양
# 소요 시간 : 00분

def breeding() -> None:
    """
    줄기세포들이 번식하는 동작을 위한 함수
    """

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    # 번식된 줄기 세포를 임시 저장해놓는 dictionary
    add_cell_info = {}

    for key, cell in cell_info.items():

        # 죽은 세포
        if cell[1] == 0:
            continue
        
        # 비활성화 세포
        if cell[1] > cell[0]:
            cell[1] -= 1

        # 활성화 세포
        else:
            cell[1] -= 1

            # 번식
            for d in range(4):
                move_y, move_x = key[0] + dy[d], key[1] + dx[d]

                # 해당 방향에 이미 줄기세포가 있는 경우
                if cell_info.get((move_y, move_x)):
                    continue
                
                # 해당 방향에 줄기세포가 없는 경우
                else:

                    # 동시 번식
                    if add_cell_info.get((move_y, move_x)):
                        add_cell_info[(move_y, move_x)] = max(add_cell_info[(move_y, move_x)], cell[0])
                    
                    # 단일 번식
                    else:
                        add_cell_info[(move_y, move_x)] = cell[0]
    
    # 현 시간에 번식된 세포 반영
    for add_key, add_cell in add_cell_info.items():
        cell_info[add_key] = [add_cell, add_cell * 2]


def total_of_alive_cells() -> None:
    """
    비활성화 또는 활성화된 세포의 개수를 세는 함수
    """
    
    total = 0
    for cell in cell_info.values():
        if cell[1] != 0:
            total += 1
    
    return total


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell_info = {}

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] != 0:
                cell_info[(i, j)] = [row[j], row[j] * 2]
    
    for _ in range(K):
        breeding()
    
    print(f"#{tc} {total_of_alive_cells()}")
        