#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
int M, N;
char** brd;

int check(int a, int b) {
	int min = 0, temp = 0, cnt = 1;
	for (int i = a; i < a+8; i++) {
		for (int j = b; j < b+8; j++) {
			if (cnt == 0) {
				if (brd[i][j] != 'W')
					temp++;
			}
			else if (cnt == 1) {
				if (brd[i][j] != 'B')
					temp++;
			}
			cnt++;
			if (cnt == 2)
				cnt -= 2;
		}
		cnt++;
		if (cnt == 2)
			cnt -= 2;
	}
	min = temp;
	temp = 0;
	cnt = 0;
	for (int i = a; i < a+8; i++) {
		for (int j = b; j < b+8; j++) {
			if (cnt == 0) {
				if (brd[i][j] != 'W')
					temp++;
			}
			else if (cnt == 1) {
				if (brd[i][j] != 'B')
					temp++;
			}
			cnt++;
			if (cnt == 2)
				cnt -= 2;
		}
		cnt++;
		if (cnt == 2)
			cnt -= 2;
	}

	if (min > temp)
		min = temp;

	return min;
}

int main() {
	scanf("%d %d", &M, &N);
	int min = 64;
	brd = (char**)calloc(M, sizeof(char*));
	for (int i = 0; i < M; i++) {
		brd[i] = (char*)calloc(N, sizeof(char));
	}

	char temp[50];
	for (int i = 0; i < M; i++) {
		scanf("%s", temp);
		for (int j = 0; j < N; j++) {
			brd[i][j] = temp[j];
		}
	}

	for (int i = 0; i < M - 7; i++) {
		for (int j = 0; j < N - 7; j++) {
			int num = check(i, j);
			if (min > num)
				min = num;
		}
	}
	for (int i = 0; i < M; i++) {
		free(brd[i]);
	}
	free(brd);
	printf("%d", min);

	return 0;
}
