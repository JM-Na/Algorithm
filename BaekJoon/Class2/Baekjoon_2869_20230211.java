import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A = scan.nextInt();
        int B = scan.nextInt();
        int V = scan.nextInt();
        int stat = 0;
        int cnt = (V-A) / (A-B) + 1;
        if ((V - A) % (A - B) != 0) cnt++;

        System.out.println(cnt);
    }
}
