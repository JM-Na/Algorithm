#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n; //������ �� ���� ũ��
int* col; //�� �ະ�� ���� ��ġ 

void printQueens() {
    int i;
    printf(" ");
    for (i = 1; i <= n; i++)
        printf("row : %d, column : %d\n ", i, col[i]);
    exit(1);
}

int checkerror(int i) { // ������ ������ üũ 
    int k = 1;
    while (k < i) {
        if (col[i] == col[k] || abs(col[i] - col[k]) == abs(i - k))    // �����¿� �� �밢�� �� �ִ� �� Ȯ��
            return 0;
        k++;
    }
    return 1;
}

void setQueens(int i) {
    if (checkerror(i)) { // ������ ���� ��� (�����¿� �� �밢�� �� ��ġ�� �ʴ� ���)
        if (i == n) { // ������ ����� ������ �����ٸ� 
            printQueens();    // ���� ��ġ ��� 
            return;
        }
        else {
            for (int j = 1; j <= n; j++) { // ��� �� Ž�� 
                col[i + 1] = j;
                setQueens(i + 1); // ��������� ���� �� �ƻ�
            }
        }
    }
}

int main() {
    printf("Input N: ");
    scanf("%d", &n);
    col = (int*)malloc(sizeof(int) * (n + 1));
    setQueens(0);
    printf("No solution exists.");    // �ذ���� ���� ��� 

    return 0;
}
