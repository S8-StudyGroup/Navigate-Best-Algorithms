# [Programmers] 43163. 단어 변환
# 소요 시간 : 30분

from collections import deque


def bfs(begin, target, words):
    used = set()
    used.add(begin)
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        cur_word, level = queue.popleft()
        
        # 현재 단어가 타겟과 일치하면 단계 반환
        if cur_word == target:
            return level
        
        # 이미 사용한 단어는 패스
        for word in words:
            if word in used:
                continue;
                
            cnt = 0
            for i in range(len(word)):
                if cur_word[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                used.add(word)
                queue.append((word, level + 1))
    
    # 타겟과 일치할 수 없다면 0 반환
    return 0

def solution(begin, target, words):
    
    # target이 words에 없다면 0 반환
    if target not in words:
        return 0
    
    return bfs(begin, target, words)