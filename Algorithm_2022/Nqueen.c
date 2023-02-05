#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n; //보드판 한 변의 크기
int* col; //각 행별로 퀸의 위치 

void printQueens() {
    int i;
    printf(" ");
    for (i = 1; i <= n; i++)
        printf("row : %d, column : %d\n ", i, col[i]);
    exit(1);
}

int checkerror(int i) { // 오류가 없는지 체크 
    int k = 1;
    while (k < i) {
        if (col[i] == col[k] || abs(col[i] - col[k]) == abs(i - k))    // 상하좌우 및 대각선 상에 있는 지 확인
            return 0;
        k++;
    }
    return 1;
}

void setQueens(int i) {
    if (checkerror(i)) { // 오류가 없는 경우 (상하좌우 및 대각선 상에 겹치지 않는 경우)
        if (i == n) { // 마지막 행까지 선택이 끝났다면 
            printQueens();    // 퀸의 위치 출력 
            return;
        }
        else {
            for (int j = 1; j <= n; j++) { // 모든 열 탐색 
                col[i + 1] = j;
                setQueens(i + 1); // 재귀적으로 다음 열 탬색
            }
        }
    }
}

int main() {
    printf("Input N: ");
    scanf("%d", &n);
    col = (int*)malloc(sizeof(int) * (n + 1));
    setQueens(0);
    printf("No solution exists.");    // 해결법이 없을 경우 

    return 0;
}
