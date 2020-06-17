#include <stdio.h>
#include <stdlib.h>

int prob1546(void) {
	int n;
	scanf("%d", &n);

	int* subj = (int*)malloc(sizeof(int)*n);
	float* res = (float*)malloc(sizeof(float)*n);
	for (int i = 0; i < n; i++)
		scanf("%d", &subj[i]);

	int m = 0;
	for (int j = 0; j < n; j++) {
		//printf("%d\n", subj[j]);
		if (subj[j] > m) {
			m = subj[j];
		}
	}
	//printf("%d\n", m);
	////////////////////////////////////
	for (int k = 0; k < n; k++) {
		//printf("%d\n", subj[k] * 100 / m);
		res[k] = (float)(subj[k] * 100) / (float)m;
		//printf("%f\n", res[k]);
	}
	////////////////////////////////////
	float sum = 0;
	for (int t = 0; t < n; t++) {
		sum = sum + res[t];
	}
	printf("%f\n", sum / (float)n);
	free(subj);
	free(res);
	return 0;
}