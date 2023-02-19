import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(bf.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(bf.readLine()); //
        }
        Merge_Sort m = new Merge_Sort();
        m.merge_sort(arr);
        for (int i = 0; i < N; i++) {
            bw.write(Integer.toString(arr[i]));
            bw.write('\n');
        }
        bw.flush();
    }
}
