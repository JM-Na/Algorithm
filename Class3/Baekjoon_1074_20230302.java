import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int r = scan.nextInt();
        int c = scan.nextInt();
        int temp = N;
        int result = 0;
        while (true) {
            if (temp == 1) {
                result = result + r * 3 + c;
                if (r == 1) result--;
                break;
            }
            double num = Math.pow(2, temp - 1);
            if (r < num && c < num) result += 0;
            else if (r < num && c >= num) {
                result += Math.pow(num, 2);
                c -= num;
            } else if (r >= num && c < num) {
                result += (2 * Math.pow(num, 2));
                r -= num;
            } else if (r >= num && c >= num) {
                result += (3 * Math.pow(num, 2));
                r -= num;
                c -= num;
            }
            temp--;
        }
        System.out.println(result);
    }
}
