# [BOJ] 10799. 쇠막대기
# 소요 시간 : 30분
bar_info = input()

pieces = 0
stack_cnt = 0
is_point = False

while len(bar_info) > 0:
    temp = bar_info[0]
    bar_info = bar_info[1:]
    if temp == '(':
        stack_cnt += 1
        is_point = True
    elif temp == ')':
        stack_cnt -= 1
        if is_point:
            pieces += stack_cnt
            is_point = False
        else:
            pieces += 1
print(pieces)



