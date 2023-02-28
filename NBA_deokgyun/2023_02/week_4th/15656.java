// N과 M (7)
// 소요시간 : 120분
// https://www.acmicpc.net/problem/15656

package boj_15656;
import java.io.*;
import java.util.*;

public class boj_15656 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] num_arr = new int[N];
        String[] numst_arr = new String[N];
        int[] result_arr = new int[M];
        for (int i=0; i < N;i++) {
            num_arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(num_arr);
        for (int i = 0; i < N; i++){
            numst_arr[i] = Integer.toString(num_arr[i]);
        }
        StringBuilder stringbuild = new StringBuilder();
        for (int i = 0; i < N + 1; i++) {
            result_arr[M-1] = i;
            if (i == N) {
                i = 0;
                for (int j = M-1; j > 0; j--) {
                    if (result_arr[j] == N) {
                        result_arr[j] = 0;
                        result_arr[j - 1] += 1;
                    }
                }
                if (result_arr[0] == N) {
                    break;
                }
            }
            for (int t = 0; t < M-1; t++)
                stringbuild.append(numst_arr[result_arr[t]]).append(" ");
            stringbuild.append(numst_arr[result_arr[M-1]]).append("\n");
        }
        System.out.println(stringbuild);
        return;
    }
}