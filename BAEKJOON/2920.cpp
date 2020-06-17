#include <stdio.h>

int prob2920(void) {
	int arr[8];
	for (int i = 0; i < 8; i++)
		scanf("%d", &arr[i]);

	int a1 = 0;
	int a2 = 0;

	for (int j = 0; j < 8; j++) {
		if (arr[j] == j + 1)
			a1++;
	}

	for (int k = 0; k < 8; k++) {
		if (arr[k] == 8 - k)
			a2++;
	}

	if (a1 == 8)
		printf("ascending\n");
	else if (a2 == 8)
		printf("descending\n");
	else
		printf("mixed\n");

	return 0;
}