# [BOJ] 20923. 숫자 할리갈리 게임
# 소요 시간 : 50분(시간초과) + 30분
import sys
from collections import deque

card_num, turns = map(int, sys.stdin.readline().split())
do_deck, su_deck = deque(), deque()
do_ground, su_ground = deque(), deque()
for t in range(card_num):
    do_card, su_card = map(int, sys.stdin.readline().split())
    do_deck.append(do_card)
    su_deck.append(su_card)


def start():
    global turns
    do_index = turns % 2
    while turns > 0:
        # 행동
        # do
        if turns % 2 == do_index:
            do_turn = do_deck.pop()
            do_ground.append(do_turn)
        # su
        else:
            su_turn = su_deck.pop()
            su_ground.append(su_turn)
        # 판별
        if checked():
            return
        bell()
        turns -= 1
    if len(do_deck) == len(su_deck):
        print('dosu')
        return
    elif len(do_deck) > len(su_deck):
        print('do')
        return
    elif len(do_deck) < len(su_deck):
        print('su')
        return


def bell():
    global do_ground, su_ground
    # su win
    if do_ground and su_ground:
        if do_ground[-1] + su_ground[-1] == 5:
            su_deck.extendleft(do_ground)
            do_ground = deque()
            su_deck.extendleft(su_ground)
            su_ground = deque()
    # do win
    if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
        do_deck.extendleft(su_ground)
        su_ground = deque()
        do_deck.extendleft(do_ground)
        do_ground = deque()


def checked():
    if len(su_deck) == 0:
        print('do')
        return True
    elif len(do_deck) == 0:
        print('su')
        return True
    return False


start()