# [Programmers] 160585. 혼자서 하는 틱택토
# 소요 시간 : 90분

# from collections import Counter
# def solution(board):
#     count_o, count_x = 0, 0
#     for line in board:
#         counter = Counter(line)
#         temp_o, temp_x = counter["O"], counter["X"]
#         if temp_o == 3 or temp_x == 3:
#             return 0
#         count_o += temp_o
#         count_x += temp_x
#     if not 0 <= count_o - count_x < 2:
#         return 0
#     if count_o + count_x == 9:
#         return 0
#     for i in range(3):
#         if board[0][i] != "." and board[0][i] == board[1][i] == board[2][i]:
#             return 0
#     if board[0][0] != "." and board[0][0] == board[1][1] == board[2][2]:
#         return 0
#     if board[0][2] != "." and board[0][2] == board[1][1] == board[2][0]:
#         return 0
#     return 1
    


# def solution(board):
#     global win_o, win_x
#     temp = 1
#     win_x = False
#     win_o = False
#     cnt_o, cnt_x = 0, 0
#     for line in board:
#         for value in line:
#             globals()['value{}'.format(temp)] = value
#             temp += 1
#             if value == "O":
#                 cnt_o += 1
#             elif value == "X":
#                 cnt_x += 1
    
#     # 개수 확인
#     if cnt_x > cnt_o:
#         return 0
#     if cnt_o - cnt_x > 1:
#         return 0

#     # 빙고 확인
#     if value1 == value2 == value3 != ".":
#         check(value1)
#     if value4 == value5 == value6 != ".":
#         check(value4)
#     if value7 == value8 == value9 != ".":
#         check(value7)
#     if value1 == value4 == value7 != ".":
#         check(value1)
#     if value2 == value5 == value8 != ".":
#         check(value2)
#     if value3 == value6 == value9 != ".":
#         check(value3)
#     if value1 == value5 == value9 != ".":
#         check(value1)
#     if value3 == value5 == value7 != ".":
#         check(value3)
#     if win_o and win_x:
#         return 0
#     if win_o:
#         if cnt_o - cnt_x != 1:
#             return 0
#     if win_x:
#         if cnt_o != cnt_x:
#             return 0
#     return 1

# def check(value):
#     global win_o, win_x
#     if value == "O":
#         win_o = True
#     elif value == "X":
#         win_x = True


def solution(board):
    global win_o, win_x
    temp = 1
    win_x = False
    win_o = False
    cnt_o, cnt_x = 0, 0
    for line in board:
        for value in line:
            globals()['value{}'.format(temp)] = value
            temp += 1
            if value == "O":
                cnt_o += 1
            elif value == "X":
                cnt_x += 1
    
    # 개수 확인
    if cnt_x > cnt_o:
        return 0
    if cnt_o - cnt_x > 1:
        return 0

    # 빙고 확인
    check_bingo(value1, value2, value3)
    check_bingo(value4, value5, value6)
    check_bingo(value7, value8, value9)
    check_bingo(value1, value4, value7)
    check_bingo(value2, value5, value8)
    check_bingo(value3, value6, value9)
    check_bingo(value1, value5, value9)
    check_bingo(value3, value5, value7)

    if win_o and win_x:
        return 0
    if win_o:
        if cnt_o - cnt_x != 1:
            return 0
    if win_x:
        if cnt_o != cnt_x:
            return 0
    return 1

def check_bingo(value1, value2, value3):
    global win_o, win_x
    if value1 == value2 == value3 != ".":
        if value1 == "O":
            win_o = True
        elif value1 == "X":
            win_x = True


print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))