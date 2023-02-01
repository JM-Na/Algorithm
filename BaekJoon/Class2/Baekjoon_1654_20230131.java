import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int K = scan.nextInt();
        int N = scan.nextInt();
        long sum = 0;
        long[] arr = new long[K];
        long max = 0;
        long min = 1;
        for(int i = 0; i < K; i++){
            arr[i] = scan.nextInt();
            if(arr[i]>max)
                max = arr[i];
            sum += arr[i];
        }
        long origin_max = max;
        while(true){
            long res1 = 0, res2 = 0;

            if(min <= 0)
                min =1;
            for(int i =0; i<K;i++){
                res1 += (arr[i]/min);
            }
            for(int i =0; i<K;i++){
                res2 += (arr[i]/max);
            }
            //System.out.println("max = " + max + " " + "res2 = " + res2);
            //System.out.println("min = " + min + " " + "res1 = " + res1);
            //System.out.println("---------------");
            if(res1>=N && res2>=N){
                if (max == min)
                    break;
                long temp = max;
                max = 2 * max - min;
                if(max>origin_max)
                    max = origin_max;
                min = temp;
            }
            else if(res1>=N && res2<N){
                if(max - min <=1)
                    break;
                min = (min + max)/2;
            }
            else if(res1<N && res2<N){
                long temp = min;
                min = min * 2 - max;
                max = temp;
            }
        }
        System.out.println(min);
    }
}
