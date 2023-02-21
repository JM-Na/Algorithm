import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int max = 0;
        int[] arr = new int[N];
        for (int i = 0; i < N;i++ ) {
            arr[i] = scan.nextInt();
        }
        for (int i = 0; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                for (int l = j + 1; l < N; l++) {
                    int temp;
                    temp = arr[i] + arr[j] + arr[l];
                    if (temp <= M && max < temp)
                        max = temp;
                }
            }
        }
        System.out.println(max);

    }
}
