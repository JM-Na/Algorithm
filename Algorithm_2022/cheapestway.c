#pragma warning(disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char data;
char past;
int row, column;
int** cost,  **array;
char** route;

void search();

void main() {
	FILE* fp;
	fp = fopen("test.txt", "r");
	if (fp == NULL) {
		puts("파일을 열 수 없습니다.");
	}
	//row 값 입력 받은 후 동적 배열
	fscanf(fp, "%d %d", &row, &column);

	array = (int**)calloc(row, sizeof(int*));
	cost = (int**)calloc(row, sizeof(int*));
	route = (char**)calloc(row, sizeof(char*));

	for (int i = 0; i < row; i++) {
		array[i] = (int*)calloc(column, sizeof(int));
		cost[i] = (int*)calloc(column, sizeof(int));
		route[i] = (char*)calloc(column, sizeof(char));
	}
	
	//수 입력 받기
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			fscanf(fp, "%d", &array[i][j]);
		}
	}

	search();

	for (int i = 0; i < row; i++) {
		free(array[i]);
		free(cost[i]);
		free(route[i]);
	}

	free(array);
	free(cost);
	free(route);

	fclose(fp);
}

void search() {
	int min = 10, k = 0, index = 0;
	for (int i = 0; i < column; i++) {
		for (int j = 0; j < row; j++) {
			if (i == 0) {
				cost[j][i] = array[j][i];
				itoa(array[j][i], &past, 10);
				route[j][i] = past;
			}
			else {
				min = cost[j][i - 1];
				index = j;
				for (int t = j - 1; t < j + 2; t++) {
					if (t < 0) k = row - 1;
					else if (t == row) k = 0;
					else k = t;
					if (min > cost[k][i-1]) {
						min = cost[k][i - 1];
						index = k;
					}
				}
				cost[j][i] = array[j][i] + cost[index][i-1];
				itoa(index, &past, 10);
				route[j][i] = past;
			}
		}
	}

	min = cost[0][column - 1];
	for (int i = 0; i < row; i++) {
		if (min > cost[i][column - 1]) { 
			min = cost[i][column - 1]; 
			index = i;
		}
	}

	int* result = (int*)calloc(column, sizeof(int));

	printf("%d\n", min);

	for (int i = column-1; i >=0; i--) {
		result[i] = array[index][i];
		index = route[index][i] - 48;
	}

	for (int i = 0; i < column; i++) {
		printf("%d ", result[i]);
	}
}