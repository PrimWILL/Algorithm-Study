#include <stdio.h>

int main(void) {
	int T;
	scanf("%d", &T);
	while(T--)
	{
		int R;
		char S[20];
		scanf("%d %s", &R, S);

		for(int i = 0; i < sizeof(S); i++)
		{
			for(int j = 0; j < R; j++)
			{
				printf("%c", &S[i]);
			}
		}
		printf("\n");
	}
	return 0;
}