#include <stdio.h>
#include <string.h>
#define N 1000000

int v[N], w[N], aux[N];
long long ans;

// merges the sorted arrays w[lo .. mid) and w[mid .. hi)
void merge(int lo, int mid, int hi) {
    int i = lo, j = mid, k = 0;
    while (i < mid && j < hi)
        if (v[w[i]] < v[w[j]])
            aux[k++] = w[i++];
        else {
            aux[k++] = w[j++];
            ans += mid - i;
        }

    while (i < mid)
        aux[k++] = w[i++];

    while (j < hi)
        aux[k++] = w[j++];

    memcpy(w + lo, aux, k * sizeof(w[0])); // w[lo .. hi) = aux[0 .. k)
}

void mergesort(int lo, int hi) {
    int mid = (lo + hi) / 2;
    if (lo + 1 < mid)
        mergesort(lo, mid);

    if (mid + 1 < hi)
        mergesort(mid, hi);

    // w[lo .. mid) and w[mid .. hi) are now sorted
    merge(lo, mid, hi);
}

int main(void) {
    int n;
    scanf("%d", &n);

    int i, x;
    for (i = 0; i < n; ++i) {
        scanf("%d", &x);
        v[x - 1] = i;
    }

    for (i = 0; i < n; ++i) {
        scanf("%d", w + i);
        --w[i];
    }

    mergesort(0, n);
    printf("%lld\n", ans);
    return 0;
}
