#include <stdio.h>	
#include <stdlib.h>

int prob11720(void) {
	int n = 0;
	scanf("%d", &n);

	char* num = (char*)malloc(n * sizeof(char));
	scanf("%s", num);

	int result = 0;
	for (int i = 0; i < n; i++) {
		result = result + (int)(num[i]) - '0';
	}
	printf("%d\n", result);
	return 0;
}