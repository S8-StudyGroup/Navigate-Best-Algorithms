# [BOJ] 17822. 원판 돌리기
# 소요 시간 : 00분
from collections import deque

# Input
N, M, rotate_cnt = map(int, input().split())
boards = [deque(map(int, input().split())) for _ in range(N)]
rotates = [tuple(map(int, input().split())) for _ in range(rotate_cnt)]


# 
for x, d, k in rotates:
    # 회전
    for i in range(x, N+1, x):
        if d == 0:
            boards[i-1].rotate(k)
        else:
            boards[i-1].rotate(-k)

    # 인접 체크
    del_list = []
    for i in range(N):
        for j in range(M):
            if boards[i][j] == 0:
                continue
            
            if boards[i][j] == boards[i][(j+1) % M]:
                del_list.append((i, j))
            elif boards[i][j] == boards[i][(j-1) % M]:
                del_list.append((i, j))
            elif i > 0 and boards[i][j] == boards[i-1][j]:
                del_list.append((i, j))
            elif i < N-1 and boards[i][j] == boards[i+1][j]:
                del_list.append((i, j))
    
    # 지우기
    if del_list:
        for i, j in del_list:
            boards[i][j] = 0
    
    # 평균 +- 1
    else:
        check_sum = 0
        check_cnt = 0
        for i in range(N):
            for j in range(M):
                if boards[i][j] > 0:
                    check_sum += boards[i][j]
                    check_cnt += 1

        if check_cnt > 0:
            average = check_sum / check_cnt
            for i in range(N):
                for j in range(M):
                    if boards[i][j] == average or boards[i][j] == 0:
                        continue
                    elif boards[i][j] > average:
                        boards[i][j] -= 1
                    else:
                        boards[i][j] += 1
    
    # print('==========debug============')
    # for dd in boards:
    #     print(dd)


# Output
print(sum(map(sum, boards)))