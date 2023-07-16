# [BOJ] 12100. 2048 (Easy)
# 소요 시간 : 00분

def moving(board:list):
    length = len(board)
    rotate_board = list(map(list, zip(*board)))
    new_board = [[], [], [], []]
    for line_num in range(length):
        line_list = [board[line_num], board[line_num][::-1], rotate_board[line_num], rotate_board[line_num][::-1]]
        for board_num in range(4):
            new_board[board_num].append([])
            nums = []
            for num in line_list[board_num]:
                if num != 0:
                    nums.append(num)
                if len(nums) == 2:
                    if nums[0] == nums[1]:
                        new_board[board_num][line_num].append(2*nums[0])
                        nums = []
                    else:
                        new_board[board_num][line_num].append(nums.pop(0))
            new_board[board_num][line_num] += nums
                    
            new_board[board_num][line_num] += [0 for _ in range(length - len(new_board[board_num][line_num]))]
    for i in range(length):
        new_board[1][i] = new_board[1][i][::-1]
        new_board[3][i] = new_board[3][i][::-1]
    new_board[2] = list(map(list, zip(*new_board[2])))
    new_board[3] = list(map(list, zip(*new_board[3])))
    return new_board

def easy2048(board:list, length:int, depth:int=0):
    if depth == 5:
        return True
    dir_list = moving(board)
    for dir in dir_list:
        if easy2048(dir, length, depth + 1):
            biggest = 0
            for i in range(length):
                for j in range(length):
                    if dir[i][j] > biggest:
                        biggest = dir[i][j]
            global max_biggest
            if max_biggest < biggest:
                max_biggest = biggest
    
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
max_biggest = 0
easy2048(board, n)
print(max_biggest)