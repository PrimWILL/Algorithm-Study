#include <stdio.h>
int main() {
	int a[4];
	int b[5];
	
	scanf("%d %d %d %d ", &a[0], &a[1], &a[2], &a[3]);
	scanf("%d %d %d %d %d", &b[0], &b[1], &b[2], &b[3], &b[4]);
	
	int count = 0;
	for (int i = 0; i < 5; i++) {
		int temp = 0;
		for (int j = 0; j < 4; j++) {
			if (a[j] == b[i]) {
				temp++;
				break;
			}
		}
		if (temp == 0) count++;
	}
	
	printf("%d\n", count);
	return 0;
}