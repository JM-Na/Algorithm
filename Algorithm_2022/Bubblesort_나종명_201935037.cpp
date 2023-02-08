#include<stdio.h>
#define SIZE 10

void bubblesort(int* array, const int size);
void swap(int* element1Ptr, int* element2Ptr);

int main(void)
{
	int a[SIZE] = { 2, 6, 4, 8, 10, 12, 89, 68, 45, 17 };
	int i;

	printf("Data items in original order \n");

	for (i = 0; i < SIZE; i++)
	{
		printf("%d ", a[i]);
	}

	bubblesort(a, SIZE);

	printf("\nData item in ascending order \n");

	for (i = 0; i < SIZE; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");

	return 0;
}

void bubblesort(int* array, const int size)
{
	int* elementPtr1 = NULL, * elementPtr2 = NULL;
	for (int i = size - 1; i >= 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			elementPtr1 = array + j;
			elementPtr2 = array + j + 1;
			if (*elementPtr1 > * elementPtr2)
			{
				swap(elementPtr1, elementPtr2);
			}
		}
	}
}

void swap(int* element1Ptr, int* element2Ptr)
{
	int temp; //임시저장용

	temp = *element2Ptr;
	*element2Ptr = *element1Ptr;
	*element1Ptr = temp;
}