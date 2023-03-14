// [BOJ] 14620. 꽃길
// 소요 시간 : 60분


import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bff = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bff.readLine());
        int length = Integer.parseInt(st.nextToken());
        int[][] board = new int[length][length];
        for (int i = 0; i < length; i++) {
            st = new StringTokenizer(bff.readLine());
            for (int j = 0; j < length; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
//        System.out.println(Arrays.deepToString(board));
        int loc2 = length - 2;
        int loc = loc2 * loc2;
        int minvalue = 1000000;
        for (int i = 0; i < loc; i++) {
            int irow = i / loc2 + 1, icol = i % loc2 + 1;
            for (int j = i; j < loc; j++) {
                int jrow = j / loc2 + 1, jcol = j % loc2 + 1;
                for (int k = j; k < loc; k++) {
                    int krow = k / loc2 + 1, kcol = k % loc2 + 1;
                    boolean cond1 = Math.abs(irow - jrow) + Math.abs(icol - jcol) >= 3;
                    boolean cond2 = Math.abs(jrow - krow) + Math.abs(jcol - kcol) >= 3;
                    boolean cond3 = Math.abs(krow - irow) + Math.abs(kcol - icol) >= 3;
                    if (cond1 && cond2 && cond3) {
                        int isum = board[irow - 1][icol] + board[irow + 1][icol] + board[irow][icol - 1] + board[irow][icol + 1] + board[irow][icol];
                        int jsum = board[jrow - 1][jcol] + board[jrow + 1][jcol] + board[jrow][jcol - 1] + board[jrow][jcol + 1] + board[jrow][jcol];
                        int ksum = board[krow - 1][kcol] + board[krow + 1][kcol] + board[krow][kcol - 1] + board[krow][kcol + 1] + board[krow][kcol];
                        if (minvalue > isum + jsum + ksum) {
                            minvalue = isum + jsum + ksum;
                        }
                    }
                }
            }
        }
        System.out.println(minvalue);
    }
}
