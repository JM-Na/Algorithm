import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true){
            int input = scan.nextInt();
            if(input == 0)
                break;
            int length = (int)(Math.log10(input)+1);
            int cnt = 0;
            int[] arr = new int[length];
            for(int i = 0;i<length;i++){
                arr[i] = input % 10;
                input /= 10;
            }
            for(int i = 0; i<length/2;i++){
                if(arr[i]!=arr[length-1-i]){
                    cnt++;
                }
            }
            if(cnt != 0)
                System.out.println("no");
            else
                System.out.println("yes");
            cnt=0;
        }
    }
}
