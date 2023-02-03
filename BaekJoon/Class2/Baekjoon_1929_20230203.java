import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int M = scan.nextInt();
        int N = scan.nextInt();
        for(int i = M; i<=N;i++){
            if(check(i)==1)
                System.out.println(i);
        }
    }
    static int check(int a){
        int cnt = 0;
        if(a == 1)
            return 0;
        else if(a>1&&a<4)
            return 1;
        else {
            for(int i = 1; i <= Math.sqrt(a); i++){
                if(a%i==0)
                    cnt++;
            }
            if(cnt == 1)
                return 1;
            else
                return 0;
        }
    }
}
