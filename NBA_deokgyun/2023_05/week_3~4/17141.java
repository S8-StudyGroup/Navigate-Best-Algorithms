import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

// # [BOJ] 17141. 연구소 2
// # 소요 시간 : 00분

class Boj17141 {
    List<int[]> resultList;
    public static void main(String[] args) {
        Sol sol = new Sol();
        Scanner sc = new Scanner(System.in);
        String[] numbers = sc.nextLine().split(" ");
        int labSize = Integer.parseInt(numbers[0]), r = Integer.parseInt(numbers[1]);
        String[][] labBoard = new String[labSize][labSize];
        for (int i = 0; i < labSize; i++) {
            labBoard[i] = sc.nextLine().split(" ");
        }
        sc.close();
        int n = 0;
        List<int[]> virusList = new ArrayList<>();
        for (int i = 0; i < labSize; i++) {
            for (int j = 0; j < labSize; j++) {
                if (labBoard[i][j].equals("2")) {
                    n++;
                    int[] virus = {i,j};
                    virusList.add(virus);
                }
            }
        }
        sol.virusLocation(n,r);
        List<Integer> result = sol.bfs(labBoard, labSize, virusList);
        int finalResult = Integer.MAX_VALUE;
        for (int i : result) {
            if (i == -1)
                continue;
            else if (i < finalResult)
                finalResult = i;
        }
        System.out.println((finalResult == Integer.MAX_VALUE) ? -1 : finalResult);
    }
}

class Sol {
    List<List<Integer>> resultList;
    int selectingNum;
    int totalNum;
    public void virusLocation(int n, int r) {
        resultList = new ArrayList<>();
        totalNum = n;
        selectingNum = r;
        selectLocation(0, 0, new ArrayList<>());
    }
    public void selectLocation(int nowNum, int cnt, List<Integer> selected) {
        if (nowNum >= totalNum) {
            if (cnt == selectingNum) {
                List<Integer> selectedList = new ArrayList<>();
                for (int i = 0; i < selected.size(); i++) {
                    selectedList.add(selected.get(i));
                }
                resultList.add(selectedList);
            }
            return;
        }
        selected.add(nowNum);
        selectLocation(nowNum + 1, cnt + 1, selected);
        selected.remove(selected.size() - 1);
        selectLocation(nowNum + 1, cnt, selected);
    }
    public int bfs2(String[][] labBoard, List<Integer> virusLoc, List<int[]> virusList, int labSize) {
        Queue<int[]> queue = new LinkedList<>();
        for (int virus : virusLoc) {
            int[] virusNow = virusList.get(virus);
            labBoard[virusNow[0]][virusNow[1]] = "3";
            int[] virusNowTime = new int[3];
            virusNowTime[0] = virusNow[0];
            virusNowTime[1] = virusNow[1];
            virusNowTime[2] = 0;
            queue.add(virusNowTime);
        }
        int totalTime = 0;
        while (!queue.isEmpty()) {
            int[] virus = queue.poll();
            totalTime = virus[2];
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1;j++) {
                    if (Math.abs(i+j) == 1) {
                        try {
                            if (!labBoard[virus[0]+i][virus[1]+j].equals("1") && !labBoard[virus[0]+i][virus[1]+j].equals("3")) {
                                labBoard[virus[0]+i][virus[1]+j] = "3";
                                int[] virusNext = new int[3];
                                virusNext[0] = virus[0]+i;
                                virusNext[1] = virus[1]+j;
                                virusNext[2] = virus[2]+1;
                                queue.add(virusNext);
                            }
                        } catch(Exception e) {}
                    }
                }
            }
        }
        for (int i = 0; i < labSize; i++) {
            for (int j = 0; j < labSize; j++) {
                if (labBoard[i][j].equals("2") || labBoard[i][j].equals("0")) {
                    totalTime = -1;
                    break;
                }
            }
        }
        return totalTime;
    }
    public List<Integer> bfs(String[][] labBoard, int labSize, List<int[]> virusList) {
        
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < resultList.size(); i++) {
            List<Integer> virusLoc = resultList.get(i);
            String[][] labBoard2 = new String[labSize][labSize];
            for (int t = 0; t < labSize; t++) {
                for (int k = 0; k < labSize; k++) {
                    labBoard2[t][k] = labBoard[t][k];
                }
            }
            result.add(bfs2(labBoard2, virusLoc, virusList, labSize));
        }
        return result;
    }
}