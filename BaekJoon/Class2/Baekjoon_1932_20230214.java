import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] arr = new int[N+1];
        int[] arrTemp = new int[N+1];
        int MAX = 0;
        for(int i = 1;i<=N;i++){
            System.out.println(Arrays.toString(arr));
            for(int j =1;j<=i;j++){
                int temp = scan.nextInt();
                if(i==1) arrTemp[i] = temp;
                else {
                    if(j==1)
                        arrTemp[j] = arr[1] + temp;
                    else if(j==i){
                        arrTemp[j] = arr[j-1] + temp;
                    }
                    else {
                        if(arr[j-1]>arr[j])
                            arrTemp[j] = arr[j-1] + temp;
                        else
                            arrTemp[j] = arr[j] + temp;
                    }
                }
                if(MAX < arrTemp[j]) MAX = arrTemp[j];
            }
            for(int k = 1; k<=i;k++){
                arr[k] = arrTemp[k];
            }
            System.out.println(Arrays.toString(arr));
            System.out.println();
        }
        System.out.println("MAX = " + MAX);
    }
}
