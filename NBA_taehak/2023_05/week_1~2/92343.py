# [Programmers] 92343. 양과 늑대
# 소요 시간 : 00분
answer = 0
def solution(info, edges):
    visited = [False] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)
        else:
            return 
        
        for parent, child in edges:
            # 갈수 있는 곳 == 부모는 방문했고 자식은 방문 안했을때 자식노드로 진행 가능
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = False

    visited[0] = True
    dfs(1, 0)

    return answer