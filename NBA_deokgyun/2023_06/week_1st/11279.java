// # [BOJ] 11279. 최대 힙
// # 소요 시간 : 00분
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Boj11279 {
    private static int[] heap;
    private static int size;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        heap = new int[N + 1];
        size = 0;

        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());

            if (x == 0) {
                if (size == 0) {
                    System.out.println(0);
                } else {
                    int max = deleteMax();
                    System.out.println(max);
                }
            } else {
                insert(x);
            }
        }

        br.close();
    }

    private static void insert(int value) {
        heap[++size] = value;
        int current = size;

        while (current > 1 && heap[current] > heap[current / 2]) {
            swap(current, current / 2);
            current /= 2;
        }
    }

    private static int deleteMax() {
        int max = heap[1];
        heap[1] = heap[size];
        heap[size--] = 0;

        int current = 1;
        int child;

        while (current * 2 <= size) {
            child = current * 2;

            if (child < size && heap[child] < heap[child + 1]) {
                child++;
            }

            if (heap[current] < heap[child]) {
                swap(current, child);
                current = child;
            } else {
                break;
            }
        }

        return max;
    }

    private static void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
}
