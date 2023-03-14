// [BOJ] 16987. 계란으로 계란치기
// 소요 시간 : 60분


import java.io.*;
import java.util.*;

class Main {
    private static int max_eggs = 0;
    private static int number = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader bff = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bff.readLine());
        number = Integer.parseInt(st.nextToken());
        int[][] eggs = new int[number][2];
        for (int i = 0; i < number; i++) {
            st = new StringTokenizer(bff.readLine());
            for (int j = 0; j < 2; j++) {
                eggs[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        select(eggs, 0);
        System.out.println(max_eggs);
    }
    private static void select(int[][] eggs, int idx) throws IndexOutOfBoundsException {
        if (idx >= number) {
            int result = 0;
            for (int i = 0; i < number; i++) {
                if (eggs[i][0] <= 0) {
                    result++;
                }
            }
            if (result > max_eggs) {
                max_eggs = result;
            }
            return;
        }
        else {
            if (eggs[idx][0] <= 0) {
                select(eggs, idx + 1);
            }
            else {
                int left_count = 0;
                for (int i = 0; i < number; i++) {
                    if (eggs[i][0] > 0 && i != idx) {
                        left_count++;
                        eggs[i][0] -= eggs[idx][1];
                        eggs[idx][0] -= eggs[i][1];
                        select(eggs, idx + 1);
                        eggs[i][0] += eggs[idx][1];
                        eggs[idx][0] += eggs[i][1];
                    }
                }
                if (left_count == 0) {
                    select(eggs, idx + 1);
                }
            }
        }
    }
}
