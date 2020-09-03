#include <stdio.h>

void self_num(int arr[], int num) {
	if (num < 10) {
		num = num + num;
		arr[num - 1] = 1;
	}
	else if (num < 100) {
		num = num + num/10 + num%10;
		arr[num - 1] = 1;
	}
	else if (num < 1000) {
		num = num + num/100 + (num/10)%10 + num%10;
		arr[num - 1] = 1;
	}
	else if (num < 10000) {
		num = num + num/1000 + (num/100)%10 + (num/10)%10 + num%10;
		if (num <= 10000) arr[num - 1] = 1;
	}
}

int main(void) {
	int number[10001] = { 0 };
	for (int i = 1; i <= 10000; i++) {
		self_num(number, i);
	}
	for(int i = 0; i < 10000; i++) {
		if (!number[i]) {
			printf("%d\n", i + 1);
		}
	}
	return 0;
}