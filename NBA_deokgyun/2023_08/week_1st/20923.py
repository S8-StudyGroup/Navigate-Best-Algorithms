# [BOJ] 20923. 숫자 할리갈리 게임
# 소요 시간 : 00분

from sys import stdin
from collections import deque

readline = stdin.readline

card_cnt, game_cnt = map(int, readline().split())

do_card = deque([])
su_card = deque([])
for _ in range(card_cnt):
    do, su = map(int, readline().split())
    do_card.append(do)
    su_card.append(su)

do_ground, su_ground = deque([]), deque([])
game_going = 0
while do_card and su_card:
    game_going += 1

    if game_going & 1:
        do_ground.appendleft(do_card.pop())
        if not do_card:
            break
    else:
        su_ground.appendleft(su_card.pop())
        if not su_card:
            break

    if do_ground and su_ground and do_ground[0] + su_ground[0] == 5:
        su_card.extendleft(do_ground)
        su_card.extendleft(su_ground)
        do_ground, su_ground = deque([]), deque([])
    if (do_ground and do_ground[0] == 5) or (su_ground and su_ground[0] == 5):
        do_card.extendleft(su_ground)
        do_card.extendleft(do_ground)
        do_ground, su_ground = deque([]), deque([])

    if game_going == game_cnt:
        break

result = len(do_card) - len(su_card)

print("do" if result > 0 else ("dosu" if result == 0 else "su"))