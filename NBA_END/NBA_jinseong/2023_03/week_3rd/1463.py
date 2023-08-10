# [BOJ] 1463. 1로 만들기
# 소요 시간 : 00분

N = int(input())

answers = [0, 0]

for num in range(2, N+1):
    candi = []
    if num % 3 == 0:
        candi.append(answers[num // 3])
    if num % 2 == 0:
        candi.append(answers[num // 2])
    candi.append(answers[num-1])
    answers.append(min(candi) + 1)

print(answers[N])
