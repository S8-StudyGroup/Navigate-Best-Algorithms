# [BOJ] 14620. 꽃길
# 소요 시간 : 20분

# 꽃의 위치가 서로 간섭하는지 확인하는 함수
def is_not_conflict(flower_list, place):
    for flower in flower_list:
        # 맨헤튼 거리가 2를 넘지 않는다면 간섭하는 걸로 처리
        if abs(flower[0] - place[0]) + abs(flower[1] - place[1]) <= 2:
            return False
    return True


def dfs(flower_list, price):
    global min_price

    # 현재 가격이 최소 가격보다 크면 백트래킹
    if price >= min_price:  
        return
    
    # 꽃 3개의 위치를 모두 정했다면 최소 가격 비교 및 갱신
    if len(flower_list) == 3:
        min_price = min(min_price, price)
        return

    # 꽃의 위치가 서로 간섭하지 않는다면 해당 위치로 재귀 진행
    for i in range(N - 2):
        for j in range(N - 2):
            if is_not_conflict(flower_list, (i, j)):
                dfs(flower_list + [(i, j)], price + price_of_ground[i][j])


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

# 가로 N-2, 세로 N-2의 2차원 배열 생성 : 각 위치의 값은 해당 위치에서 꽃이 피었을 때 드는 비용을 뜻함
price_of_ground = [[ground[i][j] + ground[i][j - 1] + ground[i][j + 1] + ground[i - 1][j] + ground[i + 1][j] for j in range(1, N - 1)] for i in range(1, N - 1)]
min_price = 1e9

dfs([], 0)
print(min_price)