#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int *v = (int*)malloc(n * sizeof(int)), i;
    for (i = 0; i < n; i++)
        scanf("%d", v + i);

    int *w = (int*)malloc(n * sizeof(int)), j;
    for (j = 0; j < n; j++)
        scanf("%d", w + j);

    long long ans = 0ll;
    for (i = 0; i < n; ++i) { // for each i, place w[i] in position i of v
        j = i; // find v[i] in w at index j
        while (w[j] != v[i])
            ++j;

        while (j > i) { // swap it repeatedly to its right place
            int aux = w[j];
            w[j] = w[j - 1];
            w[j - 1] = aux;

            --j;
            ++ans;
        }
    }

    printf("%lld", ans);
    return 0;
}
