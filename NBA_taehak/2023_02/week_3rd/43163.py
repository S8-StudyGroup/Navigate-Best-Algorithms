# [Programmers] 43163. 단어 변환
# 소요 시간 : 30분

from collections import deque

def changable(a_word, b_word):
    cnt = 0
    for idx in range(len(a_word)):
        if a_word[idx] == b_word[idx]:
            continue
        else:
            cnt += 1
            if cnt > 1:
                return False
    return True

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    que = deque([(begin, 0)])

    while que:
        word, step = que.popleft()
        if word == target:
            answer = step
            break

        for next_word in words:
            if changable(word, next_word):
                que.append((next_word, step + 1))

    return answer