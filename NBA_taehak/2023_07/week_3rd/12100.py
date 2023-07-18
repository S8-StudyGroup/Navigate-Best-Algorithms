# [BOJ] 12100. 2048 (Easy)
# 소요 시간 : 00분
from itertools import product
from copy import deepcopy

size = int(input())
board_0 = [list(map(int, input().split())) for _ in range(size)]


def sum_line(line, size=size):
    '''
    일차원 자료형 기준으로 왼쪽으로 이동시켰을 경우 결과
    @ ex) [2, 2, 4] => [4, 4, 0]
    '''
    answer = []
    memo = -1
    for num in line:
        if num == 0:
            continue
        elif memo == num:
            answer[-1] *= 2
            memo = -1
        else:
            answer.append(num)
            memo = num
    
    for _ in range(size - len(answer)):
        answer.append(0)
    
    return answer


def rotate_board(di, board):
    if di == 0:
        return board
    elif di == 1:
        return list(map(list, zip(*board[::-1])))
    elif di == 2:
        return list(map(lambda x : x[::-1], board))
    else:
        return list(map(list, zip(*board)))[::-1]


answer = 0
for case_2048 in product([0, 1, 2, 3], repeat=5):
    board = deepcopy(board_0)
    for di in case_2048:
        board = rotate_board(di, board)
        board = list(map(sum_line, board))
    answer = max(answer, (max(map(max, board))))


print(answer)