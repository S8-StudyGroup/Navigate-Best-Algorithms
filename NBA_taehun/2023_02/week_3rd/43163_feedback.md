# [Programmers] 43163. 단어 변환

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.
1. 방문한 단어를 저장하는 리스트 대신, 집합으로 변경합니다. 집합은 검색에 있어서 더욱 빠릅니다.
2. 알파벳 차이를 검사하는 부분을 is_one_diff 함수로 따로 분리하였습니다.
3. enumerate 함수를 사용하지 않고, for loop과 zip 함수를 사용하여 코드를 더욱 간단하게 만들었습니다.
```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    # 방문한 단어를 저장하는 리스트 대신, 집합으로 변경
    visited = set()
    dq = deque([(begin, 0)])

    while dq:
        word, count = dq.popleft()

        for next_word in words:
            if next_word not in visited and is_one_diff(word, next_word):
                if next_word == target:
                    return count + 1
                dq.append((next_word, count + 1))
                visited.add(next_word)

    return 0

# 두 단어가 한 개의 알파벳만 다른지 확인하는 함수
def is_one_diff(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1
```

### 🌼 **도움되었던 내용**

3가지 변경사항 모두 도움이 되었습니다.

1. 방문 여부를 확인할 때 set 자료형 사용
2. 특정 기능을 하는 부분은 따로 함수로 분리
3. enumerate 대신 zip함수를 통해 서로 다른 두개의 글자 비교
