# [BOJ] 16722. 결! 합!
# 소요 시간 : 00분

from itertools import combinations

insp = lambda : input().split()
cards = [[]]
scb = [{"CIRCLE":1, "TRIANGLE":10, "SQUARE":100},{"YELLOW":1, "RED":10, "BLUE":100},{"GRAY":1, "WHITE":10, "BLACK":100}]

for _ in range(9):
    cards.append([dic[inp] for dic, inp in zip(scb, insp())])

h_cards = set()

for comb in [i for i in list(combinations([j for j in range(1,10)], 3))]:
    for i in list(map(sum, zip(*[cards[i] for i in comb]))):
        if i not in [3,30,300,111]:
            break
    else:
        h_cards.add(comb)

score = 0
gcall = False
for _ in range(int(input())):
    turn = insp()
    if turn[0] == "H":
        turn_tupl = tuple(map(int,sorted(turn[1:])))
        if turn_tupl in h_cards:
            score += 1
            h_cards.remove(turn_tupl)
        else:
            score -= 1
    else:
        if not h_cards and not gcall:
            score += 3
            gcall = True
        else:
            score -= 1

print(score)