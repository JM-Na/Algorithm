import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true){
            int[] arr = new int[3];
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();
            arr[0] = a;
            arr[1] = b;
            arr[2] = c;
            if(a==0&&b==0&&c==0)
                break;
            if(arr[0]>arr[1]){
                int temp = arr[0];
                arr[0] = arr[1];
                arr[1] = temp;
            }
            if(arr[1]>arr[2]){
                int temp = arr[1];
                arr[1] = arr[2];
                arr[2] = temp;
            }
            if(arr[0]>arr[1]){
                int temp = arr[0];
                arr[0] = arr[1];
                arr[1] = temp;
            }
            if(arr[1]>arr[2]){
                int temp = arr[1];
                arr[1] = arr[2];
                arr[2] = temp;
            }
            if(arr[0]*arr[0] + arr[1]*arr[1] == arr[2]*arr[2])
                System.out.println("right");
            else
                System.out.println("wrong");
        }


    }
}
