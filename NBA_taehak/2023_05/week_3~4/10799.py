# [BOJ] 10799. 쇠막대기
# 소요 시간 : 00분

brackets = input()
answer = 0
stack = []
lazer = True

for bracket in brackets:
    if bracket == '(':
        lazer = True
        stack.append(bracket)
    else:
        if lazer:
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
        lazer = False

print(answer)