// [BOJ] 10799. 쇠막대기
// 소요 시간 : 30분

import java.util.Scanner;


class boj10799 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String bars = sc.nextLine();
        sc.close();
        String[] result = bars.replace("()", "1").split("");
        int barNow = 0;
        int resultCount = 0;
        for (String i : result) {
            if (i.equals("(")) {
                barNow++;
            }
            else if (i.equals(")")) {
                barNow--;
                resultCount += 1;
            }
            else {
                resultCount += barNow;
            }
        }
        System.out.println(resultCount);
    }
}