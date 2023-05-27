// # [BOJ] 16918. 봄버맨
// # 소요 시간 : 00분

import java.util.Scanner;

class Boj16918 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] firstLine = sc.nextLine().split(" ");
        int rowCnt = Integer.parseInt(firstLine[0]);
        int colCnt = Integer.parseInt(firstLine[1]);
        String[] board = new String[rowCnt];
        String[] boardReverse = new String[rowCnt];
        String[] board2 = new String[rowCnt];
        char[][] charBoard2 = new char[rowCnt][colCnt];
        char[][] charBoard3 = new char[rowCnt][colCnt];
        int timeAfter = Integer.parseInt(firstLine[2]);
        for (int i = 0; i < rowCnt; i++) {
            board[i] = sc.nextLine();
            boardReverse[i] = "";
            charBoard2[i] = board[i].toCharArray();
            charBoard3[i] = "O".repeat(colCnt).toCharArray();
            for (Character j : board[i].toCharArray()) {
                boardReverse[i] += j == 'O' ? "." : "O";
            }
        }
        for (int i =0; i < rowCnt; i++) {
            for (int j = 0; j < colCnt; j++) {
                if (charBoard2[i][j] == 'O') {
                    for (int k = -1; k <= 1; k++) {
                        for (int t = -1; t <= 1; t++) {
                            if (Math.abs(k + t) == 1) {
                                try {
                                    charBoard3[i+k][j+t] = '.';
                                } catch(Exception e) {}
                            }
                        }
                    }
                    charBoard3[i][j] = '.';
                }
            }
        }

        int clean = 0;
        for (int i = 0; i < rowCnt; i++) {
            boardReverse[i] = new String(charBoard3[i]);
            if (boardReverse[i].equals(".".repeat(colCnt))) {
                clean++;
            }
        }
        if (clean == rowCnt) {
            for(int i = 0; i < rowCnt; i++) {
                board2[i] = new String("O".repeat(colCnt));
            }
        }
        else {
            for(int i = 0; i < rowCnt; i++) {
                board2[i] = new String(board[i]);
            }
        }
        sc.close();
        if (timeAfter < 2) {
            for (int i = 0; i < rowCnt; i++) {
                System.out.println(board[i]);
            }
        }
        else {
            switch ((timeAfter - 2) % 4) {
                case 0:
                case 2:
                    for(int i = 0; i < rowCnt; i++) {
                        System.out.println("O".repeat(colCnt));
                    }
                    break;
                case 1:
                    for(int i = 0; i < rowCnt; i++) {
                        System.out.println(boardReverse[i]);
                    }
                    break;
                case 3:
                    for(int i = 0; i < rowCnt; i++) {
                        System.out.println(board[i]);
                    }
                    break;
            }
        }
    }
}