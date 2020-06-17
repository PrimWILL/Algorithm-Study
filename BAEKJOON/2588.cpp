#include <stdio.h>

int prob2588(void) {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);

	int b1 = b % 10;
	int b2 = (b / 10) % 10;
	int b3 = b / 100;

	int a1 = a * b1;
	int a2 = a * b2;
	int a3 = a * b3;

	printf("%d\n", a1);
	printf("%d\n", a2);
	printf("%d\n", a3);
	printf("%d\n", a1 + a2 * 10 + a3 * 100);
	return 0;
}