# [BOJ] 14391. 종이 조각
# 소요 시간 : 00분

# 0은 제자리, 1은 오른쪽, 2은 아래
def dfs(y:int, x:int, remain:int, numbers:list, dir:int) -> None:
    if remain == 0:
        print("S", numbers, visited)
        global max_sum
        if not numbers[-1]:
            numbers.pop()
        max_sum = max(max_sum, sum(list(map(int, numbers))))
        return
    
    numbers[-1] += matrix[y][x]
    visited[y][x] = True

    if y + 1 < N and not visited[y + 1][x]:

        if dir == 0:
            dfs(y + 1, x, remain - 1, numbers, 2)

            # numbers.append("")
            # dfs(y + 1, x, remain - 1, numbers, 0)
            # numbers.pop()

        if dir == 2:
            # numbers.append("")
            # dfs(y + 1, x, remain - 1, numbers, 0)
            # numbers.pop()

            dfs(y + 1, x, remain - 1, numbers, 2)

    if x + 1 < M and not visited[y][x + 1]:

        if dir == 0:
            dfs(y, x + 1, remain - 1, numbers, 1)

            # numbers.append("")
            # dfs(y, x + 1, remain - 1, numbers, 0)
            # numbers.pop()

        if dir == 1:
            # numbers.append("")
            # dfs(y, x + 1, remain - 1, numbers, 0)
            # numbers.pop()

            dfs(y, x + 1, remain - 1, numbers, 1)

    next_y, next_x = find_not_visited()
    numbers.append("")
    dfs(next_y, next_x, remain - 1, numbers, 0)
    numbers.pop()

    visited[y][x] = False
    print(y, x, remain, numbers, visited)
    numbers[-1] = numbers[-1][:-1]

def find_not_visited():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                return i, j

    return -1, -1
            
N, M = map(int, input().split())

matrix = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_sum = 0

dfs(0, 0, N * M, [""], 0)
print(max_sum)


# --- 시도 1 ---

# 가로의 합과 세로의 합 중 큰 것을 출력

# 이렇게 쉬울 리 없지..

# N, M = map(int, input().split())

# matrix = [input() for _ in range(N)]

# rotated_matrix = []
# for i in range(M):
#     row = ""
#     for j in range(N):
#         row += matrix[j][i]
#     rotated_matrix.append(row)

# row_sum = sum([int(matrix[i]) for i in range(N)])
# col_sum = sum([int(rotated_matrix[i]) for i in range(M)])

# print(max(row_sum, col_sum))