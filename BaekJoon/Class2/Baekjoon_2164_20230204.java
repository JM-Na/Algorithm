import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Deque<Integer> stack = new ArrayDeque<>();

        int N = scan.nextInt();

        for(int i = N; i>0;i--){
            stack.add(i);
        }

        while(stack.size()>1){
            stack.removeLast();
            stack.addFirst(stack.removeLast());
        }
        System.out.println(stack.removeLast());
    }
}
