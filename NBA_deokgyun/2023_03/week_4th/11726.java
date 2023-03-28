import java.util.Scanner;

// [BOJ] 11726. 2xn 타일링
// 소요 시간 : 00분
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] memo = new long[n + 1];
        memo[0] = 1;
        memo[1] = 1;
        for (int i = 2; i <= n; i++){
            memo[i] = (memo[i - 1] + memo[i - 2]) % 10007;
        }
        long result = memo[n];
        System.out.println(result);
    }
}