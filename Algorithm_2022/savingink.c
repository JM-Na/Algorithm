#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct s_edge {
	int x, y;
	double length;
}edge, *p_edge;

p_edge p;
FILE* fp;

double** arr;
int* parent;
double usage_ink;
char* data;
int N, num;

void input() {
	arr = (double**)calloc(N, sizeof(double*));
	for (int i = 0; i < N; i++) {
		arr[i] = (double*)calloc(2, sizeof(double));
	}
	int index1 = 0, k = 0, count = 1, index2 = 0;
	while (!feof(fp)) {
		data = fgetc(fp);
		double temp;
		if (data == '\n') {
			index1++;
			k = 0;
			count = 0;
			index2 = 0;
		}
		else if (data == ' ') {
			index2++;
			k = 0;
		}
		else {
			if (arr[index1][index2] == 0) {
				arr[index1][index2] = atof(&data);
			}
			else if (data == '.') {
				k++;
			}
			else {
				if (k == 0) {
					arr[index1][index2] *= 10;
				}
				else {
					temp = atof(&data);
					for (int i = 0; i < count; i++) {
						temp /= 10;
					}
					arr[index1][index2] += temp;
				}
			}
		}
	}
}
double cal_length(int a, int b) {
	double length = sqrt(pow(arr[a][0] - arr[b][0], 2) + pow(arr[a][1] - arr[b][1], 2));
	return length;
}
void set_edge() {
	int idx = 0;
	parent = (int*)calloc(N+1, sizeof(int));
	for (int i = 0; i < N+1; i++) {
		parent[i] = i;
	}
	for (int i = 1; i < N; i++) {
		num += i;
	}
	p = (p_edge)malloc(sizeof(edge) * num);
	for (int i = 0; i < N-1; i++) {
		for (int j = i+1; j < N; j++) {
			p[idx].x = i;
			p[idx].y = j;
			p[idx].length = cal_length(i, j);
			idx++;
		}
	}
}
void sort_edge() {
	edge temp;
	for (int i = 0; i < num-1; i++) {
		for (int j = 0; j < num-1-i; j++) {
			if (p[j].length > p[j + 1].length) {
				temp = p[j];
				p[j] = p[j + 1];
				p[j + 1] = temp;
			}
		}
	}
}
void change_parent(edge p) {
	if (parent[p.x] > parent[p.y]) {
		parent[p.x] = parent[p.y];
	}
	else if (parent[p.x] < parent[p.y]) {
		parent[p.y] = parent[p.x];
	}
}
double cal_cheapest() {
	for (int i = 0; i < num; i++) {
		if(parent[p[i].x] != parent[p[i].y]){
			usage_ink += p[i].length;
			change_parent(p[i]);
		}
	}
	return usage_ink;
}

void main() {
	fp = fopen("test.txt", "r");
	data = fgetc(fp);
	N = atoi(&data);
	data = fgetc(fp);
	
	input();
	set_edge();
	sort_edge();

	printf("%.2lf", cal_cheapest());

	for (int i = 0; i < N; i++) {
		free(arr[i]);
	}
	free(arr);
	free(p);
	free(parent);
	fclose(fp);
}