#include <stdio.h>

void self_num(int* arr, int num) {
	int n = num;
	while (1) {
		if (num == 0) break;
		n += num%10;
		num /= 10;
	}
	if (n <= 10000)
		arr[n - 1]++;
}

int main(void) {
	int number[10000] = { 0 };
	for (int i = 1; i <= 10000; i++) {
		self_num(number, i);
	}
	for(int i = 0; i < 10000; i++) {
		if (!*(number + i)) {
			printf("%d\n", i + 1);
		}
	}
	return 0;
}