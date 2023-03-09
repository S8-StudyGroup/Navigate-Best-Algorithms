// [BOJ] 10870. 피보나치 수 5
// 소요 시간 : 40분

import java.io.*;
import java.util.*;

class Main {
    private static int[] fibo_num = new int[21];
    public static void main(String[] args) throws IOException {
        fibo_num[1] = 1;
        BufferedReader bff = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bff.readLine());
        int loc = Integer.parseInt(st.nextToken());
        System.out.println(fibonacci(loc));
        return;
    }
    
    private static int fibonacci(int loc) throws IndexOutOfBoundsException {
        if (loc == 0) {
            return 0;
        }
        else if (fibo_num[loc] != 0) {
            return fibo_num[loc];
        }
        else {
            fibo_num[loc] = fibonacci(loc - 1) + fibonacci(loc - 2);
            return fibo_num[loc];
        }
    }
}