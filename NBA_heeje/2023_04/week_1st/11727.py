# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 20분


n = int(input())
memo = [1]

# 메모이제이션 이용
# i가 홀수일 때 마지막 값에 2를 곱하고 1을 더한 값을,
# i가 짝수일 때 마지막 값에 2를 곱하고 1을 뺀 값을 반영해준다.  
for i in range(1, n):
    if i % 2:
        memo.append((memo[-1] * 2 + 1) % 10007)
    else:
        memo.append((memo[-1] * 2 - 1) % 10007)

print(memo[-1])