// [BOJ] 3055. 탈출
// 소요 시간 : 00분

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
    static int[] dx = {-1, 0, 1, 0}; // 상하좌우 이동을 위한 dx, dy 배열
    static int[] dy = {0, 1, 0, -1};
    static int[][] dist; // 각 지점까지의 최단 거리를 저장할 배열
    static int n, m;
    static char[][] board;

    static class Three {
        int x;
        int y;
        int z;
    
        Three(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        board = new char[n][m];
        dist = new int[n][m];
        int startX = 0, startY = 0, goalX = 0, goalY = 0;
        Queue<Three> queue = new LinkedList<>(); 

        // 지도 입력
        for (int i = 0; i < n; i++) {
            board[i] = sc.next().toCharArray();
            for (int j = 0; j < m; j++) {
                dist[i][j] = -1;
                if (board[i][j] == 'S') {
                    startX = i;
                    startY = j;
                    dist[i][j] = 0;
                } else if (board[i][j] == 'D') {
                    goalX = i;
                    goalY = j;
                } else if (board[i][j] == '*') {
                    queue.add(new Three(i, j, 1)); 
                }
            }
        }
        
        queue.add(new Three(startX, startY, 2));

        while (!queue.isEmpty()) {
            Three p = queue.remove();
            int x = p.x;
            int y = p.y;
            int z = p.z;
            if (z == 1) {
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                        if (board[nx][ny] == '.' || board[nx][ny] == 'S') {
                            board[nx][ny] = '*';
                            queue.add(new Three(nx, ny, 1));
                        }
                    }
                }
                continue;
            } else {
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if (nx >= 0 && nx < n &&ny >= 0 && ny < m) {
                        if (board[nx][ny] == '.' || board[nx][ny] == 'D') {
                            if (board[nx][ny] == 'D') {
                                System.out.println(dist[x][y] + 1); 
                                return;
                            }
                            board[nx][ny] = 'S';
                            dist[nx][ny] = dist[x][y] + 1;
                            queue.add(new Three(nx, ny, 2));
                        }
                    }
                }
                continue;
            }
        }
        System.out.println("KAKTUS");
    }
}