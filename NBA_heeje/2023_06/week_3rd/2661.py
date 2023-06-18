# [BOJ] 2661. ⚾
# 소요 시간 : 90분

from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

# 0번 선수를 제외한 순열 생성
for hitters in permutations(range(1, 9), 8):

    # tuple을 list로 만들고, 3번째 인덱스에 0번 선수 삽입
    hitters = list(hitters)
    hitters.insert(3, 0)
    
    # hitter: 타자 인덱스, score: 현재 순열에 대한 점수
    hitter = 0
    score = 0
    inning = 0
    # 이닝
    for inning in innings:

        # out: 현재 이닝의 아웃 개수, diamond: n루 타석
        out = 0
        diamond = [False] * 3

        # 아웃이 3번 이하일 때
        while out < 3:
            hit = inning[hitters[hitter]]
            # 현재 이닝의 
            if hit != 0:
                for i in range(3):
                    if diamond[2 - i]:
                        # hit + 2 - i > 2:
                        if hit > i:
                            score += 1
                        else:
                            diamond[2 - i + hit] = True
                        diamond[2 - i] = False
                
                if hit == 4:
                    score += 1
                else:
                    diamond[hit - 1] = True
            else:
                out += 1
            
            hitter = (hitter + 1) % 9
    
    max_score = max(max_score, score)


print(max_score)