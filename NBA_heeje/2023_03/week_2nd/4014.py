# [SWEA] 4014. 활주로 건설
# 소요 시간 : 20분


def airstrip_counter(ground):
    cnt_airstrip = 0

    for i in range(N):

        # 기준 및 해당 기준 땅의 길이 지정
        pre = ground[i][0]
        cnt = 1

        # 활주로 가능 후보
        is_possible = True

        for j in range(1, N):
            if is_possible:

                # 기준과 같은 높이라면 개수 + 1
                if ground[i][j] == pre:
                    cnt += 1
                
                # 기준보다 높이가 1 높다면 
                elif ground[i][j] - pre == 1:

                    # 길이가 경사로 길이보다 길거나 같다면 경사로 설치 및 기준, 길이 변경
                    if cnt >= X:
                        pre = ground[i][j]
                        cnt = 1
                    
                    # 길이가 경사로 길이보다 짧다면 활주로 불가
                    else:
                        break
                
                # 기준보다 높이가 1 낮다면 활주로 가능 후보를 False로 두고 해당 지형의 길이를 세보자
                elif ground[i][j] - pre == -1:
                    is_possible = False
                    pre = ground[i][j]
                    cnt = 1

                # 기준과의 높이 차이가 2 이상이라면 활주로 불가
                else:
                    break
            
            # 활주로 가능 후보가 False라면
            else:
                
                # 기준과 현재 땅의 높이가 같다면 길이 + 1
                if ground[i][j] == pre:
                    cnt += 1
                
                # 다르면 활주로 불가 확정
                else:
                    break
            
            # 활주로 가능 후보가 False인데 해당 땅의 길이가 경사로 길이와 같다면
            if not is_possible and X == cnt:
                
                # 활주로 가능 후보 True 및 길이 초기화
                is_possible = True
                cnt = 0

        # 해당 지형이 활주로로 가능하다고 판별
        else:
            if is_possible:
                cnt_airstrip += 1

    return cnt_airstrip


T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    
    # list(zip(*ground)) : 전치행렬
    print(f"#{tc} {airstrip_counter(ground) + airstrip_counter(list(zip(*ground)))}")
