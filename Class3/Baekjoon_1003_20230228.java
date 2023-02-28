import java.io.*;
import java.util.*;

public class Main {
    static int[] result0 = new int[41];
    static int[] result1 = new int[41];
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        for(int i = 0;i<T;i++){
            int N = scan.nextInt();
            fibonacci(N);
            System.out.println(result0[N]+" "+result1[N]);
        }
    }
    public static void fibonacci(int n){
        if(n==0) result0[0] = 1;
        else if (n==1) result1[1] =1;
        else{
            if(result0[n]==0&&result1[n]==0){
                fibonacci(n-1);
                fibonacci(n-2);
            }
            result0[n] = result0[n-1]+result0[n-2];
            result1[n] = result1[n-1]+result1[n-2];
        }
    }
}
