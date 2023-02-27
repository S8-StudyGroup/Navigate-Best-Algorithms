# [BOJ] 9663. N-Queen
# 소요 시간 : 30분

def check(row=0):
    global size, answer

    if row >= size:
        return

    for col in range(size):

        if cols[col] or di_1[row+col] or di_2[size+row-col]:
            continue

        cols[col] = True
        di_1[row+col] = True
        di_2[size+row-col] = True

        check(row + 1)

        cols[col] = False
        di_1[row+col] = False
        di_2[size+row-col] = False

        if row == size - 1:
            answer += 1
    


size = int(input())

answer = 0
rows = [False] * size
cols = [False] * size
di_1 = [False] * (2 * size)     # row + col = idx
di_2 = [False] * (2 * size)     # size + row - col = idx

check()

print(answer)