# [BOJ] 15656. N과 M (7)

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
귀하의 코드는 이미 잘 작성되어 있고 주어진 문제에 대해 효율적입니다. 그러나 몇 가지 사소한 최적화 및 개선이 가능합니다.

1. 함수 매개변수화:
전역 변수 "numbers"를 사용하는 대신 "dfs" 함수에 매개 변수로 전달하는 것이 좋습니다. 이렇게 하면 코드가 더 모듈화되고 이해하기 쉬워집니다.
2. 목록을 만드는 대신 생성기 표현식을 사용하세요.
**`sorted(list(map(int, input().split())))`**와 같은 목록 이해를 사용할 때 Python은 결과를 저장하기 위해 메모리에 새 목록을 만듭니다. 입력 크기가 크면 메모리 문제가 발생할 수 있습니다. 새 목록 생성을 방지하는 생성기 표현식을 대신 사용할 수 있습니다.
3. 재귀 대신 생성기 사용:
"dfs" 함수는 재귀를 사용하여 가능한 모든 조합을 생성합니다. 재귀는 작은 입력에는 잘 작동하지만 큰 입력에는 스택 오버플로 오류가 발생할 수 있습니다. 생성기 함수를 사용하여 재귀를 사용하지 않고 반복적으로 조합을 생성할 수 있습니다.
```
2. **개선 코드**
```python
def dfs(ans_list, numbers):
    if len(ans_list) == M:
        yield ans_list
    else:
        for number in numbers:
            yield from dfs(ans_list + [number], numbers)

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for ans_list in dfs([], numbers):
    print(*ans_list)
```

### 🌼 **도움되었던 내용**
sorted를 사용할 땐 list를 굳이 안 넣어도 된다!