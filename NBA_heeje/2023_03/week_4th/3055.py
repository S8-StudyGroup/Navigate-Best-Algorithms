# [BOJ] 3055. 탈출
# 소요 시간 : 00분


def move_hedgehog_validator(y:int, x:int) -> bool:
    """
    해당 칸이 고슴도치가 움직일 수 있는 함수
    """

    return 0 <= y < R and 0 <= x < C and (y, x) not in visited and matrix[y][x] in [".", "D"]


def move_hedgehog() -> int or list:
    """
    고슴도치를 움직이는 함수
    """
    if not move_q:
        return -1
    
    # 현재 move_q 안에 들어있는 개수만큼만 진행
    for _ in range(len(move_q)):
        y, x = move_q.pop(0)

        # 비버 굴에 도달하면 1 반환
        if matrix[y][x] == "D":
            return 1

        # 고슴도치가 갈 수 있는 곳 저장
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if move_hedgehog_validator(move_y, move_x):
                visited.add((move_y, move_x))
                move_q.append((move_y, move_x))
    
    # 개수만큼 진행했다면 0 반환
    return 0

def filled_water_validator(y:int, x:int) -> bool:
    """
    해당 칸이 물을 확장할 수 있는 칸인지 검사하는 함수
    """
    return 0 <= y < R and 0 <= x < C and matrix[y][x] == "."


def filled_water() -> None:
    """
    물을 비어있는 칸으로 확장하는 함수
    """
    
    # 물을 채워야 할 칸을 저장할 set
    filled_water_list = set()

    # 물을 보면 인접한 부분에 대하여 set에 추가
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == "*":
                for d in range(4):
                    move_y, move_x = y + dy[d], x + dx[d]
                    if filled_water_validator(move_y, move_x):
                        filled_water_list.add((move_y, move_x))
    
    # filled_water_list에 저장된 좌표를 모두 물로 변환
    for y, x in filled_water_list:
        matrix[y][x] = "*"

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

R, C = map(int, input().split())
matrix = []
visited = set()
move_q = []

for i in range(R):
    row = list(input())

    for j in range(C):
        if row[j] == "S":
            visited.add((i, j))
            move_q.append((i, j))

    matrix.append(row)

min_time = 0
while True:
    filled_water()
    can_move = move_hedgehog()

    # 비버 굴에 도달하지 못하는 경우
    if can_move == -1:
        print("KAKTUS")
        break

    # 비번 굴에 도달하는 경우
    elif can_move == 1:
        print(min_time)
        break

    min_time += 1