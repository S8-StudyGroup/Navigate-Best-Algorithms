# [BOJ] 5547. 일루미네이션
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
delta = {
    0: [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)],  # 짝수 행
    1: [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)],  # 홀수 행
}


def union():
    """_summary_
    건물로 둘러 싸여 있는 빈 공간을 모두 건물로 변환
    """

    def change_building(r, c):
        """
        건물로 둘러싸인 공간일 경우 건물로 변환
        """
        visited[r][c] = True
        is_building = True
        queue = [(r, c)]
        idx = 0

        while idx < len(queue):
            r, c = queue[idx]
            for dr, dc in delta[r % 2]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if matrix[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                else:
                    is_building = False

            idx += 1

        if is_building:
            for r, c in queue:
                matrix[r][c] = 1

    visited = [[False] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if not visited[row][col] and matrix[row][col] == 0:
                change_building(row, col)


def count_wall():
    """_summary_
    건물의 외곽에 있는 벽의 개수를 세어 출력
    """
    answer = 0
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 1:
                for dr, dc in delta[row % 2]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if matrix[nr][nc] == 0:
                            answer += 1
                    else:
                        answer += 1

    print(answer)


union()
count_wall()
