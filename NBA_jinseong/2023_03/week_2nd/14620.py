# [BOJ] 14620. 꽃길
# 소요 시간 : 00분

def check(arr):
    global ans
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    now_price = 0

    while arr:
        num = arr.pop()
        i = num // (N - 2) + 1
        j = num % (N - 2) + 1
        # 안 겹칠 경우 계속 진행, cnt += 1 => cnt = 3이면 답 비교
        if not visited[i][j] and not visited[i - 1][j] and not visited[i + 1][j] and not visited[i][j + 1] and not visited[i][j - 1]:
            visited[i][j] = True
            visited[i - 1][j] = True
            visited[i + 1][j] = True
            visited[i][j + 1] = True
            visited[i][j - 1] = True
            cnt += 1
            now_price += price_grid[i][j] + price_grid[i - 1][j] + price_grid[i + 1][j] + price_grid[i][j - 1] + price_grid[i][j + 1]
    if cnt == length:
        if now_price < ans:
            ans = now_price
    return


def combination(arr, start):
    if len(arr) == length:
        check(arr[:])
        return
    for i in range(start, len(numbers)):
        arr.append(numbers[i])
        combination(arr, i + 1)
        arr.pop()


N = int(input())
price_grid = [list(map(int, input().split())) for _ in range(N)]
ans = 3000

numbers = [i for i in range((N-2)**2)]
length = 3

combination([], 0)

print(ans)


