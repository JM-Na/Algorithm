import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Set<String> set = new TreeSet<>();

        Integer max, cnt = 0;
        max = scan.nextInt();
        scan.nextLine();

        for (int i = 0; i < max; i++) {
            set.add(scan.nextLine());
        }

        String[] arr = new String[set.size()];
        for (String s : set) {
            arr[cnt] = s;
            cnt++;
        }
        Arrays.sort(arr, (String s1, String s2) -> s1.length() - s2.length());

        for (String s : arr) {
            System.out.println(s);
        }
    }
}
