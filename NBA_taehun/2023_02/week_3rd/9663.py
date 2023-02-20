# [BOJ] 9663. N-Queen
# 소요 시간 : 70분
# 답안 확인

import sys
input = sys.stdin.readline

def adjacent(x): # x와 i가 같으면 행이 같다.
    for i in range(x): # 인덱스가 행, row[n]값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
            return False # 대각선이 같은 경우는 두 좌표에서 행 -행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
    return True

def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N): # i는 열 번호 0부터 N 전까지 옮겨가면서 유망한 곳 찾기
            row[x] = i
            if adjacent(x): # 행, 열, 대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x + 1)

N = int(input().strip())

row = [0] * N
result = 0
dfs(0)
print(result)
