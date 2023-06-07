# [BOJ] 1874. 스택 수열
# 소요 시간 : 60분


n = int(input())
# 실패 시
failed = False
# 스택
stack = []
# 결과 저장
result = []
# 입력값 저장
info = []
# 현재 들어갈 숫자
cur_num = 1
for _ in range(n):
    temp = int(input())
    info.append(temp)

for i in info:
    if failed:
        break
    # 넣는 숫자가 작은 경우
    while cur_num <= i:
        stack.append(cur_num)
        cur_num += 1
        result.append('+')
    # 넣을 숫자보다 결과 숫자가 큰 경우
    if cur_num > i:
        num = stack.pop()
        if i != num:
            failed = True
            break
        result.append('-')


if failed:
    print('NO')
else:
    for s in result:
        print(s)