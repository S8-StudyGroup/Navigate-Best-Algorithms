# [BOJ] 3678. 카탄의 개척자
# 소요 시간 : 00분
case_cnt = int(input())
targets = [int(input()) for _ in range(case_cnt)]


target_max = max(targets)
board = [1, 2, 3, 4, 5, 2, 3, 1]

nums = {x: 0 for x in range(1, 6, 1)}
for i in board:
    nums[i] += 1


def get_new_num(excepts):
    sorted_nums = sorted(nums.items(), key= lambda x: (x[1], x[0]))
    for num, cnt in sorted_nums:
        if num not in excepts:
            nums[num] += 1

            # print('sorted_nums :', sorted_nums)
            # print('excepts :', excepts)
            # print('get new number ================ num :', num)
            # print()

            return num


cycle = hexa = 1
num = 8

while num <= target_max:

    if hexa == 6:
        except_nums = []
        except_nums.append(board[num-1])
        except_nums.append(board[num - 6*cycle - hexa])
        except_nums.append(board[num - 6*cycle - hexa + 1])
        # print('hexa6 꼭지점---------')
        # print(num, cycle, hexa)
        board.append(get_new_num(except_nums))
        num += 1

        # print('hexa6 첫번째지점---------')
        # print(num, cycle, hexa)
        # print(num-1)
        # print(num - 6*cycle - hexa)
        except_nums = []
        except_nums.append(board[num-1])
        except_nums.append(board[num - 6*cycle - hexa])
        board.append(get_new_num(except_nums))
        num += 1

    else:
        except_nums = []
        except_nums.append(board[num-1])
        except_nums.append(board[num - 6*cycle - hexa])
        # print('꼭지점---------')
        # print(num, cycle, hexa)
        board.append(get_new_num(except_nums))
        num += 1

    for idx in range(cycle):

        # print('사잇값---------')
        # print(num, cycle, hexa)

        except_nums = []
        except_nums.append(board[num-1])
        except_nums.append(board[num - 6*cycle - hexa])
        except_nums.append(board[num - 6*cycle - hexa - 1])
        board.append(get_new_num(except_nums))
        num += 1

    # 다음 사이클
    hexa += 1

    if hexa == 7:
        cycle += 1
        hexa = 1


for target in targets:
    print(board[target-1])