import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int cnt = 0;
        if (N < 5 && N != 3) {
            cnt = -1;
        }
        else {
            int a = N % 5;
            cnt += N / 5;
            if (a == 1 || a == 3) cnt += 1;
            else if (a == 2 || a == 4) {
                if (N == 7) cnt = -1;
                else cnt += 2;
            }

        }
        System.out.println(cnt);
    }
}
