# [Programmers] 43163. 단어 변환

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
used에 이미 사용한 단어를 저장하고 있지만, 이미 큐에 추가한 단어를 확인하는 과정에서 중복을 체크하기 때문에 used를 제거할 수 있습니다.
모든 단어를 비교하는데, 단어의 길이가 50 이하이므로 가능한 모든 경우의 수는 50 x 50 = 2500개입니다. 따라서 가능한 모든 경우의 수를 미리 계산해 놓고, 이를 통해 단어 간의 차이를 O(1)로 계산할 수 있습니다. 이를 위해서는 각 단어를 인덱스와 매칭하는 딕셔너리를 만들면 됩니다.
```
2. **개선 코드**
```python
from collections import deque

def bfs(begin, target, words, diffs):
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        cur_word, level = queue.popleft()
        
        if cur_word == target:
            return level
        
        for word in words:
            if diffs[cur_word][word] == 1:
                queue.append((word, level + 1))
                del diffs[cur_word][word]
    
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0
    
    diffs = {}
    for word in words + [begin]:
        diffs[word] = {}
        for other_word in words + [begin]:
            if word == other_word:
                diffs[word][other_word] = 0
            else:
                diffs[word][other_word] = sum([1 for i in range(len(word)) if word[i] != other_word[i]])
    
    return bfs(begin, target, words, diffs)
```

### 🌼 **도움되었던 내용**
딱 한글자만 다른 단어를 찾는 작업을 이런 식으로 할 수도 있겠구나라는 것을 배웠다.