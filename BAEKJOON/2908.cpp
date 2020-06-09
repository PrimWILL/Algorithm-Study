#include <stdio.h>

int prob2908(void) {
	int a = 0;
	int b = 0;

	scanf("%d %d", &a, &b);

	int arr_a[3];
	arr_a[2] = a / 100;
	arr_a[1] = (a % 100) / 10;
	arr_a[0] = a % 10;

	int arr_b[3];
	arr_b[2] = b / 100;
	arr_b[1] = (b % 100) / 10;
	arr_b[0] = b % 10;

	a = arr_a[0] * 100 + arr_a[1] * 10 + arr_a[2];
	b = arr_b[0] * 100 + arr_b[1] * 10 + arr_b[2];

	if (a > b)
		printf("%d", a);
	else
		printf("%d", b);
	return 0;
}