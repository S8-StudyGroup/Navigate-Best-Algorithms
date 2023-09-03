# [BOJ] 20061. 모노미노도미노 2
# 소요 시간 : 00분
from pprint import pprint
gboard = [[0]*4 for _ in range(6)]
bboard = [[0]*6 for _ in range(4)]

score = 0

for _ in range(int(input())):
    t, row, col = map(int, input().split())

    g,b = False, False
    for i in range(5, -1, -1):
        if not g:
            if t in [1,3] and gboard[i][col] == 0:
                gboard[i][col] = 1
                if t == 3:
                    gboard[i-1][col] = 1
                g = True
            elif t == 2 and (gboard[i][col] == 0 and gboard[i][col+1] == 0):
                gboard[i][col], gboard[i][col+1] = 1, 1
                g = True
        if not b:
            if t in [1,2] and bboard[row][i] == 0:
                bboard[row][i] = 1
                if t == 2:
                    bboard[row][i-1] = 1
                b = True
            elif t == 3 and (bboard[row][i] == 0 and bboard[row+1][i] == 0):
                bboard[row][i], bboard[row+1][i] = 1, 1
                b = True
        if g and b:
            break
    
    glines, blines = [], []
    for i in range(5, 3, -1):
        gline = []
        bline = []
        for j in range(4):
            gline.append(gboard[i][j])
            bline.append(bboard[j][i])
        if min(gline):
            glines.append(True)
        else:
            glines.append(False)
        if min(bline):
            blines.append(True)
        else:
            blines.append(False)
    
    for d in range(2):
        if glines[d]:
            gboard.pop(5-d)
            gboard = [[0] * 4] + gboard
            score += 1

    for d in blines:
        if blines[d]:
            for i in range(4):
                bboard[i].pop(5-d)
                bboard[i] = [0] + bboard[i]
            score += 1

    glines, blines = [False] * 2, [False] * 2
    for i in range(2):
        for j in range(4):
            if not glines[i] and gboard[i][j] == 1:
                glines[i] = True
            if not blines[i] and bboard[j][i] == 1:
                blines[i] = True
            if glines[i] and blines[i]:
                break
    
    for gline, bline in zip(glines, blines):
        if gline:
            gboard.pop()
            gboard = [[0] * 4] + gboard
        if bline:
            for i in range(4):
                bboard[i].pop()
                bboard[i] = [0] + bboard[i]

cnt = 0
for i in range(6):
    for j in range(4):
        cnt += gboard[i][j] + bboard[j][i]

print(score, cnt)
pprint(gboard)
pprint(bboard)