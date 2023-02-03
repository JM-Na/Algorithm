import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int cnt = 0;
        for(int i =0;i<N;i++){
            if(check(scan.nextInt())==1)
                cnt++;
        }
        System.out.println( cnt);
    }
    static int check(int a){
        int cnt = 0;
        if(a==1)
            return 0;
        for(int i = 1;i<=Math.sqrt(a);i++){
            if(a%i==0)
                cnt++;
        }
        if(cnt > 1)
            return 0;
        else
            return 1;
    }
}
