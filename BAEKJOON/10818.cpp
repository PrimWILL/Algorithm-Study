#include <stdio.h>
#include <stdlib.h>

int prob10818(void) {
	int n;
	scanf("%d", &n);

	int* arr = (int*)malloc(sizeof(int)*n);
	
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	int max = arr[0];
	int min = arr[0];

	for (int j = 0; j < n; j++) {
		if (arr[j] > max)
			max = arr[j];
	}
	for (int k = 0; k < n; k++) {
		if (arr[k] < min)
			min = arr[k];
	}

	printf("%d %d", min, max);
	free(arr);
	return 0;
}