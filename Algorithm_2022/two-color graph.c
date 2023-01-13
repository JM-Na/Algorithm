#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
FILE* fp;
int vert_num, edge_num;
int** line;
int* chk;

void input() {
	fp = fopen("test.txt", "r");
	while (!feof(fp)) {
		char* temp = fgetc(fp);
		vert_num = atoi(&temp);
		if (vert_num == 0)
			break;
		temp = fgetc(fp);
		temp = fgetc(fp);
		edge_num = atoi(&temp);
		line = (int**)calloc(edge_num, sizeof(int*));
		for (int i = 0; i < edge_num; i++) {
			line[i] = (int*)calloc(2, sizeof(int));
		}
		for (int i = 0; i < edge_num; i++) {
			temp = fgetc(fp);
			temp = fgetc(fp);
			line[i][0] = atoi(&temp);
			temp = fgetc(fp);
			temp = fgetc(fp);
			line[i][1] = atoi(&temp);
		}
		fgetc(fp);
	}
	fclose(fp);
}
void check() {
	int num = 0, stat = 0, temp=0;
	chk = (int*)calloc(edge_num, sizeof(int));
	for (int i = 0; i < vert_num; i++) {
		for (int j = 0; j < edge_num;j++) {
			if (line[j][0] == i) {
				chk[num] = j;
				num++;
			}
		}
		for (int j = 0; j < edge_num; j++) {
			if (line[j][1] == i) {
				for (int k = 0; k < vert_num; k++) {
					while (temp != num) {

						if (line[k][0] == line[temp][1] && line[k][1] == line[j][0]) {
							stat = 1;
							break;
						}
						else if (line[k][1] == line[temp][1] && line[k][0] == line[j][0]) {
							stat = 1;
							break;
						}
						else temp++;
					}
					temp = 0;
				}
			}
		}
		num = 0;
	}

	if (stat == 1) printf("not two-color");
	else if (stat == 0) printf("two-color");
}
int main() {

	input();
	check();
}