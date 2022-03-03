import java.util.Scanner;

public class BagherHalNadareValiPoolDare {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int A[] = new int[11];

        for (int i = 1; i <= n; i++)
            A[i] = scanner.nextInt();


        int memo[][] = new int[10001][11];
        int INF = 1000000000;

        for (int i = 1; i <= m; i++)
            memo[i][0] = INF;


        for (int j = 1; j <= n; j++) {
            for (int i = 0; i <= m; i++) {
                memo[i][j] = INF;
                for (int k = 1; k * k <= i; k++) {
                    if (memo[i][j] > memo[i - k * k][j - 1] + (A[j] - k) * (A[j] - k))
                        memo[i][j] = memo[i - k * k][j - 1] + (A[j] - k) * (A[j] - k);

                }
            }
        }

        if (memo[m][n] == INF)
            System.out.println(-1);
        else
            System.out.println(memo[m][n]);

    }
}
