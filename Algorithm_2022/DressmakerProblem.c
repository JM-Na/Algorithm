#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char* data;
int* T, * S;
double** avg;
int K, N;

void input();
void output();
void sort();

FILE* fp;

void main() {
	fp = fopen("test.txt", "r");

	data = fgetc(fp);
	K = atoi(&data);

	for (int i = 0; i < K; i++) {
		input();
		sort();
		output();
	}

	free(T);
	free(S);
	free(avg);

	fclose(fp);
}

void input() {
	do { data = fgetc(fp); } while (data == '\n');
	N = atoi(&data);
	T = (int*)calloc(N, sizeof(int));
	S = (int*)calloc(N, sizeof(int));
	avg = (double*)calloc(N, sizeof(double));

	data = fgetc(fp);

	for (int i = 0; i < N; i++) {
		int num = 0;
		while (1) {
			data = fgetc(fp);
			if (isspace(data)) {
				break;
			}
			else {
				if (num == 0) num = atoi(&data);
				else num = num * 10 + atoi(&data);
			}
		}
		T[i] = num;
		num = 0;
		while (1) {
			data = fgetc(fp);
			if (isspace(data) != 0 || data == EOF) {
				break;
			}
			else {
				if (num == 0) num = atoi(&data);
				else num = num * 10 + atoi(&data);
			}
		}

		S[i] = num;
		avg[i] = (double*)calloc(2, sizeof(double));
		avg[i][0] = (double)S[i] / (double)T[i];
		avg[i][1] = i + 1.0;
	}

}

void sort() {

	double temp1, temp2, temp3;

	int index = 0;

	for (int k = N - 1; k > 0; k--) {
		for (int i = 0; i < k; i++) {
			if (avg[i][0] < avg[i + 1][0]) {
				temp1 = avg[i][0];
				temp2 = avg[i][1];
				temp3 = T[i];
				avg[i][0] = avg[i + 1][0];
				avg[i + 1][0] = temp1;
				avg[i][1] = avg[i + 1][1];
				avg[i + 1][1] = temp2;
				T[i] = T[i + 1];
				T[i + 1] = temp3;
			}
			else if (avg[i][0] == avg[i + 1][0] && T[i] > T[i + 1]) {
				temp1 = avg[i][0];
				temp2 = avg[i][1];
				temp3 = T[i];
				avg[i][0] = avg[i + 1][0];
				avg[i + 1][0] = temp1;
				avg[i][1] = avg[i + 1][1];
				avg[i + 1][1] = temp2;
				T[i] = T[i + 1];
				T[i + 1] = temp3;
			}
		}
	}
}

void output() {
	int k = 0;
	for (int i = 0; i < N; i++) {
		printf("%.0lf ", avg[i][1]);
	}
	printf("\n");
}