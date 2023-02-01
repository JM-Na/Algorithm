import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int temp = 666, num = 0;
        while(true){
            if(Integer.toString(temp).contains("666")){
                num++;
            }
            if(num == N){
                System.out.println(temp);
                break;
            }
            else
                temp++;
        }
    }
}
