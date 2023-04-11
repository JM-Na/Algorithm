import java.util.*;
public class Main {
    static Scanner scan = new Scanner(System.in);
    static int N = scan.nextInt(); // number of vertices
    static int M = scan.nextInt(); // number of edges
    static int V = scan.nextInt(); // starting vertex num.
    static ArrayList<Integer>[] arr = new ArrayList[N + 1];
    static ArrayList<Integer>[] arr1 = new ArrayList[N + 1];

    public static void main(String[] args) {
        for (int i = 0; i < N + 1; i++)
            arr[i] = new ArrayList<Integer>();
        for (int i = 0; i < M; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            if (!arr[a].contains(b))
                arr[a].add(b);
            if (!arr[b].contains(a))
                arr[b].add(a);
        }

        DFS();
        BFS();
    }

    private static void DFS() {
        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> dfsSq = new ArrayList<>();
        stack.push(V);
        int cnt = 0;
        while (true) {
            while(dfsSq.contains(stack.peek()))
                stack.pop();
            int k = stack.pop();
            dfsSq.add(k);
            Collections.sort(arr[k], Collections.reverseOrder());
            if (cnt == N || cnt == M || dfsSq.size() == N||arr[k].isEmpty())
                break;
            cnt++;
            for (int num : arr[k]) {
                if (!dfsSq.contains(num))
                    stack.push(num);
            }
        }
        for (int num : dfsSq){
            if(dfsSq.indexOf(num)==0)
                System.out.print(num);
            else
                System.out.print(" " + num);
        }
        System.out.println();
    }

    private static void BFS() {
        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Integer> bfsSq = new ArrayList<>();
        queue.offer(V);
        int cnt = 0;
        while (true) {
            while(bfsSq.contains(queue.peek()))
                queue.remove();
            int k = queue.poll();
            Collections.sort(arr[k]);
            bfsSq.add(k);
            if (cnt == N || cnt == M || bfsSq.size() == N||arr[k].isEmpty())
                break;
            cnt++;
            for (int num : arr[k]) {
                if (!bfsSq.contains(num))
                    queue.offer(num);
            }
        }
        for (int num : bfsSq){
            if(bfsSq.indexOf(num)==0)
                System.out.print(num);
            else
                System.out.print(" " + num);
        }
    }
}
