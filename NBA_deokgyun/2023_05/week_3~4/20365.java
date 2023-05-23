// # [BOJ] 20365. 블로그2
// # 소요 시간 : 00분

import java.util.Scanner;

class Boj20365 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputNum = sc.nextLine();
        String inputStr = sc.nextLine();
        sc.close();
        int cnt = 0;
        Character prevChar = null;
        for (Character i : inputStr.toCharArray()) {
            if (!i.equals(prevChar)) 
                cnt++;
            prevChar = i;
        }
        System.out.println(cnt / 2 + 1);
    }
}