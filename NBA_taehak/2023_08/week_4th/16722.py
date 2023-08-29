# [BOJ] 16722. 결! 합!
# 소요 시간 : 00분
from itertools import combinations


# Input
scb = [tuple(input().split()) for _ in range(9)]
game_cnt = int(input())
player_inputs = [tuple(input().split()) for _ in range(game_cnt)]


# check 합!
def is_hop(scb1, scb2, scb3):
    for idx in range(3):
        hop1 = scb1[idx] == scb2[idx] == scb3[idx]
        hop2 = scb1[idx] != scb2[idx] and scb1[idx] != scb3[idx] and scb2[idx] != scb3[idx]
        if not hop1 and not hop2:
            return False
    return True


# 조합 가능한 합! 들
cases = list(combinations(range(9), 3))
hop_set = set()
for a, b, c in cases:
    if is_hop(scb[a], scb[b], scb[c]):
        hop_set.add((a, b, c))


# player turn
score = 0
check_g = False
for player in player_inputs:
    if player[0] == 'H':
        hg, a, b, c = player
        abc = [int(a)-1, int(b)-1, int(c)-1]
        abc.sort()
        abc = tuple(abc)
        if abc in hop_set:
            hop_set.discard(abc)
            score += 1
        else:
            score -= 1
    else:
        if not check_g and len(hop_set) == 0:
            check_g = True
            score += 3
        else:
            score -= 1


# Output
print(score)