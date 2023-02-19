public class Merge_Sort {
    private static int[] sorted;
    // 정렬된 데이터를 임시로 저장할 배열
    public static void merge_sort(int[] a) { // 최초 배열을 입력 받을 시
        sorted = new int[a.length];
        merge_sort(a, 0, a.length - 1);
        sorted = null;
    }
    private static void merge_sort(int[] a, int left, int right) { // 입력 받은 배열을 분할
        if(left == right) return;

        int mid = (left + right) / 2;	// 절반 위치

        merge_sort(a, left, mid);		// 절반 중 왼쪽 부분리스트(left ~ mid)
        merge_sort(a, mid + 1, right);	// 절반 중 오른쪽 부분리스트(mid+1 ~ right)

        merge(a, left, mid, right);		// 병합작업
    }
    private static void merge(int[] a, int left, int mid, int right) { // 입력 받을 배열을 정렬
        int l = left;		// 왼쪽 부분리스트 시작점
        int r = mid + 1;	// 오른쪽 부분리스트의 시작점
        int idx = left;		// 채워넣을 배열의 인덱스

        while(l <= mid && r <= right) { //왼쪽 또는 오른쪽에서 종점에 도달할 때까지
            if(a[l] <= a[r]) {
                sorted[idx] = a[l];
                idx++;
                l++;
            }
            else {
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        }

        if(l > mid) //while문 종료 후 남는 경우 확인
            while(r <= right) {
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        else
            while(l <= mid) {
                sorted[idx] = a[l];
                idx++;
                l++;
            }

        for(int i = left; i <= right; i++)
            a[i] = sorted[i];
    }
}