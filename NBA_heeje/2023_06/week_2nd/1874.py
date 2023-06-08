# [BOJ] 1874. 스택 수열
# 소요 시간 : 00분


def sol():
    answer = []
    is_impossible = False
    n = int(input())
    stack = []
    rear = 1
    for _ in range(n):
        x = int(input())
        while True:
            # count하는 숫자가 범위 밖으로 나가면
            if rear > n + 1:
                is_impossible = True
                break

            # stack이 비었거나 입력받은 숫자가 rear보다 더 크면
            elif not stack or x >= rear:
                answer.append("+")
                stack.append(rear)
                rear += 1

            # stack의 마지막 요소와 x가 일치한다면
            elif x == stack[-1]:
                answer.append("-")
                stack.pop()
                break

            else:
                is_impossible = True
                break

    return [] if is_impossible else answer


answer = sol()
if answer:
    print(*answer, sep="\n")
else:
    print("NO")
