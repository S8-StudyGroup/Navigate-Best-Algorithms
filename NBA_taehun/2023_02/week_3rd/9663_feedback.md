# [BOJ] 9663. N-Queen

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.
adjacent 함수는 입력으로 현재까지 퀸을 놓은 위치를 담은 리스트 row와 새로운 퀸을 놓을 위치 x를 받아 열이 같거나 대각선에 위치하는지를 확인합니다. 이 때 all 내장 함수와 제너레이터 표현식을 사용하여 False를 반환하는 경우가 있는지 확인합니다.
dfs 함수는 입력으로 row 리스트, 행 번호 x, 체스판의 크기 N, 결과값을 담은 리스트 result를 받습니다. 이 함수에서는 결과값 result가 전역 변수로 선언되지 않고 매개변수로 전달됩니다. 이를 통해 함수 호출 스택에 있는 모든 dfs 함수가 동일한 리스트 result를 참조하므로, 함수 내에서 값을 변경하여도 올바른 결과값이 반환됩니다.
dfs 함수의 호출 코드는 n_queens 함수 내부에 포함됩니다. 이 때, result를 리스트로 전달해야 하므로 result 변수가 스칼라에서 리스트로 변경되었습니다. 함수 호출 코드에서는 result[0]의 값을 반환합니다.
```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.
def adjacent(row, x):
    # 열이 같거나 대각선에 위치하는지 확인
    return all(abs(row[i] - row[x]) not in (0, x - i) for i in range(x))

def dfs(row, x, N, result):
    if x == N:
        result[0] += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(row, x):
                dfs(row, x + 1, N, result)

def n_queens(N):
    result = [0]
    row = [0] * N
    dfs(row, 0, N, result)
    return result[0]

N = int(input().strip())
print(n_queens(N))
```

### 🌼 **도움되었던 내용**
