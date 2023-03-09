// [Programmers] 43105. 정수 삼각형
// 소요 시간 : 60분

import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int tri_len = triangle.length;
        int[][] num_arr = triangle;
        for (int i = 0; i < tri_len; i++) {
            int arr_len = triangle[i].length;
            for (int j = 0; j < arr_len;j++) {
                if (i == 0) {
                    num_arr[i][j] = triangle[i][j];
                }
                else if (j == 0) {
                    num_arr[i][j] = triangle[i - 1][j] + triangle[i][j];
                }
                else if (j == arr_len - 1) {
                    num_arr[i][j] = triangle[i - 1][j - 1] + triangle[i][j];
                }
                else {
                    int num1 = triangle[i - 1][j - 1] + triangle[i][j];
                    int num2 = triangle[i - 1][j] + triangle[i][j];
                    num_arr[i][j]  = (num1 > num2) ? num1 : num2;
                }
            }
        }
        Arrays.sort(num_arr[tri_len - 1]);
        answer = num_arr[tri_len - 1][num_arr[tri_len - 1].length - 1];
        return answer;
    }
}