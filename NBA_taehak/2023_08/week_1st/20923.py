# [BOJ] 20923. 숫자 할리갈리 게임
# 소요 시간 : 00분
import sys
from collections import deque
input = sys.stdin.readline

# Input
card_cnt, turn_limit = map(int, input().split())
do_card = deque()
su_card = deque()
for _ in range(card_cnt):
    d, s = map(int, input().split())
    do_card.append(d)
    su_card.append(s)

# 
do_ground = deque()
su_ground = deque()


def bell():
    if do_ground and su_ground and do_ground[-1] + su_ground[-1] == 5:
        su_card.extendleft(do_ground)
        su_card.extendleft(su_ground)
        su_ground.clear()
        do_ground.clear()
        return

    if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
        do_card.extendleft(su_ground)
        do_card.extendleft(do_ground)
        su_ground.clear()
        do_ground.clear()
        return


def game(turn_limit=turn_limit):
    turn = 0

    while True:
        do_ground.append(do_card.pop())
        if not do_card: return 'su'
        bell()
        turn += 1
        if turn == turn_limit: break

        su_ground.append(su_card.pop())
        if not su_card: return 'do'
        bell()
        turn += 1
        if turn == turn_limit: break

    if len(su_card) > len(do_card):
        return 'su'
    elif len(su_card) < len(do_card):
        return 'do'
    else:
        return 'dosu'


print(game())