# [BOJ] 17178. 줄서기
# 소요 시간 : 00분


# Input
line_cnt = int(input())
tickets = []
for line in range(line_cnt):
    tickets.extend(input().split())

# 정렬
tickets_sorted = sorted(tickets, key=lambda x: (x[0], int(x[2:])), reverse=True)
tickets = tickets[::-1]

# 
waiting = []
answer = 'GOOD'

while tickets_sorted:
    next_enter = tickets_sorted.pop()

    while True:
        if waiting and waiting[-1] == next_enter:
            waiting.pop()
            break
        if tickets and tickets[-1] == next_enter:
            tickets.pop()
            break

        if tickets and tickets[-1] != next_enter:
            if len(waiting) < 5:
                waiting.append(tickets.pop())
                continue
            else:
                answer = 'BAD'
                break
        
        answer = 'BAD'
        break


    if answer == 'BAD':
        break

print(answer)

