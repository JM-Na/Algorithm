#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int p, q, n, t, e, d;
long pow_(long, long, long);
int encryption(int, int, int);
int decryption(int, int, int);
int gcd(int, int);
int primaryTest(int);
void keyGeneration();

int main() {
	int input;

	printf("Generating keys.....\n");
	keyGeneration();

	printf("Keys generated.\nPublic key = (%d, %d)\nPrivate key = (%d, %d)\n", n, e, n, d);
	printf("Type your Integer : ");
	scanf_s("%d", &input);

	input = encryption(input, e, n);
	decryption(input, d, n);

	return 0;
}
int gcd(int a, int b) {
	int q1, r1, r2, r;

	if (a > b) {
		r1 = a;
		r2 = b;
	}
	else {
		r1 = b;
		r2 = a;
	}

	while (r2 > 0) {
		q1 = r1 / r2;
		r = r1 - q1 * r2;
		r1 = r2;
		r2 = r;
	}

	return r1;
}
int primaryTest(int a){
	int count = 0, last = a/2;
	for (int i = 2; i < last; i++) {
		if (a % i == 0) {
			return 0;
		}
	}
	return 1;
}
void keyGeneration() {
	do {
		p = rand();
	} while (!primaryTest(p));

	do {
		q = rand();
	} while (!primaryTest(q));

	n = p * q;
	t = (p - 1) * (q - 1);

	do {
		e = rand() % (t - 2) + 2;
	} while (gcd(e, t) != 1);

	d = inverse(t, e);
}
long pow_(long i, long j, long k) {
	double l, temp, p = 1;
	for (temp = 0; temp < j; temp++) {
		p = (p * ((double)i));
		l = (long)(p / k); //소수점 삭제.
		p = p - (l * k);
	}
	return (long)p;
}
int encryption(int input, int e, int n) {
	int i = pow_(input, e, n);
	printf("RSA encryption result = %d\n", i);
	return i;
}
int decryption(int input, int d, int n) {
	int i = pow_(input, d, n);
	printf("RSA decrption result = %d\n", i);
	return i;
}
int inverse(int a, int b)
{
	int inv;
	int q, r, r1 = a, r2 = b, t, t1 = 0, t2 = 1;

	while (r2 > 0)
	{
		q = r1 / r2;
		r = r1 - q * r2;
		r1 = r2;
		r2 = r;

		t = t1 - q * t2;
		t1 = t2;
		t2 = t;
	}

	if (r1 == 1) {
		inv = t1;
	}

	if (inv < 0) {
		inv = inv + a;
	}

	return inv;
}