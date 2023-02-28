# [Programmers] 43163. 단어 변환
# 소요 시간 : 30분

# 프로그래머스 43163. 단어변환

from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    word_cnt = len(words)
    visited = [0] * word_cnt
    word_len = len(begin)

    used = deque()
    used.append([begin, 0])
    while used:
        now, cnt = used.popleft()

        if now == target:
            return cnt

        for i in range(word_cnt):
            if not visited[i]:
                diff = 0
                for j in range(word_len):
                    if now[j] != words[i][j]:
                        diff += 1
                else:
                    if diff == 1:
                        visited[i] = 1
                        used.append([words[i], cnt + 1])
    return 0