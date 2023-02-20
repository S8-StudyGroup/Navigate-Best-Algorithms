# [Programmers] 43163. 단어 변환
# 소요 시간 : 30분

from collections import deque

def solution(begin, target, words):
    # 불가능한 경우
    if target not in words:
        return 0
    visited = [False] * len(words)
    dq = deque([(begin, 0)])
    while dq:
        word, count = dq.popleft()
        for idx, next_word in enumerate(words):
            if not visited[idx]:
                # 한 개의 알파벳만 다른지 확인
                cnt = 0
                for i in range(len(begin)):
                    if word[i] != next_word[i]:
                        cnt += 1
                    if cnt > 1:
                        break
                else:
                    if next_word == target:
                        return count + 1
                    dq.append((next_word, count + 1))
                    visited[idx] = True


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))