import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();
        int count = 0 ;
        Queue<Integer> queue = new LinkedList<>();
        Queue<Integer> result = new LinkedList<>();

        for(int i = 1;i<=N;i++){
            queue.add(i);
        }
        while(!queue.isEmpty()){
            count++;
            int temp = queue.poll();
            if(count != K)
                queue.add(temp);
            else{
                count = 0;
                result.add(temp);
            }
        }
        for(int i = 0; i <N;i++){
            if(i==0) System.out.print('<');
            System.out.print(result.poll());
            if(i!=N-1) System.out.print(", ");
            else System.out.print('>');
        }
    }
}
