#include <stdio.h>
#include <stdlib.h>

int prob10871(void) {
	int N, X;
	scanf("%d %d", &N, &X);

	int* arr = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	for (int j = 0; j < N; j++) {
		if (arr[j] < X) {
			printf("%d ", arr[j]);
		}
	}
	printf("\n");
	free(arr);
	return 0;
}