# [BOJ] 1799. 비숍
# 소요 시간 : 00분

# # TRY 01
# size = int(input())
# board = [list(map(int, input().split())) for _ in range(size)]

# # 대각선 방문리스트 
# # diag1 : row + col == n
# # diag2 : row - col == n
# diag1 = {x: True for x in range(2 * size - 1)}
# diag2 = {y: True for y in range(- size + 1, size)}
# endr = endc = size - 1
# result = 0

# # n1 = row + col
# # n2 = row - col
# def dfs(row=0, col=0, n1=0, n2=0, cnt=0):
#     global result

#     # 종료조건
#     if row == endr and col == endc:
#         if board[row][col] == 1 and diag1[n1] and diag2[n2]:
#             cnt += 1
#         result = max(result, cnt)
#         return

#     # 비숍을 놓는 경우
#     if  diag1[n1] and diag2[n2] and board[row][col] == 1:
#         diag1[n1] = False
#         diag2[n2] = False

#         if col == endc:
#             dfs(row + 1, 0, row + 1, row + 1, cnt + 1)
#         else:
#             dfs(row, col + 1, n1 + 1, n2 - 1, cnt + 1)
        
#         diag1[n1] = True
#         diag2[n2] = True
    
#     # 비숍을 놓지 않는 경우
#     if col == endc:
#         dfs(row + 1, 0, row + 1, row + 1, cnt)
#     else:
#         dfs(row, col + 1, n1 + 1, n2 - 1, cnt)


# dfs()
# print(result)


# # TRY 02
# import sys

# size = int(input())
# board = [list(map(int, input().split())) for _ in range(size)]

# # 45도 회전 (시계방향으로)
# dboard = [[] for _ in range(2 * size - 1)]
# rc = []
# for r in range(size):
#     rc.append((r, 0))
# for c in range(1, size):
#     rc.append((size - 1, c))

# for idx in range(2 * size - 1):
#     r, c = rc[idx]
#     while r >= 0 and c < size:
#         dboard[idx].append((board[r][c], r - c))
#         r -= 1
#         c += 1

# # diag1 : row + col == n1
# # diag2 : row - col == n2
# diag2 = {y: True for y in range(- size + 1, size)}
# endn1 = 2 * size - 1
# maxVal = 2 * size - 2
# result = 0
# end = False

# def dfs(n1=0, cnt=0):
#     global result, end

#     # 종료조건
#     if n1 == endn1 and end:
#         result = max(result, cnt)
#         return
    
#     if cnt == maxVal:
#         result = maxVal
#         end = True
#         return
#         # print(maxVal)
#         # sys.exit(0)

    
#     for can, n2 in dboard[n1]:
#         if diag2[n2] and can == 1 and not end:
#             diag2[n2] == False
#             dfs(n1 + 1, cnt + 1)
#             diag2[n2] == True
           

#     else:
#         dfs(n1 + 1, cnt)

# dfs()
# print(result)



# TRY 03
size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]

# 45도 회전 (시계방향으로)
rboard = [[] for _ in range(2 * size - 1)]
rc = []
for r in range(size):
    rc.append((r, 0))
for c in range(1, size):
    rc.append((size - 1, c))

for idx in range(2 * size - 1):
    r, c = rc[idx]
    while r >= 0 and c < size:
        rboard[idx].append((board[r][c], r - c))
        r -= 1
        c += 1

# diag : row - col == n
diag = {n: True for n in range(- size + 1, size)}
# for i in rboard:
#     print(i)
# print(diag)

endn1 = 2 * size - 1
endn2 = 2 * size - 3

result1 = result2 = 0
way = []


def dfs(row, cnt=0):
    global result1, result2

    if row >= endn1:
        if row % 2 == 0:
            result1 = max(result1, cnt)
        else:
            result2 = max(result2, cnt)
        return

    for can, n in rboard[row]:
        if can and diag[n]:
            diag[n] = False
            dfs(row + 2, cnt + 1)
            diag[n] = True
    else:
        dfs(row + 2, cnt)


dfs(0)
dfs(1)
print(result1 + result2)