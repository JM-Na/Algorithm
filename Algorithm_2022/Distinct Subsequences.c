#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//첫 번째 문자열의 최대 크기 정의
#define MAX_LIST_SIZE 10000
//선형 탐색 후 결과를 저장할 리스트 선언
typedef char element;
typedef struct {
	element array[MAX_LIST_SIZE];
	int size;
}ArrayListType;
//위의 리스트 대신 각 배열의 인덱스를 저장할 리스트 선언
typedef struct {
	int number[MAX_LIST_SIZE];
	int size;
}ArrayList;

ArrayListType list;
ArrayList num;

char arrX[10000], arrZ[100];
char* data;
char arrX[10000], arrZ[100];
int N;

int get_length(ArrayListType* L)
{
	return L->size;
}
void clear(ArrayListType* L, ArrayList* K) {
	L->size = 0;
	K->size = 0;
}

int is_empty(ArrayListType* L)
{
	return L->size == 0;
}
int is_full(ArrayListType* L)
{
	return L->size == MAX_LIST_SIZE;
}
void insert_last(ArrayListType* L, element item)
{
	if (is_full(L))
		printf("List Overflowed\n");
	else
		L->array[L->size++] = item;
}

int is_empty2(ArrayList* K)
{
	return K->size == 0;
}
int is_full2(ArrayList* K)
{
	return K->size == MAX_LIST_SIZE;
}
void insert_last2(ArrayList* K, int item)
{
	if (is_full2(K))
		printf("List Overflowed\n");
	else
		K->number[K->size++] = item;
}

int search(ArrayListType* L, ArrayList* K) {
	for (int i = 0; i < strlen(arrX)-1; i++) {
		//첫번째 문자와 같은 첫 입력일 경우 인덱스를 1로 설정 후 삽입
		if (arrX[i] == arrZ[0] && get_length(&list) == 0) {
			insert_last(&list, arrX[i]);
			insert_last2(&num, 1);
		}
		else if (get_length(&list) != 0) {
			int k = get_length(&list);
			for (int j = 0; j < k; j++) {
				if (arrX[i] == arrZ[K->number[j]]) {
					insert_last(&list, arrX[i]);
					insert_last2(&num, K->number[j] + 1);
				}
			}
			if (arrX[i] == arrZ[0]) {
				insert_last(&list, arrX[i]);
				insert_last2(&num, 1);
			}
		}
	}
	int count = 0;
	int length = 0;
	for (int i = 0; arrZ[i] != '\n' && arrZ[i] != '\0';i++) {
		length++;
	}
	for (int i = 0; i < get_length(&list); i++) {
		if (K->number[i] == length) count++;
	}
	return count;
}

int main() {
	FILE* fp;
	fp = fopen("test.txt", "r");
	if (fp == NULL) {
		printf("File open failed");
		return 1;
	}
	data = fgets(arrX, 7, fp);
	N = atoi(data);
	for (int i = 0; i < N; i++) {
		fgets(arrX, 10000, fp);
		fgets(arrZ, 100, fp);

		printf("%d\n", search(&list, &num));
		clear(&list, &num);
	}
	fclose(fp);
}