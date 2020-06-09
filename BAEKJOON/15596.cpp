#include <stdio.h>
#include <stdlib.h>

long long sum(int *a, int n) {
	long long hap = 0;
	for (int j = 0; j < n; j++) {
		hap += a[j];
	}
	return hap;
}

int prob15596(void) {
	int n;
	scanf("%d", &n);
	int* a = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	long long res = sum(a, n);
	printf("%lld\n", res);
	free(a); //안녕하세요
	return 0; 
}