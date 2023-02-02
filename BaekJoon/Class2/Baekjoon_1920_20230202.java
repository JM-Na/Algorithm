import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        TreeSet<Long> A = new TreeSet<Long>();
        for(int i = 0; i<N; i++){
            A.add(scan.nextLong());
        }
        int M = scan.nextInt();
        for(int i = 0; i<M; i++){
            if(A.contains(scan.nextLong()))
                System.out.println(1);
            else
                System.out.println(0);
        }


    }

}
