# [Programmers] 1843. 사칙연산
# 소요 시간 : 00분

from collections import deque

def solution(arr):
    dq = deque(arr)
    stack = [deque()]
    
    while dq:
        number = int(dq.popleft())
        stack[-1].append(number)
        if dq:
            operator = dq.popleft()
            if operator == "-":
                stack.append(deque())
    l = len(stack)
    if l % 2 == 0:
        flag_max = False
    else:
        flag_max = True
    
    right_side = []

    while stack:
        left_side = stack.pop()
        if right_side:
            if flag_max:
                right_side = deque([(sum(left_side) - right_side.popleft()) + sum(right_side)])
            else:
                temp = left_side.pop() - sum(right_side)
                if temp >= 0:
                    right_side = left_side.append(temp)
                else:
                    right_side = deque([sum(left_side) + temp])

        else:
            right_side = left_side
        flag_max = not flag_max
    
    return right_side[-1]




print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))