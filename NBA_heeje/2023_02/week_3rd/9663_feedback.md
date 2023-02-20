# [BOJ] 9663. N-Queen

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
이 코드에서는 백트래킹을 사용하여 퀸을 놓을 수 있는 경우를 찾아내고 있습니다. 하지만 이 코드에서는 백트래킹을 위한 코드와 퀸을 놓을 수 있는지 판단하는 코드가 섞여 있어서 가독성이 떨어집니다. 이 문제를 해결하려면, 퀸을 놓을 수 있는지 판단하는 코드를 별도의 함수로 분리해야 합니다.

또한, 현재 코드에서는 퀸을 놓은 후, 해당 퀸의 영향을 받는 칸을 체크하기 위해 8방향을 모두 체크하고 있습니다. 이러한 방식은 시간복잡도를 높일 수 있으므로, 퀸을 놓은 위치에서 해당 위치의 가로, 세로, 대각선 방향만 체크하도록 변경해야 합니다.

마지막으로, 전역 변수를 사용하는 것보다는 지역 변수를 사용하는 것이 좋습니다.
```
2. **개선 코드**
```python
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def check(x, y, n, board):
    # 가로, 세로 방향 체크
    for i in range(n):
        if board[x][i] == 1 or board[i][y] == 1:
            return False

    # 대각선 방향 체크
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:
                return False
            nx += dx[i]
            ny += dy[i]

    return True

def dfs(depth, n, board):
    if depth == n:
        return 1

    cnt = 0
    for i in range(n):
        if check(depth, i, n, board):
            board[depth][i] = 1
            cnt += dfs(depth + 1, n, board)
            board[depth][i] = 0

    return cnt

N = int(input())
board = [[0] * N for _ in range(N)]
print(dfs(0, N, board))
```

### 🌼 **도움되었던 내용**
함수별로 분리하는 작업에 대한 비중을 높여야겠다.