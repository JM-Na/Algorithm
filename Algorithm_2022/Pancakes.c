#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cakes[30] = {0, };
char stack[1024];
char* cake;
int count = 0;

int findBiggest(int);
void flip(int, int);
int check(int);

int main() {
	FILE* fp;

	int  num =0, t=0, arrCount=0;

	fp = fopen("test.txt", "r");
	while (!feof(fp)) {
		cake = fgets(stack, 1024, fp);
		arrCount++;
		t = 0;
		num = 0;
		if(arrCount == 3) stack[strlen(stack) - 1] = '\0';
		while (t < strlen(cake)) {
			int temp = 0;

			for (;stack[t]!=' '&& stack[t] != '\0'&&stack[t]!=NULL; t++) {
				temp += stack[t] - '0';
				if (stack[t+1] == '\n' || stack[t + 1] == ' ') {
					t++;
					break;
				}
				temp *= 10;
			}
			t++;
			cakes[num] = temp;
			num++;
		}
		count = num;
		printf("정렬 이전의 스택입니다.\n");
		for (int j = 0; j < count; j++) {
			printf("%d ", cakes[j]);
		}
		printf("\n\n");

		while (1) {
			if (check(num) != 0) {
				int max = findBiggest(num);
				if (max == 0&&check(num)==0) return 0;
				flip(max, num);
			}
			else break;
			int k = cakes[num - 1];
			do {
				num--;
			} while (k == cakes[num - 1]);
		}

		printf("\n");
		printf("정렬 후의 스택입니다.\n");
		for (int l = 0; l < count; l++) {
			printf("%d ", cakes[l]);
		}
		printf("\n\n");
		for (int k = 0; k < num; k++) {
			cakes[k] = 0;
		}
	}

	fclose(fp);

	return 0;
}

int findBiggest(int k) {
	int max = cakes[k-1], idx = k-1;
	for (int i = k-1; i >= 0; i--) {
		if (max < cakes[i]) {
			max = cakes[i];
			idx = i;
		}
	}
	return idx;
}

void flip(int k, int num) {
	int temp[30] = { 0, }, temp2;
	for (int i = 0; i < num; i++) { //temp배열에 cakes 배열을 복사
		temp[i] = cakes[i];
	}
	for (int j = 0; j < k+1; j++) {
		temp[j] = cakes[k - j];
	}
	for (int t = 0; t <num; t++) {
 		temp2 = temp[num-1 - t];
		cakes[t] = temp2;
	}
	for (int l = 0; l < count; l++) {
		printf("%d ", cakes[l]);
	}
	printf("\n");
}

int check(int k) {
	int temp = 0;
	for (int i = k-1; i >= 0.; i--) {
		if (cakes[i] < cakes[i - 1]) {
			temp++;
		}
	}
	return temp;
}