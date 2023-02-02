import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A = scan.nextInt();
        int B = scan.nextInt();
        int gcd = GCD(A,B);
        System.out.println(gcd);
        System.out.println(A*B/gcd);
    }
    static int GCD(int a, int b){
        int temp;
        while(a%b!=0){
            temp = a;
            a = b;
            b = temp % b;
        }
        return b;
    }
}
