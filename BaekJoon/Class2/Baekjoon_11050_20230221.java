import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();

        System.out.println(calculate(N, K));

    }
    public static int calculate(int n, int k){
        int temp;
        if(n==k||k==0)
            return 1;
        temp = calculate(n-1,k-1) + calculate(n-1, k);
        return temp;
    }
}
