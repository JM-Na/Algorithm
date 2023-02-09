import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        int N = scan.nextInt();
        int k = 0;
        while (N-- > 0) {
            int num = scan.nextInt();
            if (k < num) {
                for (int i = k+1; i <= num; i++) {
                    stack.push(i);
                    sb.append("+").append("\n");
                }
                k = num;
            }
            else if (stack.peek() != num) {
                System.out.println("NO");
                return;
            }
            stack.pop();
            sb.append("-").append("\n");
        }
        System.out.println(sb);
    }
    /*public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> result = new ArrayList<String>();
        int N = scan.nextInt();
        int k = 0;
        int cnt = 0;

        while (N > cnt) {
            int num = scan.nextInt();
            if (k < num) {
                for (int i = k+1; i <= num; i++) {
                    stack.push(i);
                    result.add("+");
                }
                k = num;
            }
            else if (stack.peek() != num) break;
            stack.pop();
            result.add("-");
            cnt++;
        }
        if (stack.isEmpty())
            for (int i = 0; i < result.size(); ++i) {
                System.out.println(result.get(i));
            }
        else System.out.println("NO");

    }*/
    /*public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] arr = new int[N+1];
        int pos = 1;
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> result = new ArrayList<String>();
        for(int i = 1; i<=N;i++){
            arr[i] = scan.nextInt();
        }
        for(int i = 1;i<=N;i++){
            stack.push(i);
            result.add("+");
            while(!stack.isEmpty()&&stack.peek() == arr[pos]){
                stack.pop();
                result.add("-");
                pos++;
            }
        }
        if(stack.isEmpty()){
            for(int i = 0;i<2*N;i++){
                System.out.println(result.get(i));
            }
        }
        else System.out.println("NO");

    }*/
    /*public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> result = new ArrayList<String>();
        int N = scan.nextInt();
        int k = 0;
        int cnt = 0;

        while(N>cnt){
            int num = scan.nextInt();
            while(true){
                if(k>num){
                    int temp = stack.pop();
                    if(temp!=num) break;
                    else if(temp==num){
                        result.add("-");
                        break;
                    }
                }
                else if(k==num){
                    int temp = stack.pop();
                    if(temp!=num) break;
                    else if(temp==num){
                        result.add("-");
                        break;
                    }
                }
                else if(k<num){
                    k++;
                    for(;k<=num;k++){
                        stack.push(k);
                        result.add("+");
                    }
                    k--;
                }
            }
            cnt++;
        }
        if(result.size() == 2*N)
            for (int i = 0; i < result.size(); ++i) {
                System.out.println(result.get(i));
            }
        else System.out.println("NO");
    }*/
}
