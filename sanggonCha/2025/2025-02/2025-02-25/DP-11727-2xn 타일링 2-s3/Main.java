import java.io.*;

public class Main {
    private static int N;
    private static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        N = Integer.parseInt(br.readLine());

        // dp
        if (N == 1) {
            System.out.println(1);
        } else if (N == 2) {
            System.out.println(2);
        } else {
            dp = new int[N + 1];
            dp[1] = 1;
            dp[2] = 3;
            for (int i = 3; i <= N; i++) {
                dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007;
            }

            System.out.println(dp[N]);
        }
    }
}