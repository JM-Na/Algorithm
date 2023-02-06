import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int count = 1;

        while(true){
            if(count == 1){
                N -= 1;
            }
            else{
                N = N - (count*6-6);
            }
            if(N<=0){
                break;
            }
            count++;
        }

        System.out.println(count);
    }
}
