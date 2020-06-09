#include <stdio.h>

int prob2562(void) {
	int arr[9];
	for (int i = 0; i < 9; i++)
		scanf("%d", &arr[i]);
	int num = 0;
	int max = 0;

	for (int k = 0; k < 9; k++) {
		if (arr[k] > max) {
			max = arr[k];
			num = k + 1;
		}
	}
	printf("%d\n", max);
	printf("%d\n", num);
	return 0;
}