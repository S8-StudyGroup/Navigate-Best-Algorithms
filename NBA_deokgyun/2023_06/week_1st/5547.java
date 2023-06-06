// # [BOJ] 5547. 일루미네이션
// # 소요 시간 : 00분

import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main{
    static int n, m;
    static int[][] arr;
    static int[][] odd = {{-1,0},{0,-1},{1,0},{1,1},{0,1},{-1,1}};
    static int[][] even = {{-1,-1},{0,-1},{1,-1},{1,0},{0,1},{-1,0}};
    static boolean[][] visit;
    static Queue<Point> queue = new LinkedList<>();
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        arr = new int[m+2][n+2];
        visit = new boolean[m+2][n+2];
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                arr[i][j] = scan.nextInt();
            }
        }
        bfs();
    }
    static void bfs(){
        queue.offer(new Point(0,0));
        visit[0][0] = true;
        while(!queue.isEmpty()){
            Point now = queue.poll();
            int nx = now.x;
            int ny = now.y;
            for(int i = 0; i < 6; i++){
                int px;
                int py;
                if(nx % 2 == 0) {
                    px = nx + even[i][0];
                    py = ny + even[i][1];
                }
                else {
                    px = nx + odd[i][0];
                    py = ny + odd[i][1];
                }
                if(px >= 0 && px <= m + 1 &&  py >= 0 && py <= n + 1){
                    if(!visit[px][py]){
                        if(arr[px][py] == 0){
                            visit[px][py] = true;
                            queue.offer(new Point(px, py));
                        }
                    }
                }
            }
        }
        int sum = 0;
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                if(arr[i][j] == 0)
                    continue;
                for(int t = 0; t < 6; t++){
                    int nx; int ny;
                    if(i % 2 == 0){
                        nx = i + even[t][0];
                        ny = j + even[t][1];
                    }else{
                        nx = i + odd[t][0];
                        ny = j + odd[t][1];
                    }
                    if(visit[nx][ny])
                        sum++;
                }
            }
        }
        System.out.println(sum);
    }
}