#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int N = 0, n = 0, cnt =1;
double** arr, **rad;
double sum = 0;
int* stack;
FILE* fp;
void sort();
void scan();
void cal();
double callength(int a, int b);
int main() {
	fp = fopen("test.txt", "r");
	char* data = fgetc(fp);
	N = atoi(&data);
	for (int i = 0; i < N; i++) {
		data = fgetc(fp);
		data = fgetc(fp);
		data = fgetc(fp);
		n = atoi(&data);
		data = fgetc(fp);
		arr = (double**)calloc(sizeof(double*), n);
		for (int j = 0; j < n; j++) {
			arr[j] = (double*)calloc(sizeof(double), 2);
		}
		int count = 0, pos = 0, dec = 0, temp = 0, neg = 0;
		while (!feof(fp)) {
			data = fgetc(fp);
			if (data == '\n') {
				if (neg == 1) temp *= -1;
				arr[count][pos] = temp;
				temp = 0;
				pos = 0;
				dec = 0;
				neg = 0;
				count++;
			}
			else if (data == ' ') {
				if (neg == 1) temp *= -1;
				arr[count][pos] = temp;
				temp = 0;
				dec = 0;
				neg = 0;
				pos++;
			}
			else if (data == '-') neg++;
			else {
				if (data == '.') dec++;
				if (dec == 0) {
					temp *= 10;
					temp += atoi(&data);
				}
				else {
					for (int i = 0; i < dec; i++) temp *= 10;
					temp += atoi(&data);
					for (int i = 0; i < dec; i++) temp /= 10;
					dec++;
				}
			}
		}
		if (neg == 1) temp *= -1;
		arr[count][pos] = temp;
	}
	sort();
	scan();
	cal();
	fclose(fp);
}

int ccw(int a, int b, int c) {
	return arr[a][0] * arr[b][1] + arr[b][0] * arr[c][1] + arr[c][0] * arr[a][1] - (arr[b][0] * arr[a][1] + arr[c][0] * arr[b][1] + arr[a][0] * arr[c][1]);
}
void sort() {
	double temp = 0;
	for (int i = 0; i < n-1; i++) {
		for (int j = 0; j < n - i-1; j++) {
			if (arr[j][0] > arr[j + 1][0]) {
				temp = arr[j][0];
				arr[j][0] = arr[j + 1][0];
				arr[j + 1][0] = temp;
				temp = arr[j][1];
				arr[j][1] = arr[j + 1][1];
				arr[j + 1][1] = temp;
			}
			else if (arr[j][0] == arr[j + 1][0] && arr[j][1] > arr[j + 1][1]) {
				temp = arr[j][0];
				arr[j][0] = arr[j + 1][0];
				arr[j + 1][0] = temp;
				temp = arr[j][1];
				arr[j][1] = arr[j + 1][1];
				arr[j + 1][1] = temp;
			}
		}
	}
	rad = (double**)calloc(sizeof(double*), n);
	for (int i = 0; i < n; i++) {
		rad[i] = (double*)calloc(sizeof(double), 2);
	}
	rad[0][0] = 0;
	rad[0][1] = 0;
	for (int i = 1; i < n; i++) {
		rad[i][0] = calRad(i);
		rad[i][1] = i;
	}
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n - 1; j++) {
			if (rad[j][0] > rad[j + 1][0]) {
				temp = rad[j][0];
				rad[j][0] = rad[j + 1][0];
				rad[j + 1][0] = temp;
				temp = rad[j][1];
				rad[j][1] = rad[j + 1][1];
				rad[j + 1][1] = temp;
			}
		}
	}
}
void scan() {
	int k = 1, i = 2;
	stack = (int *)calloc(sizeof(int), n);
	stack[0] = 0;
	stack[1] = 1;
	while(1) {
		if (i == n) i = 0;
		if (i == 1) break;
		if (ccw(stack[k - 1], stack[k], i) > 0) {
			stack[k+1] = i;
			k++;
			i++;
		}
		else {
			if (k == 1) {
				stack[k] = i;
				i++;
			}
			else {
				stack[k] = NULL;
				k--;
				i++;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (stack[i] != 0) cnt++;
	}
}
int calRad(int a) {
	double radian = atan2( arr[a][1] - arr[0][1], arr[a][0] - arr[0][0]);
	return radian * 180 / 3.141592;
}
double callength(int a, int b) {
	return sqrt(pow(arr[a][0] - arr[b][0], 2) + pow(arr[a][1] - arr[b][1], 2));
}
void cal() {
	for (int i = 0; i < cnt; i++) {
		sum += callength(stack[i], stack[i + 1]);
		if(stack[i+1]!=0) sum += 2;
	}
	printf("%.2lf", sum);
}
