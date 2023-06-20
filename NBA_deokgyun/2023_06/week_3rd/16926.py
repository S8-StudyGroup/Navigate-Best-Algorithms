# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 00분

def sol(given_list, n, m, r):
    result_list = [[0 for _ in range(m)] for _ in range(n)]
    delta_list = [[0,1],[1,0],[0,-1],[-1,0]]
    t = min(n, m) // 2
    for k in range(t):
        tmp_list = []
        for j in range(k, m - k - 1):
            tmp_list.append(given_list[k][j])
        for i in range(k, n - k - 1):
            tmp_list.append(given_list[i][m - k - 1])
        for j in range(m - k - 1, k, -1):
            tmp_list.append(given_list[n - k - 1][j])
        for i in range(n - k - 1, k, -1):
            tmp_list.append(given_list[i][k])

        start = r % len(tmp_list)
        first = tmp_list[:start]
        second = tmp_list[start:]
        num_list = (second + first)[::-1]
        for j in range(k, m - k - 1):
            result_list[k][j] = num_list.pop()
        for i in range(k, n - k - 1):
            result_list[i][m - k - 1] = num_list.pop()
        for j in range(m - k - 1, k, -1):
            result_list[n - k - 1][j] = num_list.pop()
        for i in range(n - k - 1, k, -1):
            result_list[i][k] = num_list.pop()
        
    for line in result_list:
        print(*line)

n, m, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
sol(board, n, m, r)