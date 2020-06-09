#include <stdio.h>
#include <stdlib.h>

int prob4344(void) {
	int c;
	scanf("%d", &c);

	while (c--) {
		int n;
		scanf("%d", &n);
		int* num = (int*)malloc(sizeof(int)*n);
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);
		int sum = 0;
		for (int j = 0; j < n; j++)
			sum += num[j];
		int cnt = 0;
		for (int k = 0; k < n; k++) {
			if (num[k] > (float)sum / (float)n)
				cnt++;
		}
		printf("%.3f%%\n", (float)cnt * 100 / (float)n);
		free(num);
	}
	return 0;
}