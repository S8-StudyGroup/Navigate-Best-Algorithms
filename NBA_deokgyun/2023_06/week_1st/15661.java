// # [BOJ] 15661. 링크와 스타트
// # 소요 시간 : 00분

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Boj15661 {
	static int map[][], n, answer,t;
	static boolean v[];
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		v = new boolean[n];
		answer = Integer.MAX_VALUE;
		t=0;
		StringTokenizer stk;
		
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		for(t=1; t<n; t++) {
			nCr(0,0);			
		}
		System.out.println(answer);
	}
	
	public static void nCr(int depth, int start) {
		
		if(depth == t ) {
			answer = Math.min(answer, diff());
			if(answer == 0) {
				System.out.println(answer);
				System.exit(0);
			}
			return;
		}
		for(int i=start; i<n; i++) {
			if(!v[i]) {
				v[i]= true;
				nCr(depth+1, i+1);
				v[i]=false;
			}
		}
	}
	
	public static int diff() {
		
		int start = 0; 
		int link = 0; 
		for(int i=0; i<n-1; i++) {
			for(int j=i+1; j<n; j++) {
				if(v[i] && v[j]) {
					start += (map[i][j] +map[j][i]);
				}
				else if(!v[i] && !v[j]) {
					link += (map[i][j] + map[j][i]);
				}
			}
		}
		
		return  Math.abs(start - link);
	}
}