# [BOJ] 15656. N과 M (7)

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.

전체적으로 코드가 깔끔하게 작성되어 있고, 의미 있는 변수명을 사용하고 있습니다. 하지만 몇 가지 개선할 부분이 있습니다.

1. 재귀함수를 이용하여 코드를 작성하면 더욱 간결해질 수 있습니다.
2. StringBuilder 객체를 사용하면 문자열 연산이 많아져도 효율적인 성능을 보장할 수 있습니다. 현재 코드에서는 반복문 안에서 계속해서 문자열을 추가하는 방식으로 문자열을 생성하고 있습니다. 이 방식은 문자열이 길어질수록 성능이 저하됩니다.
3. 결과 출력 부분에서 개행 문자를 문자열에 추가하고 있습니다. 이 부분에서는 개행 문자 대신에 System.out.println() 메서드를 사용하는 것이 더욱 간결해질 수 있습니다.
4. 현재 코드에서는 for 반복문의 조건식으로 **`i < N + 1`**을 사용하고 있습니다. 이 부분에서는 **`i <= N`**으로 변경하는 것이 더욱 자연스러울 수 있습니다.
```

2. **개선 코드**

```java
# ChatGPT의 개선된 코드를 적어주세요.

import java.io.*;
import java.util.*;

public class boj_15656 {
    static StringBuilder stringbuild = new StringBuilder();
    static int[] num_arr, result_arr;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        num_arr = new int[N];
        result_arr = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num_arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(num_arr);
        permute(0);
        System.out.print(stringbuild);
    }

    private static void permute(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                stringbuild.append(result_arr[i]).append(" ");
            }
            stringbuild.append("\n");
            return;
        }
        for (int i = 0; i < N; i++) {
            result_arr[depth] = num_arr[i];
            permute(depth + 1);
        }
    }
}
```

### 🌼 **도움되었던 내용**

백트래킹을 오랜만에 다시 복습해서 좋았습니다.
