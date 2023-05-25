# [BOJ] 20365. 블로그2
# 소요 시간 : 10분

# 색깔이 변할 때마다 카운트
# 두 색깔 중 적게 나온것 + 1

N = int(input())
problems = input()
colors = [0, 0]
last = ""

for problem in problems:
    if problem == "B" and last != "B":
        colors[0] += 1
        last = "B"
    elif problem == "R" and last != "R":
        colors[1] += 1
        last = "R"

print(min(colors) + 1)