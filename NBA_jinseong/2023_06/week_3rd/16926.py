# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 00분


N, M, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
# 가장자리부터 돔
def rotate(cnt):
    if cnt == 0:
        return
    for k in range(min(N, M) // 2):
        i_range = N - k
        j_range = M - k
        before = array[k][k]
        # 왼쪽 변
        for i in range(k + 1, i_range):
            temp = array[i][k]
            array[i][k] = before
            before = temp
        # 밑변
        for j in range(k + 1, j_range):
            temp = array[N - k - 1][j]
            array[N - k - 1][j] = before
            before = temp
        # 오른쪽 변
        for i in range(i_range - 2, k - 1, -1):
            temp = array[i][M - k - 1]
            array[i][M - k - 1] = before
            before = temp
        # 윗변
        for j in range(j_range - 2, k - 1, -1):
            temp = array[k][j]
            array[k][j] = before
            before = temp
    rotate(cnt - 1)

rotate(R)

for i in range(N):
    print(*array[i])

