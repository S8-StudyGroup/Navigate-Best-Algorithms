# [Programmers] 92343. 양과 늑대
# 소요 시간 : 90분
# 구글 참고

def solution(info, edges):
    def dfs(sheep, wolf):
        
        # 양이 늑대보다 많다면 answer에 양의 수 저장
        if sheep > wolf:
            answer.add(sheep)
        else:
            return
        
        # 간선을 돌면서 이동가능한 새로운 곳 탐색
        for start, end in edges:
            if visited[start] and not visited[end]:
                visited[end] = 1
                if info[end] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[end] = 0
    
    # 중복 제거를 위해 set으로 설정
    answer = set()
    visited = [0] * len(info)
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)