# [BOJ] 20923. 숫자 할리갈리 게임
# 소요 시간: 70분

import sys
from collections import deque
input = sys.stdin.readline

def initialize_ground():
    global suyeon_ground, dodo_ground
    suyeon_ground = deque()
    dodo_ground = deque()

def ring():

    if dodo_ground and suyeon_ground and dodo_ground[-1] + suyeon_ground[-1] == 5:
        # dodo_ground.reverse()
        # suyeon_ground.reverse()
        suyeon_deck.extendleft(dodo_ground)
        suyeon_deck.extendleft(suyeon_ground)
        initialize_ground()

    if (dodo_ground and dodo_ground[-1] == 5) or (suyeon_ground and suyeon_ground[-1] == 5):
        # suyeon_ground.reverse()
        # dodo_ground.reverse()
        dodo_deck.extendleft(suyeon_ground)
        dodo_deck.extendleft(dodo_ground)
        initialize_ground()
    
    if cnt == M:
        return True

    return False



N, M = map(int, input().split())
dodo_deck = deque()
dodo_ground = deque()
suyeon_deck = deque()
suyeon_ground = deque()
cnt = 0

for _ in range(N):
    card1, card2 = map(int, input().split())
    dodo_deck.append(card1)
    suyeon_deck.append(card2)

while True:
    dodo_ground.append(dodo_deck.pop())
    if not dodo_deck:
        break
    cnt += 1
    if ring():
        break

    suyeon_ground.append(suyeon_deck.pop())
    if not suyeon_deck:
        break
    cnt += 1
    if ring():
        break

if len(dodo_deck) > len(suyeon_deck):
    print("do")
elif len(dodo_deck) < len(suyeon_deck):
    print("su")
else:
    print("dosu")