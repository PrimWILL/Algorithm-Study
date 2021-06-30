#include <stdio.h>

#define min(a,b) a < b ? a : b

void merge(int arr[], int sorted[], int first, int mid, int last) {
    int i = first;
    int j = mid;
    int k = first;

    while (i < mid && j < last) {
        if (arr[i] < arr[j])
            sorted[k++] = arr[i++];
        else
            sorted[k++] = arr[j++];
    }

    if (i >= mid) {
        while (j < last)
            sorted[k++] = arr[j++];
    }
    else {
        while (i < mid)
            sorted[k++] = arr[i++];
    }
}

void mergesort(int arr[], int sorted[], int n) {
    for (int i = 1; i < n; i *= 2) {
        int j;

        for (j = 0; j < n; j = j + 2*i) {
            merge(arr, sorted, j, min(j+i, n), min(j+2*i, n));
        }
        for (j = 0; j < n; j++) {
            arr[j] = sorted[j];
        }
    }
}

int main(void)
{
    int n = 0;
    scanf("%d", &n);

    int arr[n];
    int sorted[n];

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    mergesort(arr, sorted, n);

    for (int i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}