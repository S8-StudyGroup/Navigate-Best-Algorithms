# [BOJ] 2661. 좋은수열
# 소요 시간 : 00분


def dfs(n, numbers):
    global answer

    # 좋은 수열이 아니거나 답이 정해진 경우
    if not is_good(numbers) or answer:
        return

    # 좋은 수열이면서 길이가 N일 경우
    if n == N:
        answer = numbers
        return

    for i in ["1", "2", "3"]:
        dfs(n + 1, numbers + i)


def is_good(numbers):
    for i in range(2, len(numbers) + 1, 2):
        for j in range(len(numbers) - i + 1):
            if numbers[j : j + (i // 2)] == numbers[j + (i // 2) : j + i]:
                return False
    return True


N = int(input())
answer = ""

dfs(0, "")
print(answer)
